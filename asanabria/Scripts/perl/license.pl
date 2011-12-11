#!/usr/bin/perl
#Created by Allen Sanabria
use strict;
use Data::Dumper;
use warnings;
use VMware::VIRuntime;
Opts::parse();
Opts::validate();
Util::connect();

my $content = Vim::get_service_content();
my $licMgr = Vim::get_view(mo_ref => $content->licenseManager);
my $lic_usage = $licMgr->QueryLicenseSourceAvailability;
my (@costUnit, @featureName, @featureDescription, @available, @total);
my $i = 0;

foreach my $line (Dumper(@$lic_usage)){
  if ($line =~ /\'(costUnit)\'\s+\=\>\s+\'(\w+.*)\'/g){
    $costUnit[$i] = "$1 = $2";
    print "$costUnit[$i]\n";
  }
  if ($line =~ /\'(featureName)\'\s+\=\>\s+\'(\w+.*)\'/g){
    $featureName[$i] = "$1 = $2";
    print "$featureName[$i]\n";
  }
  if ($line =~ /\'(featureDescription)\'\s+\=\>\s+\'\w+\:\s+(\w+.*)\'/g){
    $featureDescription[$i] = "$1 = $2";
    print "$featureDescription[$i]\n";
  }
  if ($line =~ /\'(total)\'\s+\=\>\s+\'(\d+)\'/g){
    $total[$i] = "$1 = $2";
    print "$total[$i]\n";
  }
  if ($line =~ /\'(available)\'\s+\=\>\s+\'(\d+)\'/g){
    $available[$i] = "$1 = $2";
    print "$available[$i]\n\n";
  }
  #print "$costUnit[$i]\n$featureName[$i]";
  $i +=1;
}
Vim::logout();
