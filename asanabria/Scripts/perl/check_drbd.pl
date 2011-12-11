#!/usr/bin/perl -w
#
#
#Author Allen Sanabria
#Purpose monitor drbd using snmp
#Created 5:30AM of November 11th of 2006

use strict;

my @state;
my $drbd_state = "drbdadm state all";
my $drbd_sline;
my $i = 0;

open STATE, "$drbd_state|" || die "Could not run $drbd_state\n";
while ( $drbd_sline = <STATE> ) {
    chomp($drbd_sline);
    if (   $drbd_sline =~ /(Primary\/Secondary)/
        || $drbd_sline =~ /(Secondary\/Primary)/ )
    {
        $state[$i]{drbd0} = $1;
        $state[$i]{drbd1} = $1;
        $i++;
    }
}
close STATE;

if ( $state[0]{drbd0} =~ /Connected/ && $state[1]{drbd1} =~ /Connected/ ) {
    print "drbd0:$state[0]{drbd0} and dbrd1:$state[1]{drbd1}\n";
    exit 0;
}

elsif ( $state[0]{drbd0} =~ /Unconnected/ && $state[1]{drbd1} =~ /Unconnected/ )
{
    print "drbd0:$state[0]{drbd0} and dbrd1:$state[1]{drbd1}\n";
    exit 0;
}

elsif ($state[0]{drbd0} =~ /WFConnection/
    && $state[1]{drbd1} =~ /WFConnection/ )
{
    print "drbd0:$state[0]{drbd0} and dbrd1:$state[1]{drbd1}\n";
    exit 0;
}

