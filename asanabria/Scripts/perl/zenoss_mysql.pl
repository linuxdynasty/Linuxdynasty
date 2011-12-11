#!/usr/bin/perl
#####################################################################################
#Allen Sanabria aka LinuxDynasty aka PrNino69				            #
#This script was created to keep our IDB (mysql) database in sync with ZenOSS       #
#In this Script we sync up the console info, power info, switch info, rack info,    #
#hardware info, and Production state. Also will soon be keeping the project/cluster #
#I create 5 subroutines, 1-DbServerQuery, 2-GetRedirectUrl, 3-EditDevice, 	    #
#4-SnmpInfo, and 5-usage							    #
#info in sync with zenoss.							    #
#Created on March 27 2007							    #
#Last modified April 03 2007							    #
#####################################################################################

use DBI;
use strict;
use Frontier::Client;
use LWP::UserAgent;
use Getopt::Std;

our ( $opt_l, $opt_h, $opt_v );
getopts('l:hv');
&usage() if $opt_h;
my $dsn       = "DBI:mysql:idb:mysql.be.sportsline.com";
my $user_name = "readonly";
my $password  = "";
my $sth;
my $status = 0;
my $device;
my $user = "zenoss";
my $pass = 'z3n055';
my $util = '@util2000.bc.cbsig.net';
my $base = "http://$user:$pass$util:8080";

#print "l=$opt_l\nh=$opt_h\nv=$opt_v\n";

if ( $opt_l =~ /\w+/ ) {
    &DbServerQuery();
}
else {
    &usage();
}

#Main part of my script, connect to IDB, run my query, save it into a array, then make prper subroutine calls.
sub DbServerQuery {
    my $dbh =
      DBI->connect( $dsn, $user_name, $password,
        { RaiseError => 1, PrintError => 0, AutoCommit => 1 } );
    if ( $status == 0 ) {
        my $SrvQuery =
"select host,rack,switch,hardware,console,power,buildprof,conftag,project from servers a, projects b where (a.sn= b.sn and a.lan like '%$opt_l%' AND b.project != 'webhost') order by host"
          or die "Can't connect to mysql: $!\n";
        $sth    = $dbh->prepare($SrvQuery);
        $device = $sth->execute();
        while ( my @data = $sth->fetchrow_array() ) {
            my $deviceName = "$data[0]";
            my $server_url =
              "$base/zport/dmd/Devices/searchDevices?query=$deviceName";
            my $new_srv = &GetRedirectUrl($server_url);
            if ( $new_srv =~ /^\// ) {
                print "\n$new_srv\n";
            }
            else {
                print "\n$deviceName skipping, not in zenoss\n";
            }
            next if $new_srv !~ /^\//;
            my $srv_url_final = join( '', "$base", $new_srv );
            &EditDevice( $srv_url_final, @data );

        }
    }

    $sth->finish();
}

# This subroutine does what it is named as, It gets the redirect Url from the searchDevice query
sub GetRedirectUrl {
    my $redirect_url = shift @_;
    my $ua           = LWP::UserAgent->new;
    my $response     = $ua->get($redirect_url);
    my $srv_url      = $response->{'_previous'}->{'_headers'}->{'location'};
    return $srv_url;
}

# This subroutine does what it is named as, It edits the devices that are already in zenoss
sub EditDevice {

    #This is how the calls are labled in Devices.py
    my %Zenoss = (
        "deviceName"         => "",
        "devicePath"         => "",
        "tag"                => "",
        "serialNumber"       => "",
        "zSnmpCommunity"     => "monitor",
        "zSnmpPort"          => "161",
        "zSnmpVer"           => "v1",
        "rackSlot"           => "0",
        "productionState"    => "1000",
        "comments"           => "",
        "hwManufacturer"     => "",
        "hwProductName"      => "",
        "osManufacturer"     => "",
        "osProductName"      => "",
        "locationPath"       => "",
        "groupPaths"         => "",
        "systemPaths"        => "",
        "statusMonitors"     => "",
        "performanceMonitor" => "",
        "discoverProto"      => "snmp",
        "priority"           => "3"
    );
    my $groups_url = "$base/zport/dmd/Groups/getOrganizerNames";
    my $ua         = LWP::UserAgent->new;
    my $response1  = $ua->get($groups_url);
    my $srv1       = $response1->{'_content'};
    my @groups     = split( /\[|\'|\,|\]/, $srv1 );

    my @params = @_;
    my $url    = $params[0];
    my @Snmp   = &SnmpInfo($url);
    my $server =
      Frontier::Client->new( url => $url, 'encoding' => 'ISO-8859-1' );
    if ( $Snmp[0] =~ /\w+/ && $Snmp[1] =~ /\w+/ ) {
        $Zenoss{zSnmpCommunity} = $Snmp[0];
        $Zenoss{zSnmpVer}       = $Snmp[1];
    }
    $Zenoss{deviceName} = "$params[1]";
    $Zenoss{tag}        = "$params[8]";
    $Zenoss{comments}   = join( "\n",
        "Switch $params[3]",
        "Hardware $params[4]",
        "Console $params[5]",
        "Power $params[6]",
        "Build Profile $params[7]" );
    if ( $params[9] =~ /\w+/ ) {
        $Zenoss{systemPaths} = "/" . "$params[9]";
    }
    else {
        $Zenoss{systemPaths} = "/";
    }
    foreach my $group (@groups) {
        if ( $group =~ /$Zenoss{systemPaths}/ ) {
            $Zenoss{groupPaths} = $group;
        }
        else { next; }
    }

    print
"\n$Zenoss{deviceName}\n$Zenoss{tag}\n$Zenoss{comments}\n$Zenoss{systemPaths}\n$Zenoss{zSnmpCommunity}\n$Zenoss{zSnmpVer}\n"
      if ($opt_v);
    my $result = $server->call(
        'manage_editDevice',    $Zenoss{tag},
        $Zenoss{serialNumber},  $Zenoss{zSnmpCommunity},
        $Zenoss{zSnmpPort},     $Zenoss{zSnmpVer},
        $Zenoss{rackSlot},      $Zenoss{productionState},
        $Zenoss{comments},      $Zenoss{hwManufacturer},
        $Zenoss{hwProductName}, $Zenoss{osManufacturer},
        $Zenoss{osProductName}, $Zenoss{locationPath},
        $Zenoss{groupPaths},    $Zenoss{systemPaths}
    );

}

sub SnmpInfo {
    my $url           = shift @_;
    my $new_url       = $url . "/getSnmpOidTargets";
    my $ua1           = LWP::UserAgent->new;
    my $snmp_response = $ua1->get($new_url);
    my $snmp_url      = $snmp_response->{'_content'};
    my @output        = split( /\,|\\|'|\(|\)/, $snmp_url );
    my @final         = ( "$output[14]", "$output[17]" );
    return @final;
}

sub usage() {
    print "This program does...\n";
    print "usage: $0 [-hl]\n";
    print "-h        : this (help) message\n";
    print "-l        : which lan to match in the idb query\n";
    print "-v        : A little verbosity\n";
    print "example: $0 -h -l -v\n";
    exit;
}

