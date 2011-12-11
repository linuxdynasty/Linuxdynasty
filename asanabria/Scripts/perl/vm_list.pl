#!/usr/bin/perl

#This script will list snapshots  for you
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


use strict;
use warnings;
use VMware::VIRuntime;
Opts::parse();
Opts::validate();
Util::connect();
use Data::Dumper;


# Obtain all inventory objects of the specified type
my $e_vm = Vim::find_entity_views(view_type => 'VirtualMachine');
foreach my $views (sort(@$e_vm)) {
    my $vm_name = $views->name;
    print "Virtual Machine name = $vm_name\n\n";
    }
Util::disconnect();
