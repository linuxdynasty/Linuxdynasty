#!/usr/bin/perl
##############################################################################################
# BACKGROUND
# We needed a perl wrapper for the check_ping cmd in Nagios, that is able to
# ping the alternate interface. So if Nagios runs check ping cc24-0.web.dev.ccops.us it will
# then ping cc24-0.db.dev.ccops.us or if Nagios checks 10.40.0.21, than Nagios will check
# 10.41.0.21..... Do you understand the words that are coming out of my keyboard?????
# Created and Maintained by the one and only Allen Sanabria AKA LinuxDynasty
# test
##############################################################################################

use strict;
use Net::DNS;

use constant OK       => 0;
use constant WARNING  => 1;
use constant CRITICAL => 2;
use constant UNKNOWN  => 3;

my $libexec_dir = "/opt/zenoss/libexec";    # This one is obvious
my $args = join( ' ', @ARGV )
  ; # Here we go... so in this line I take the comandline argument from @ARGV and give it to $args for alter use :P
my %othernet = (    # declaring a hash for later use..
    30 => "31",
    50 => "51",
    51 => "50",
    31 => "30",
    40 => "41",
    41 => "40",
    20 => "21",
    21 => "20",
);

my $resolved
  ; #Declaring the variable resolve here so that if we use this wrapper with a host name, this will get the ip address..

# using Net::DNS to translate dns/host names
my $res   = new Net::DNS::Resolver;
my $query = $res->search("$args");
if ($query) {
    foreach my $rr ( $query->answer ) {
        next unless $rr->type eq "A";
        $resolved = $rr->address;
    }
}

# Here all thats happening is to check if we are giving a ip address or host address..... this perl wrapper is flexable

if ($resolved) {
    &RESOLVED;
}
elsif ($args) {
    &UNRESOLVED;
}

sub RESOLVE {

    my @addr   = split( /\./, $resolved );
    my $host   = $addr[3];
    my $net    = $addr[1];
    my $base   = $addr[0];
    my $newnet = $othernet{$net};
    my $Ping =
`$libexec_dir/check_ping $base.$newnet.$addr[2].$host -w 200,15% -c 600,150% -p5`;
    print "$Ping";
    if ( $Ping =~ /OK/ ) {
        exit OK;
    }
    elsif ( $Ping =~ /WARNING/ ) {
        exit WARNING;
    }
    elsif ( $Ping =~ /CRITICAL/ ) {
        exit CRITICAL;
    }

}

sub UNRESOLVED {
    my @addr   = split( /\./, $args );
    my $host   = $addr[3];
    my $net    = $addr[1];
    my $base   = $addr[0];
    my $newnet = $othernet{$net};
    my $Ping =
`$libexec_dir/check_ping $base.$newnet.$addr[2].$host -w 200,15% -c 600,150% -p5`;
    print "$Ping";
    if ( $Ping =~ /OK/ ) {
        exit OK;
    }
    elsif ( $Ping =~ /WARNING/ ) {
        exit WARNING;
    }
    elsif ( $Ping =~ /CRITICAL/ ) {
        exit CRITICAL;
    }

}
