#!/usr/bin/perl
#
# Description: CGI script to access common VMware Virtual Machine methods

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
use Time::HiRes qw(sleep);
use Data::Dumper;
use POSIX qw(setsid);
$| = 1; # This will flush all buffers

our (
    $vmachine, $snapshot, $descr,  $vm_status,
    $help,   $action,   $url,        $status,
    $e_vm,   $g_vm
);

require "ESX.pm";

our $rc   = 0;
our $cgi  = new CGI;
our $host = $cgi->param("host") || $cgi->remote_host;
print $cgi->header;
$cgi->param("host");
$vmachine   = $cgi->param("vmachine");
$snapshot   = $cgi->param("snapshot");
$descr     = $cgi->param("descr");
$vm_status = $cgi->param("vm_status");
$action    = $cgi->param("action");

if ($help) {
    &usage();
}

unless ( $vmachine and $action eq "list"
    or $vmachine and $snapshot and $action eq "delete"
    or $vmachine and $action eq "delete_all"
    or $vmachine and $snapshot and $action eq "create"     and $descr
    or $vmachine and $snapshot and $action eq "snap_clean" and $descr
    or $vmachine and $snapshot and $action eq "revert"
    or $vmachine and $snapshot and $action eq "revert_clean"
    or $vmachine and $action eq "vmachineOff"
    or $vmachine and $action eq "vmachineShutdown"
    or $vmachine and $action eq "vmachineOn"
    or $vmachine and $action eq "vmachineReset"
    or $help )
{
    &usage();
}

