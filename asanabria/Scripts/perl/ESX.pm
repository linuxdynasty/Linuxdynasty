#!/usr/bin/env perl
#Description: VMware ESX 3.+ Perl Module with common Virtual Machine functions that can be used
#to do simple task's, like create/delete/revert/list snapshots as well as other tasks....
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

package ESX;
use strict;
use Data::Dumper;
use VMware::VIRuntime;
our ( $url, $o_vm, $username, $password, $file );
my @info;

#For the small section below you will need a file called .visdkrc
#In this file you will need 3 lines.
#The 1st line is the vc_server, 2nd line is the user name and 3rd line is the passwd, example below
#https://vc_server/sdk/webService
#user_name
#password

open VISDKRC, ".visdkrc";
while (<VISDKRC>) {
    chomp $_;
    push( @info, $_ );
}
close VISDKRC;
$url      = shift @info;
$username = shift @info;
$password = shift @info;
$file     = 'saved_session';
Vim::login(
    service_url => $url,
    user_name   => $username,
    password    => $password
);

# save the session to a file
if ( defined($file) ) {
    Vim::save_session( session_file => $file );

    #   print "Session information saved.<br>";
}
else {
    print "\nMust specify save session file for this sample\n";
    exit '1';
}

sub get_vm {
    my $vm_name = shift;
    $o_vm = Vim::find_entity_views(
        view_type => 'VirtualMachine',
        filter    => { name => $vm_name }
    );
    return ($o_vm);
}

sub get_all_vm {
    $o_vm = Vim::find_entity_views( view_type => 'VirtualMachine' );
    return ($o_vm);
}

