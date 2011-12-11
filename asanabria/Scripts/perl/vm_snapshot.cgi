#!/usr/bin/perl
#Created by Allen Sanabria aka Linux Dynasty
#This script will create a snapshot and list them for you
#Copyright (C) 2008 Allen Sanabria

#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along
#with this program; if not, write to the Free Software Foundation, Inc.,
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


use CGI;
use strict;
use warnings;
use VMware::VIRuntime;
use XML::Writer;
my $writer = new XML::Writer( DATA_MODE => 1, DATA_INDENT => 1 );
use Data::Dumper;
our ( $vm_name, $sn_name, $descr, $vm_status, $help, $action );

Opts::parse();
Opts::validate();
Util::connect();

our $rc   = 0;
our $cgi  = new CGI;
our $host = $cgi->param("host") || $cgi->remote_host;
print $cgi->header;
$cgi->param("host");
$vm_name   = $cgi->param("vm_name");
$sn_name   = $cgi->param("sn_name");
$descr     = $cgi->param("descr");
$vm_status = $cgi->param("vm_status");
$action    = $cgi->param("action");

if ($help) {
    &usage();
}

unless ( $vm_name and $action eq "list"
    or $vm_name and $sn_name and $action eq "delete"
    or $vm_name and $action eq "delete_all"
    or $vm_name and $sn_name and $action eq "create" and $descr
    or $vm_name and $sn_name and $action eq "revert"
    or $vm_name and $sn_name and $action eq "revert" and $vm_status
    or $help )
{
    &usage();
}

# Obtain all inventory objects of the specified type
our $e_vm = Vim::find_entity_views(
    view_type => 'VirtualMachine',
    filter    => { name => $vm_name }
);

if ( Dumper($e_vm) !~ /$vm_name/ ) {
    print "$vm_name does not exist<br>";
    exit;
}

foreach (@$e_vm) {
    if ( $action eq "list" and $_->name eq $vm_name ) {
        if ( Dumper($_) =~ /rootSnapshotList/ and $action eq "list" ) {
            snap_test($_);
        }
        else {
            print "No Snap Shots for $vm_name exist<br>";
            exit;
        }
    }

    if ( $action eq "create" and $_->name eq $vm_name ) {
        snap_create($_);
    }

    if ( $action eq "delete" and $_->name eq $vm_name and $sn_name ) {
        snap_test($_);
    }

    if ( $action eq "delete_all" and $_->name eq $vm_name ) {
        snap_delete_all($_);
    }

    if ( $action eq "revert" and $_->name eq $vm_name and $sn_name ) {
        snap_test($_);
    }
}

sub snap_create {
    $_->CreateSnapshot(
        name        => $sn_name,
        description => $descr,
        memory      => 0,
        quiesce     => 1
    );

    Util::trace( 0,
        "<br>Snapshot '" . $sn_name . "' completed for VM " . $vm_name );
    $rc += $? >> 8;
    exit $rc;

    #exit;
}

sub snap_print {
    my $snap_name = shift;
    my $description = shift;
    my $state = shift;
    my $vm_type = shift;
    my $time_c = shift;
    print "<pre>";
    print "snap name:\t",    $snap_name ."<br>";
    print "description:\t",  $description ."<br>";
    print "state:\t\t",      $state ."<br>";
    print "vm type:\t",      $vm_type ."<br>";
    print "time created:\t", $time_c ."<br>";
    print "</pre>";
}


sub snap_test {
    my $count = 0;
    my $sn1;
    if ( Dumper( $_->snapshot ) =~ /(rootSnapshotList)/ ) {
        $sn1 = $_->snapshot->rootSnapshotList;
    }
    elsif ( Dumper($_) =~ /(childSnapshotList)/ ) {
        $sn1 = $_->childSnapshotList;
    }
    foreach (@$sn1) {
        if ($sn_name) {
            if ( $_->name eq $sn_name ) {
                $count = +1;
                if ( $action eq "delete" ) {
                    snap_delete( $_, $count );
                }
                if ( $action eq "revert" ) {
                    snap_revert( $_, $count );
                }
            }
        }
        if ( $action eq "list" ) {
            snap_print(
                $_->name,     $_->description, $_->state->val,
                $_->vm->type, $_->createTime
            );
            if ( $_->childSnapshotList ) {
                snap_test($_);
            }
        }
        elsif ( $_->childSnapshotList ) {
            snap_test($_);
        }
    }
}

