#!/usr/bin/perl

#This script will list all your Virtual Machines and grab the vmTools
#that is running or not running or not install or all of them.
#Copyright (C) 2009 Allen Sanabria

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

use strict;
use warnings;
use VMware::VIRuntime;
use Data::Dumper;
use Getopt::Long;
our ( $toolsOld, $toolsNotInstalled, $toolsOk, $all, $toolsNotRunning, $vm_name,
    $help );
GetOptions(
    'toolsOld'          => \$toolsOld,
    'toolsNotInstalled' => \$toolsNotInstalled,
    'toolsOk'           => \$toolsOk,
    'all'               => \$all,
    'toolsNotRunning'   => \$toolsNotRunning,
    'vm_name=s'         => \$vm_name,
    'help'              => \$help
);
Opts::parse();
Opts::validate();
Util::connect();

sub usage {

    print "\thelp              : $0 [--help]\n";
    print
"\t--toolsOld             : This will print out all the Virtual Machines with an Old version of vmTools and you need to upgrade\n";
    print
"\t--toolsNotInstalled    : This will print out all the Virtual Machines with vmTools Not Installed\n";
    print
"\t--toolsNotRunning      : This will print out all the Virtual Machines with vmTools Not Running\n";
    print
"\t--toolsOk              : This will print out all Virtual Machines with vmTools running \n";
    print
"\t--all             : This will print out all Virtual Machines with vmTools installed or not installed\n";
    print "\texample           : $0 --toolsOld \n";
    print "\texample           : $0 --toolsOk \n";
    print "\texample           : $0 --toolsNotInstalled \n";
    print "\texample           : $0 --toolsRunning \n";
    print "\texample           : $0 --all --vm_name \"vm_name\" \n";
    print "\texample           : $0 --all \n";
    exit;
}

# Obtain all inventory objects of the specified type
if (   $toolsOld
    or $toolsNotInstalled
    or $toolsOk
    or $toolsNotRunning
    or $all
    or $all and $vm_name )
{
    &checkTools();
}
else {
    &usage();
}

sub checkTools {
    my $e_vm = "";
    if ($vm_name) {
        $e_vm = Vim::find_entity_views(
            view_type => 'VirtualMachine',
            filter    => { name => $vm_name }
        );
    }
    else {
        $e_vm = Vim::find_entity_views( view_type => 'VirtualMachine' );
    }

    foreach my $views ( sort(@$e_vm) ) {
        my $vm_name = $views->name;
        if ( Dumper( $views->guest ) =~ /toolsStatus/ ) {
            my $toolsStatus  = $views->guest->toolsStatus->val;
            my $toolsVersion = "";
            if ( $toolsStatus =~ /toolsOk/ ) {
                if ( Dumper( $views->guest ) =~ /toolsVersion/ ) {
                    $toolsVersion = $views->guest->toolsVersion;
                }
                else {
                    $toolsVersion =
                      "Please Check vmTools as I can not get the version";
                }
                if ( $toolsOk or $all ) {
                    print $vm_name, "\n";
                    print "  $toolsStatus and $toolsVersion\n\n";
                }
            }
            elsif ( $toolsStatus =~ /toolsOld/ ) {
                if ( Dumper( $views->guest ) =~ /toolsVersion/ ) {
                    $toolsVersion = $views->guest->toolsVersion;
                    if ( $toolsOld or $all ) {
                        print $vm_name, "\n";
                        print "  $toolsStatus and $toolsVersion\n\n";
                    }
                }
            }
            elsif ( $toolsStatus =~ /toolsNotInstalled/ ) {
                if ( $toolsNotInstalled or $all ) {
                    print $vm_name, "\n";
                    print "  ", $views->guest->toolsStatus->val, "\n\n";
                }
            }
            elsif ( $toolsStatus =~ /NotRunning/ ) {
                if ( $toolsNotRunning or $all ) {
                    print $vm_name, "\n";
                    print "  ", $views->guest->toolsStatus->val, "\n\n";
                }
            }
        }
    }
}
Util::disconnect();
