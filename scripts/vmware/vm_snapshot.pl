#!/usr/bin/perl
#Created by Allen Sanabria aka Linux Dynasty
#This script will create a snapshot and list them for you
use strict;
use warnings;
use VMware::VIRuntime;
use XML::Writer;
my $writer = new XML::Writer( DATA_MODE => 1, DATA_INDENT => 1 );
use Data::Dumper;
use Getopt::Long;
our (
    $vm_name,    $sn_name, $descr,  $create, $delete,
    $delete_all, $vm_on,   $revert, $list,   $help
);

$vm_name = "";
GetOptions(
    'vm_name=s'  => \$vm_name,
    'sn_name=s'  => \$sn_name,
    'descr=s'    => \$descr,
    'create'     => \$create,
    'delete'     => \$delete,
    'delete_all' => \$delete_all,
    'vm_on'      => \$vm_on,
    'revert'     => \$revert,
    'list'       => \$list,
    'help'       => \$help
);
Opts::parse();
Opts::validate();
Util::connect();

if ($help) {
    &usage();
}

unless ( $vm_name and $list
    or $list
    or $vm_name and $sn_name and $delete
    or $vm_name and $delete_all
    or $vm_name and $sn_name and $create and $descr
    or $vm_name and $sn_name and $revert
    or $vm_name and $sn_name and $revert and $vm_on
    or $help )
{
    &usage();
}

# Obtain all inventory objects of the specified type
our $e_vm = "";
if ( $vm_name ) {
    $e_vm = Vim::find_entity_views(
        view_type => 'VirtualMachine',
        filter    => { name => $vm_name }
    );
}
else {
    $e_vm = Vim::find_entity_views(
        view_type => 'VirtualMachine' 
    );
}
foreach (@$e_vm) {
    if ( $list and $_->name eq $vm_name ) {
        if ( Dumper($_) =~ /rootSnapshotList/ and $list ) {
            snap_test($_);
        }
        else {
            print "No Snap Shots for $vm_name exist\n";
            exit;
        }
    }
    if ( $list and not $vm_name ) {
        if ( Dumper($_->snapshot) =~ /rootSnapshotList/ and $list ) {
            my $root = $_->snapshot->rootSnapshotList;
            foreach my $snapper (@$root) {
            print $_->name,"\n";
            snap_print(
                $snapper->name, $snapper->description, $snapper->state->val,
                $snapper->vm->type, $snapper->createTime
            );
                if ( Dumper($snapper) =~ /childSnapshotList/ ) {
                        my $child = $snapper->childSnapshotList;
                    foreach my $snappy (@$child) {
                        snap_print(
                            $snappy->name, $snappy->description, $snappy->state->val,
                            $snappy->vm->type, $snappy->createTime
                        );
                    }
                }
            }
        }
    }

    if ( $create and $_->name eq $vm_name ) {
        snap_create($_);
    }

    if ( $delete and $_->name eq $vm_name and $sn_name ) {
        snap_test($_);
    }

    if ( $delete_all and $_->name eq $vm_name ) {
        snap_delete_all($_);
    }

    if ( $revert and $_->name eq $vm_name and $sn_name ) {
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
        "\nSnapshot '" . $sn_name . "' completed for VM " . $vm_name );
    exit;
}

sub snap_print {
    print "  name:\t\t",       $_[0], "\n";
    print "  description:\t",  $_[1], "\n";
    print "  state:\t",      $_[2], "\n";
    print "  vm type:\t",      $_[3], "\n";
    print "  time created:\t", $_[4], "\n\n";
    return;
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
                if ($delete) {
                    snap_delete( $_, $count );
                }
                if ($revert) {
                    snap_revert( $_, $count );
                }
            }
        }
        if ($list) {
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
        print "$sn_name does not exist on host $vm_name\n";
        exit;
    }
    my $snapshot = Vim::get_view( mo_ref => $snapname->snapshot );
    $snapshot->RemoveSnapshot( removeChildren => 0 );

    Util::trace( 0,
        "\nSnapshot '" . $sn_name . "' removed for VM " . $vm_name . "\n" );
    exit;

}

sub snap_delete_all {
    $_->RemoveAllSnapshots();
    Util::trace( 0,
        "\n All Snapshot have been ' removed for VM " . $vm_name . "\n" );
    exit;
}

sub snap_revert {
    my $snapname = $_[0];
    my $count    = $_[1];
    if ( $count < 1 ) {
        print "$sn_name does not exist on host $vm_name\n";
        exit;
    }
    my $snapshot = Vim::get_view( mo_ref => $snapname->snapshot );
    $snapshot->RevertToSnapshot();
    Util::trace( 0,
            "\nOperation :: Revert To Snapshot " . $sn_name
          . " For Virtual Machine "
          . $vm_name
          . " completed \n" );
    if ($vm_on) {
        foreach (@$e_vm) {
            if ( $_->name eq $vm_name ) {
                $_->PowerOnVM;
                Util::trace( 0,
                    "\n Virtual machine '$vm_name' has been started \n" );
                exit;
            }
        }
    }
}

sub usage {

    print "\tusage       : $0 [--help]\n";
    print
"\t--vm_name         : This is the VM name you want to create the snapshot of\n";
    print "\t--sn_name         : This will be the name of the snapshot\n";
    print
      "\t--descr           : This will be the description of the snapshot\n";
    print
"\texample        : $0 --vm_name vm_name --create --descr tester --sn_name 'Initial snapshot'\n";
    print
"\texample        : $0 --vm_name vm_name --delete --sn_name 'Initial snapshot'\n";
    print
"\texample        : $0 --vm_name vm_name --revert --sn_name 'Initial snapshot'\n";
    print
"\texample        : $0 --vm_name vm_name --revert --sn_name 'Initial snapshot' --vm_on\n";
    print
"\texample        : $0 --list\n";
    print "\texample        : $0 --vm_name --list \n";
    exit;
}
Util::disconnect();