sub snap_delete {
    my $snapname = $_[0];
    my $count    = $_[1];
    if ( $count < 1 ) {
        print "$sn_name does not exist on host $vm_name<br>";
        exit;
    }
    my $snapshot = Vim::get_view( mo_ref => $snapname->snapshot );
    $snapshot->RemoveSnapshot( removeChildren => 0 );

    Util::trace( 0,
        "<br>Snapshot '" . $sn_name . "' removed for VM " . $vm_name . "<br>" );
    $rc += $? >> 8;
    exit $rc;

    #exit;

}

sub snap_delete_all {
    $_->RemoveAllSnapshots();
    Util::trace( 0,
        "<br> All Snapshot have been ' removed for VM " . $vm_name . "<br>" );
    $rc += $? >> 8;
    exit $rc;

    #exit;
}

sub snap_revert {
    my $snapname = $_[0];
    my $count    = $_[1];
    if ( $count < 1 ) {
        print "$sn_name does not exist on host $vm_name<br>";
        exit;
    }
    my $snapshot = Vim::get_view( mo_ref => $snapname->snapshot );
    $snapshot->RevertToSnapshot();
    Util::trace( 0,
            "<br>Operation :: Revert To Snapshot " . $sn_name
          . " For Virtual Machine "
          . $vm_name
          . " completed <br>" );
    $rc += $? >> 8;
    exit $rc;
    if ( $vm_status eq "vm_on" ) {
        foreach (@$e_vm) {
            if ( $_->name eq $vm_name ) {
                $_->PowerOnVM;
                Util::trace( 0,
                    "<br> Virtual machine '$vm_name' has been started <br>" );
                $rc += $? >> 8;
                exit $rc;

                #exit;
            }
        }
    }
}

sub usage {

    print "\tusage       : $0 [--help]<br>";
    print
"\t--vm_name         : This is the VM name you want to create the snapshot of<br>";
    print "\t--sn_name         : This will be the name of the snapshot<br>";
    print
      "\t--descr           : This will be the description of the snapshot<br>";
    print
": <br>The example below will create a snapshot with a name of Initial_snapshot for Virtual Machine vm_name with the description of tester<br>";
    print
"\texample        : curl 'http://webserver/cgi-dir/script.cgi?&vm_name=vm_name&action=create&descr=tester&=sn_name=Initial_snapshot'<br>";
    print
": <br>The example below will delete the snapshot named Initial_snapshot for Virtual Machine vm_name<br>";
    print
"\texample        : curl 'http://webserver/cgi-dir/script.cgi?&vm_name=vm_name&action=delete&sn_name=Initial_snapshot'<br>";
    print
": <br>The example below will revert to the snapshot named Initial_snapshot for Virtual Machine vm_name<br>";
    print
"\texample        : curl 'http://webserver/cgi-dir/script.cgi?&vm_name=vm_name&action=revert&sn_name&Initial_snapshot'<br>";
    print
": <br>The example below will revert to the snapshot named Initial_snapshot for Virtual Machine vm_name and turn the Virtual Machine back on<br>";
    print
"\texample        : curl 'http://webserver/cgi-dir/script.cgi?&vm_name=vm_name&action=revert&sn_name&Initial_snapshot&vm_status=vm_on'<br>";
    print
": <br>The example below will list all snapshots for Virtual Machine vm_name<br>";
    print
"\texample        : curl 'http://webserver/cgi-dir/script.cgi?&vm_name=vm_name&action=list'<br>";
    exit;
}
Util::disconnect();