sub vm_values {
    our $snap = shift;
    our $vm = $snap;
    our $vm_name = shift;
    our $sn_name = shift;
    our $descr   = shift;
    our $action  = shift;

    sub verify_snap {
        my $count = 0;
        my $sn1;
        if ( Dumper( $snap->snapshot ) =~ /(rootSnapshotList)/ ) {
            $sn1 = $snap->snapshot->rootSnapshotList;
        }
        elsif ( Dumper($snap) =~ /(childSnapshotList)/ ) {
            $sn1 = $snap->childSnapshotList;
        }
        if ( Dumper( $snap->snapshot ) =~ /rootSnapshotList/
            and $action eq "delete_all" )
        {
            snap_delete_all($snap);
        }
        foreach (@$sn1) {
            if ( $_->name eq $sn_name ) {
                $count = +1;
                if ( $action eq "delete" ) {
                    snap_delete( $_, $count );
                }
                if ( $action eq "revert" ) {
                    snap_revert( $_, $count );
                }
                if ( $action eq "revert_clean" ) {
                    snap_revert( $_, $count );
                }
            }
            elsif ( $_->childSnapshotList ) {
                verify_snap($_);
            }
            unless ( $_->name =~ /$sn_name/ ) {
                    print "SnapShot $sn_name does not exist\n";
            }
        }
            print "SnapShot $sn_name does not exist\n";
    }

    sub snap_create {
        eval {
            $snap->CreateSnapshot(
                name        => $sn_name,
                description => $descr,
                memory      => 0,
                quiesce     => 1
            );
                Util::trace( 0,
                    "Snapshot $sn_name  completed for VM $vm_name\n" );
        };
        if ($@) {
            if ( ref($@) eq 'SoapFault' ) {
                if ( ref( $@->detail ) eq 'InvalidName' ) {
                        Util::trace( 0, "Snapshot name is invalid\n" );
                }
                elsif ( ref( $@->detail ) eq 'InvalidState' ) {
                        Util::trace(
                            0,
"\nOperation cannot be performed in the current state
                                 of the virtual machine\n"
                        );
                }
                elsif ( ref( $@->detail ) eq 'NotSupported' ) {
                        Util::trace( 0, "\nHost product does not support snapshots.\n" );
                }
                elsif ( ref( $@->detail ) eq 'InvalidPowerState' ) {
                        Util::trace(
                            0,
"\nOperation cannot be performed in the current power state
                            of the virtual machine.\n"
                        );
                }
                elsif ( ref( $@->detail ) eq 'InsufficientResourcesFault' ) {
                        Util::trace( 0,
                            "\nOperation would violate a resource usage policy.\n"
                        );
                }
                elsif ( ref( $@->detail ) eq 'HostNotConnected' ) {
                        Util::trace( 0, "\nHost not connected.\n" );
                }
                elsif ( ref( $@->detail ) eq 'NotFound' ) {
                        Util::trace( 0,
                            "\nVirtual machine does not have a current snapshot\n"
                        );
                }
                else {
                        Util::trace( 0, "\nFault: " . $@ . "\n\n" );
                }
            }
            else {
                    Util::trace( 0, "\nFault: " . $@ . "\n\n" );
            }
        }
    }

    sub snap_delete {
        my $snapname = shift;
        my $count    = shift;
        if ( $count < 1 ) {
                print "$sn_name does not exist on host $vm_name\n";
        }
        my $snapshot = Vim::get_view( mo_ref => $snapname->snapshot );
        eval {
            $snapshot->RemoveSnapshot( removeChildren => 0 );
                Util::trace( 0,
                        "\nSnapshot " . $sn_name
                      . " removed for VM "
                      . $vm_name
                      . "\n" );
        };
        if ($@) {
            if ( ref($@) eq 'SoapFault' ) {
                if ( ref( $@->detail ) eq 'InvalidState' ) {
                        Util::trace(
                            0,
"\nOperation cannot be performed in the current state
                                 of the virtual machine\n"
                        );
                }
                elsif ( ref( $@->detail ) eq 'HostNotConnected' ) {
                        Util::trace( 0, "\nHost not connected.\n" );
                }
                else {
                        Util::trace( 0, "\nFault: " . $@ . "\n\n" );
                }
            }
            else {
                    Util::trace( 0, "\nFault: " . $@ . "\n\n" );
            }
        }
    }

    sub snap_delete_all {
        eval {
            $snap->RemoveAllSnapshots();
               Util::trace( 0,
                       "\n All Snapshot have been removed for VM " . $vm_name . "\n" );
        };
        if ($@) {
            if ( ref($@) eq 'SoapFault' ) {
                if ( ref( $@->detail ) eq 'InvalidState' ) {
                        Util::trace(
                            0,
"\nOperation cannot be performed in the current state
                                 of the virtual machine\n"
                        );
                }
                elsif ( ref( $@->detail ) eq 'NotSupported' ) {
                        Util::trace( 0,
                            "\nHost product does not support snapshots.\n" );
                }
                elsif ( ref( $@->detail ) eq 'InvalidPowerState' ) {
                        Util::trace(
                            0,
"\nOperation cannot be performed in the current power state
                                 of the virtual machine.\n"
                        );
                }
                elsif ( ref( $@->detail ) eq 'HostNotConnected' ) {
                        Util::trace( 0, "\nHost not connected.\n" );
                }
                else {
                        Util::trace( 0, "\nFault: " . $@ . "\n\n" );
                }
            }
            else {
                    Util::trace( 0, "\nFault: " . $@ . "\n\n" );
            }
        }
    }

    sub vmachineOn {
    eval {
        $vm->PowerOnVM;

        Util::trace( 0,
            "\n Virtual machine " . $vm->name . "has been started \n" );
    };
    }

    sub vmachineOff {
    eval {
        $vm->PowerOffVM;

        Util::trace( 0,
            "\n Virtual machine " . $vm->name . "has been shutdown \n" );
    };
    }

    sub vmachineShutdown {
    eval {
        $vm->ShutdownGuest;

Util::trace( 0,
    "\n Virtual machine " . $vm->name . "has begun to shutdown gracefully\n" );
    };
    }

    sub vmachineReset {
        $vm->ResetVM;

        Util::trace( 0,
            "\n Virtual machine" . $vm->name . "has been restarted \n" );
    }

    sub vm_reboot {

  Util::trace( 0,
      "\n Virtual machine" . $vm->name . "has begun rebooting gracefully \n" );
    }

    sub snap_revert {
        my $snapname = shift;
        my $count    = shift;
        if ( $count < 1 ) {

            print "$sn_name does not exist on host $vm_name\n";
            print '1';
        }
        my $snapshot = Vim::get_view( mo_ref => $snapname->snapshot );
        eval {
            $snapshot->RevertToSnapshot();

            Util::trace( 0,
                    "\nOperation :: Revert To Snapshot " . $sn_name
                  . " For Virtual Machine "
                  . $vm_name
                  . " completed \n" );
        vmachineOn( );
        };
        if ($@) {
            if ( ref($@) eq 'SoapFault' ) {
                if ( ref( $@->detail ) eq 'InvalidState' ) {
                        Util::trace(
                            0,
"\nOperation cannot be performed in the current state
                                 of the virtual machine"
                        );
                }
                elsif ( ref( $@->detail ) eq 'NotSupported' ) {
                        Util::trace( 0,
                            "\nHost product does not support snapshots." );
                }
                elsif ( ref( $@->detail ) eq 'InvalidPowerState' ) {
                        Util::trace(
                            0,
"\nOperation cannot be performed in the current power state
                                 of the virtual machine."
                        );
                }
                elsif ( ref( $@->detail ) eq 'InsufficientResourcesFault' ) {
                        Util::trace( 0,
                            "\nOperation would violate a resource usage policy."
                        );
                }
                elsif ( ref( $@->detail ) eq 'HostNotConnected' ) {
                        Util::trace( 0, "\nHost not connected." );
                }
                elsif ( ref( $@->detail ) eq 'NotFound' ) {
                        Util::trace( 0,
                            "\nVirtual machine does not have a current snapshot"
                        );
                }
                else {
                        Util::trace( 0, "\nFault: " . $@ . "\n\n" );
                }
            }
            else {
                    Util::trace( 0, "\nFault: " . $@ . "\n\n" );
            }
        }
    }

}

Util::disconnect();
1
