#!/usr/bin/perl

use strict;
use Getopt::Std;

#Zenoss/Nagios specific
use lib "/usr/local/pkg/zenoss/libexec";
my %ERRORS = (
    'OK'        => 0,
    'WARNING'   => 1,
    'CRITICAL'  => 2,
    'UNKNOWN'   => 3,
    'DEPENDENT' => 4
);

our ( $opt_H, $opt_h, $opt_T );
getopts('H:T:h');

#&help() if $opt_h;

if ( $opt_H =~ /\w+/ && $opt_T =~ /\w+/ ) {
    &HpsSub( $opt_H, $opt_T );
}
elsif ($opt_h) {
    &help();
}
else {
    &help();
}

sub HpsSub {
    my $hps     = "/usr/bin/telnet";
    my $port    = 4252;
    my $address = @_[0];
    my $type    = @_[1];
    my $hps_cmd = "$hps $address $port 2>/dev/null";
    my $hps_line;
    my @hps;

    open HPS, "$hps_cmd|" || die "Could not run $hps_cmd\n";
    while ( $hps_line = <HPS> ) {
        chomp($hps_line);
        if ( $hps_line =~ /(^$type)\s+\[(\d+\.\d+)\%?]/ ) {
            $hps[0] = $2;
            if ( $type =~ /avg/ ) {
                print "HPSOK:avg_5min=$hps[0]|avg_5min=$hps[0]\n";
            }
            elsif ( $type =~ /peak/ ) {
                print "HPSOK:avg_1min=$hps[0]|avg_1min=$hps[0]\n";
            }
            elsif ( $type =~ /cpuidle/ ) {
                print "HPSOK:cpu_idle=$hps[0]|cpu_idle=$hps[0]\n";
            }
            elsif ( $type =~ /cache/ ) {
                print "HPSOK:cache=$hps[0]|cache=$hps[0]\n";
            }

            exit $ERRORS{OK};
        }
    }
    close HPS;
}

sub print_usage {
    print
"Usage: $0 -H <host> -T <avg> 5min average or <peak> 1min average or <cpuidle> or <cache>\n";
}

sub help {
    print "\nHPS monitor for Zenoss/Nagios\n";
    print "GPL licence, (c)2007-2007 Allen Sanabria\n\n";
    print_usage();
    print <<EOT;
-h, -h
   print this help message
-H, -H <HOST>
   name or IP address of host to check
-T, -T <avg> or <peak> or <cache> or <cpuidle>
   avg equals to 5 min Average or peak which equals to 1 min Average or cpuidle or cache
EOT
}

