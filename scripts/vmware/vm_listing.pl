#!/usr/bin/perl
#Created by Allen Sanabria aka Linux Dynasty
use strict;
use warnings;
use VMware::VIRuntime;
use XML::Writer;
my $writer = new XML::Writer( DATA_MODE => 1, DATA_INDENT => 1 );
use Data::Dumper;
use Getopt::Long;
our ( $linux, $windesk, $winserv, $hostname, $xml, $help );
GetOptions(
    'linux'      => \$linux,
    'windesk'    => \$windesk,
    'winserv'    => \$winserv,
    'hostname=s' => \$hostname,
    'xml'        => \$xml,
    'help'       => \$help
);
Opts::parse();
Opts::validate();
Util::connect();

if ($help) {
    &usage();
}

# Obtain all inventory objects of the specified type
my $e_vm = Vim::find_entity_views( view_type => 'VirtualMachine' );

foreach my $views ( sort(@$e_vm) ) {
    if ( Dumper( $views->guest ) =~ /(linuxGuest)/ and $linux ) {
        &letsGo( $views->name, $views->guest );
    }

    if ( Dumper( $views->guest ) =~ /(Microsoft\s+Windows\s+Server.*)/
        and $winserv )
    {
        &letsGo( $views->name, $views->guest );
    }

    if ( Dumper( $views->guest ) =~ /(Microsoft\s+Windows\s+(XP|Vista).*)/
        and $windesk )
    {
    print "Im here\n";
        &letsGo( $views->name, $views->guest );
    }

    if ($hostname) {
        if ( $hostname =~ /$views->hostName/ ) {
            &letsGo( $views->name, $views->guest );
        }
    }
    unless ( $hostname or $windesk or $winserv or $linux ) {
        &letsGo( $views->name, $views->guest );
    }
    else {
        $hostname = "";
    }
}

sub usage {

    print "\tusage       : $0 [--help]\n";
    print "\t--linux        : This will print out all Linux Servers\n";
    print "\t--winserv      : This will print out all Windows Servers\n";
    print "\t--windesk      : This will print out all Windows Desktops\n";
    print "\t--xml          : This will print out all info in XML\n";
    print "\texample        : $0 --xml --linux \n";
    print "\texample        : $0 --winserv \n";
    print "\texample        : $0  \n";
    exit;
}

sub letsGo {
    my $vm_name = shift @_;
    my $guest   = shift @_;
    my @gval    = qw /guestFullName guestId guestFamily guestState
      numCPU memoryMB ipAddress toolsVersion toolsStatus/;
    my @netval  = qw /deviceConfigId network macAddress connected/;
    my @diskval = qw /diskPath capacity freeSpace/;
    my $i       = 0;
    my $j       = 0;
    my $k       = 0;
    if ($xml) {
        $writer->startTag($vm_name);
        $writer->startTag("host_config");
        $writer->startTag("name");
        $writer->characters($vm_name);
        $writer->endTag("name");
    }
    else {
        print "#################################################\n";
        print "\t\t$vm_name\n";
        print "--------------------host_config-------------------\n";
    }
    foreach my $value (@gval) {
        unless ( Dumper($guest) =~ /$value/ ) {
            &NA( $gval[$i] );
            $i += 1;
        }
        else {
            if ( Dumper( $guest->$value ) =~ /val/ ) {
                &AV( $gval[$i], $guest->$value->val );
                $i += 1;
            }
            else {
                &AV( $gval[$i], $guest->$value );
                $i += 1;
            }
        }
    }
    if ($xml) {
        $writer->endTag("host_config");
    }
    else {
        print "\n";
    }
    if ( $guest->net ) {
        if ($xml) {
            $writer->startTag("network_info");
        }
        else {
            print "--------------network_info-----------------\n";
        }
        if ( Dumper($guest) =~ /net/ ) {
            my $vm_nic = $guest->net;
            foreach my $nic (@$vm_nic) {
                foreach my $nval (@netval) {
                    &AV( $nval, $nic->$nval );
                }
            }
        }
        if ($xml) {
            $writer->endTag("network_info");
        }
        else {
            print "\n";
        }
    }
    else {
        if ($xml) {
            $writer->startTag("network_info");
        }
        else {
            print "----------------network_info------------------\n";
        }
        &NA("deviceConfigId");
        &NA("network");
        &NA("macAddress");
        &NA("connected");
        if ($xml) {
            $writer->endTag("network_info");
        }
        else {
            print "\n";
        }
    }
    if ( $guest->disk ) {
        if ($xml) {
            $writer->startTag("disk_info");
        }
        else {
            print "-----------------disk_info-------------------\n";
        }
        if ( Dumper($guest) =~ /disk/ ) {
            my $vm_disk = $guest->disk;
            foreach my $disk (@$vm_disk) {
                foreach my $dval (@diskval) {
                    &AV( $dval, $disk->$dval );
                }
            }
        }
        if ($xml) {
            $writer->endTag("disk_info");
        }
        else {
            print "\n";
        }
    }
    else {
        if ($xml) {
            $writer->startTag("disk_info");
        }
        else {
            print "--------------disk_info--------------------\n";
        }
        &NA("diskPath");
        &NA("capacity");
        &NA("freeSpace");
        if ($xml) {
            $writer->endTag("disk_info");
        }
        else {
            print "\n";
        }
    }
    if ($xml) {
        $writer->endTag($vm_name);
        $writer->end();
    }
    else {
        print "#############################################\n\n";
    }
}

sub AV {
    my $meth = shift @_;
    my $val  = shift @_;
    if ($xml) {
        $writer->startTag($meth);
        $writer->characters($val);
        $writer->endTag($meth);
    }
    else {
        if ( $meth =~ /guestId|numCPU|network/ ) {
            print "$meth\t\t\t $val\n";
        }
        else {
            print "$meth\t\t $val\n";
        }
    }
}

sub NA {
    my $meth = shift @_;
    my $val  = "Not Available";
    if ($xml) {
        $writer->startTag($meth);
        $writer->characters($val);
        $writer->endTag($meth);
    }
    else {
        if ( $meth =~ /guestId|numCPU|network/ ) {
            print "$meth\t\t\t $val\n";
        }
        else {
            print "$meth\t\t $val\n";
        }
    }
}
Util::disconnect();
