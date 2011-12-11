#!/usr/bin/perl
#

#Purpose of this script is to get the Licenses we have from our VMWare ESX Server..
#Type of License, How many used, How many available..
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
#Example output
#Cost per Unit:             cpuPackage
#Feature Name:            ESX Server Standard
#Feature Description:    Grants: count per CPU package
#Total Licenses:           314
#Total Available:           290



use strict;
use warnings;
use VMware::VIRuntime;
Opts::parse();
Opts::validate();
Util::connect();

my $content   = Vim::get_service_content();
my $licMgr    = Vim::get_view( mo_ref => $content->licenseManager );
my $lic_usage = $licMgr->QueryLicenseSourceAvailability;

foreach my $line (@$lic_usage) {
    print "Cost per Unit:\t\t" . $line->feature->costUnit . "\n";
    print "Feature Name:\t\t" . $line->feature->featureName . "\n";
    print "Feature Description:\t" . $line->feature->featureDescription . "\n";
    print "Total Licenses:\t\t" . $line->total . "\n";
    print "Total Available:\t" . $line->available . "\n\n";

}
Vim::logout();