my $pid = fork();
if ( $pid == 0 ) {
    chdir '/' or die "Can't chdir to /: $!";
    setsid    or die "Can't start a new session: $!";

    # Obtain all inventory objects of the specified type
    if ($vmachine) {
        $e_vm = Esx1::get_vm($vmachine);
    }

    if ( Dumper($e_vm) !~ /$vmachine/ ) {
        print "$vmachine does not exist<br>";
        exit;
    }

    foreach (@$e_vm) {
        Esx1::vm_values( $_, $vmachine, $snapshot, $descr, $action );
        if ( $action eq "list" and $_->name eq $vmachine ) {
        eval {
            if ( $_->snapshot->rootSnapshotList and $action eq "list" ) {
                snap_print($_);
                }
        };
        unless  ( $_->snapshot ) {
        print "SnapShots do not exist for $vmachine <br>";
        }
        }

        if ( $action eq "create" and $_->name eq $vmachine ) {
            Esx1::snap_create( );
        }

        if ( $action eq "delete" and $_->name eq $vmachine and $snapshot ) {
            Esx1::verify_snap( $_ );
        }

        if ( $action eq "delete_all" and $_->name eq $vmachine ) {
            Esx1::verify_snap( $_ );
        }

        if ( $action eq "revert" and $_->name eq $vmachine and $snapshot ) {
            Esx1::verify_snap( $_ );
        }
        if ( $action eq "vmachineOff" and $_->name eq $vmachine ) {
            Esx1::vmachineOff( );
        }
        if ( $action eq "vmachineShutdown" and $_->name eq $vmachine ) {
            Esx1::vmachineShutdown( );
        }
        if ( $action eq "vmachineOn" and $_->name eq $vmachine ) {
            Esx1::vmachineOn( );
        }
        if ( $action eq "vmachineReset" and $_->name eq $vmachine ) {
            Esx1::vmachineReset( );
        }
        if ( $action eq "snap_clean" and $_->name eq $vmachine ) {
            Esx1::vmachineShutdown( );
        $status = clean( );
            if ( $status eq "notRunning" ) {
                Esx1::vmachineOff( );
                sleep 10;
                Esx1::snap_create( );
                Esx1::vmachineOn( );
            }
    }
        
    if ( $action eq "revert_clean" and $_->name eq $vmachine and $snapshot ) {
        if ( $_->guest->guestState eq "running" ) {
            Esx1::vmachineShutdown( $_, $vmachine );
        $status = clean( );
         }
            elsif ( $_->guest->guestState eq "notRunning" ) {
                Esx1::verify_snap( $_ );
            }
        }

    }

    sub clean {
        my $fet;
            do {
        my $sl = ( int( rand(270) ) + 30 );
                sleep $sl;
                $g_vm = Esx1::get_vm($vmachine);
                foreach my $fe (@$g_vm) {
                    $fet = $fe->guest->guestState;
                }
            } while ( $fet eq "running" );
        return $fet;
     }

    sub snap_print {
        my $sn1;
        if ( Dumper( $_->snapshot ) =~ /(rootSnapshotList)/ ) {
            $sn1 = $_->snapshot->rootSnapshotList;
        }
        elsif ( Dumper($_) =~ /(childSnapshotList)/ ) {
            $sn1 = $_->childSnapshotList;
        }

        foreach (@$sn1) {
            print "<pre>";
            print "snap name:\t",   $_->name,        "<br>";
            print "description:\t", $_->description, "<br>";
            print "state:\t\t", $_->state->val, "<br>";
            print "vm type:\t", $_->vm->type,   "<br>";
            print "time created:\t", $_->createTime, "<br>";
            print "\n";
            print "<pre>";

            if ( $_->childSnapshotList ) {
                snap_print($_);
            }
        }
    }

    sub usage {

        print "\tusage       : $0 [--help]<br>";
        print
": <br>The example below will create a snapshot with a name of Initial_snapshot for Virtual Machine VirtualMachineName with the description of tester<br>";
        print
"\texample        : wget 'http://VCserver/cgi/vm_admin.cgi?&vmachine=VirtualMachineName&action=create&descr=tester&=snapshot=Initial_snapshot'<br>";
        print
": <br>The example below will create a clean snapshot with a name of Initial_snapshot from a shutdown state for Virtual Machine VirtualMachineName with the description of tester<br>";
        print
"\texample        : wget 'http://VCserver/cgi/vm_admin.cgi?&vmachine=VirtualMachineName&action=snap_clean&descr=tester&=snapshot=Initial_snapshot'<br>";
        print
": <br>The example below will delete the snapshot named Initial_snapshot for Virtual Machine VirtualMachineName<br>";
        print
"\texample        : wget 'http://VCserver/cgi/vm_admin.cgi?&vmachine=VirtualMachineName&action=delete&snapshot=Initial_snapshot'<br>";
        print
": <br>The example below will revert to the snapshot named Initial_snapshot for Virtual Machine VirtualMachineName and turn the Virtual Machine back on<br>";
        print
"\texample        : wget 'http://VCserver/cgi/vm_admin.cgi?&vmachine=VirtualMachineName&action=revert&snapshot&Initial_snapshot'<br>";
        print
": <br>The example below will revert to the snapshot named Initial_snapshot but shotdown cleanly for Virtual Machine VirtualMachineName and turn the Virtual Machine back on<br>";
        print
"\texample        : wget 'http://VCserver/cgi/vm_admin.cgi?&vmachine=VirtualMachineName&action=revert_clean&snapshot&Initial_snapshot'<br>";
        print
": <br>The example below will list all snapshots for Virtual Machine VirtualMachineName<br>";
        print
"\texample        : wget 'http://VCserver/cgi/vm_admin.cgi?&vmachine=VirtualMachineName&action=list'<br>";
        print
": <br>The example below will power off the Virtual machinee VirtualMachineName<br>";
        print
"\texample        : wget 'http://VCserver/cgi/vm_admin.cgi?&vmachine=VirtualMachineName&action=vmachineOff'<br>";
        print
": <br>The example below will power on the Virtual machinee VirtualMachineName<br>";
        print
"\texample        : wget 'http://VCserver/cgi/vm_admin.cgi?&vmachine=VirtualMachineName&action=vmachineOn'<br>";
        print
": <br>The example below will reset the Virtual machinee VirtualMachineName<br>";
        print
"\texample        : wget 'http://VCserver/cgi/vm_admin.cgi?&vmachine=VirtualMachineName&action=vmachineReset'<br>";
        exit;
    }
}
unlink "saved_session";
Util::disconnect();
