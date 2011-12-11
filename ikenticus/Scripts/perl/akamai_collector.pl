#!/usr/bin/perl 
#
# Akamai Traffic Acquisition and Graphing
# Copyright (c) 2008.  All Rights Reserved.
# Author: ikenticus
#
# Adapted several of Akamai's sample code to create a unified
# script that will sort and dump all data into rrdtool and
# then created the PNG graphs and HTML code
#
# Complete EdgeControl Web Services Developers guide can be found at:
# https://control.akamai.com/portal/content/webservices/docs/awsv2.jsp
#
# You will need the RRDs module in addition to any Akamai perl requirements
# Make sure to check your perl modules using the Akamai mod-check.pl
#
# IMPORTANT NOTES:
#  * Database/graphs are organized by the CAPITALIZED PREFIX of each cpcode name
#  * Create a username/password to an read-only Accounting/Reporting user
#  * Create all output directories that you need beforehand as this script does NOT
#(safety measure...feel free to change that if you want, not that complex)
#
#Note that the main HTML output from the perl script is akamai.inc, which I include into my generic.php file:
#<table border=0 cellspacing=0 cellpadding=5>
#<?php
#  include(
#    preg_replace(
#        '/^.*\/([^\/]+)\.php$/',
#        '
#
#.inc',
#        $_SERVER['PHP_SELF']
#    )
#  );
#?>
#</table>
#
#and then I symlink it as:
#
#ln -s generic.php akamai.php
#
#
#The reason behind this is that I may want to include multiple *.inc files into my main page,
#but the generic.php file lets me view just that one include (all other individual X.inc files
#have a corresponding symlink from X.php to that generic.php file as well).
#The akarrd.pl is as follows:

use strict;
use vars qw/ %opt %bw %svc %rng @clr /;
use RRDs;
use Date::Manip;
use Data::Dumper;
use POSIX qw(strftime);
use Getopt::Std;
use HttpContentDeliveryReportService;
use HttpContentDeliveryReportService_Constants;
use StreamingReportService;
use StreamingReportService_Constants;

my $now = strftime("%b %d %H\\:%M", localtime(time));
my $tzd = strftime("%s", gmtime(time)) - strftime("%s", localtime(time));

$svc{'vod' }{'xsd'} = 'StreamingReportService';
$svc{'vod' }{'get'} = 'getVODStreamTrafficForCPCode';
$svc{'live'}{'xsd'} = 'StreamingReportService';
$svc{'live'}{'get'} = 'getLiveStreamTrafficForCPCode';
$svc{'http'}{'xsd'} = 'HttpContentDeliveryReportService';
$svc{'http'}{'get'} = 'getTrafficSummaryForCPCode';

# default range: start=-1d, x-grid=autoconfigure
$rng{'1_Daily'  } = '--x-grid=MINUTE:60:HOUR:1:HOUR:2:0:%k';
$rng{'2_Weekly' } = '--start=-1w';
$rng{'3_Monthly'} = '--start=-1m';
$rng{'4_Yearly' } = '--start=-1y';


#------------------
# Argument Checking
#------------------

my $opts = 'hdvo:s:u:p:';
getopts( "$opts", \%opt ) or help();
help() if $opt{h};


#--------------------------
# Set IMPORTANT info here
#--------------------------
my $user	= $opt{u} || 'LOGIN';
my $pass	= $opt{p} || 'PASSWD';
my $output	= $opt{o} || 'DATADIR';
my $outdb	= $output . '/db';
my $outpng	= $output . '/png';
my $outhtml	= $output . '/html';
my $start	= $opt{s} || 60;


#----------------------
# Permutation of colors
#----------------------

# Unfortunately, RRD doesn not have random auto-colors
sub permute {
  my $last = pop @_;
  return map [$_], @$last if(!@_);
  return map {
    my $left = $_;
    map [@$left, $_], @$last
  } permute(@_);
}
my @hex = ('00','33','66','99','CC','FF'); 
my @clr = permute(\@hex,\@hex,\@hex);


#--------------------
# Setup SOAP Services
#--------------------

# setup the HTTP Basic Auth parameters
sub SOAP::Transport::HTTP::Client::get_basic_credentials {
        return $user => $pass;
}


# initialize the service stub
my $service;


#------------------
# Retrieve cp codes
#------------------

sub acquire_bandwidth {
    my $type = shift;
    my $service = shift;
    my $getTraffic = shift;
    my $xsdService = shift;
    my %bandw = ();

    # !! Import Akamai Customer Care troubleshooting tip !!
    # !! uncomment following two lines to enable debugging !!
    #
    # $service->readable(1);
    # $service->on_debug(sub {print @_, "\n";});
                                                                                    
    # catch faults if any
    #$service->on_fault(sub {my ($soap, $res) = @_; 
    #                        print "\nFault ... \n", $res->faultstring,"\n"; });
                            #die "\nFault ... \n", $res->faultstring,"\n"; });
    
    # SOAP::Lite needs us to setup the XML schemas explicitly.
    $service->xmlschema("http://www.w3.org/2001/XMLSchema");

    $service->serializer
        ->namespaces
        ->{'https://control.akamai.com/'.$xsdService.'.xsd'} = 'akasiteDeldt';

    my $cpcodes = $service->getCPCodes(); # WS Call

    my %data;
    for (@$cpcodes) {
        #print "Cpcode Index# $_->{cpcode} with Name: \"$_->{description}\" ",
        #  "and Service: \"$_->{service}\"\n";
        my $div = $_->{description};
           $div =~ s/^([A-Z]+).*/

/;
        push @{$data{$div}}, $_->{cpcode} if (!inarray(@{$data{$div}},$_->{cpcode}));
    }
    print "For $type, there are " . scalar @{$cpcodes} . " cpcodes in "
      . scalar( keys %data ) . " divisions\n";

    my $serial1 = strftime("%Y-%m-%dT%H:%M:%S.0", localtime(time - 60*$start));
    my $serial2 = strftime("%Y-%m-%dT%H:%M:%S.0", localtime(time));
    my $tz = 'GMT';	#strftime("%Z", localtime(time));

    my @columns;
    my @cpCodes;
    my $returnResult; 

    for my $key (sort keys %data) {
        @cpCodes = $data{$key};
        #print Dumper(@cpCodes);
        #print "$serial1 - $serial2 ($tz)\n";
	#print 'DEBUG $returnResult = $service->' . $getTraffic . '(@cpCodes, $serial1, $serial2, $tz, \@columns);' . "\n";
	eval '$returnResult = $service->' . $getTraffic . '(@cpCodes, $serial1, $serial2, $tz, \@columns);';
        print "--- $key ---\n" . Dumper($returnResult) . "\n" if ($opt{d});
        $returnResult = "\n0,0,0,0,0,0,0,0,0,0" if (!$returnResult || $returnResult eq '1');
	
	my $stamp;
        my @fields;
        my @results = split(/\n/, $returnResult);
        for (my $i=scalar(@results); $i>=0; $i--) {
            if ($results[$i] && $results[$i] =~ /^".+,\d+/) {
                my $epoch = 0;
                print "   $key: $results[$i]\n" if $opt{v};
                @fields = split(/,/, $results[$i]);
		$stamp = $fields[0];
		$stamp =~ s/"//g;
                $epoch = $tzd + UnixDate(ParseDate($stamp),'%s') if ($stamp);
			# add time zone difference since Akamai reports in GMT
                $bandw{$key}{$epoch}{'bits'} = $fields[1] if ($epoch);
            }
        }
        #print Dumper(@results);
    }
    return %bandw;
}


#------------------
# Update functions
#------------------

sub updateRRD {
  if (-d $outdb) {
    for my $b (sort keys %bw) {
      my $rrd = "$outdb/$b-bw.rrd";
      print "Updating RRD file: $rrd\n";
      if (! -e $rrd) {
        print "$rrd does not exist, creating...";
        RRDs::create ($rrd, "--start","12am 01/01/06", "--step",300,
  	"DS:http:GAUGE:600:0:1250000000",
  	"DS:live:GAUGE:600:0:1250000000",
  	"DS:vod:GAUGE:600:0:1250000000",
  	"RRA:AVERAGE:0.5:1:105120",
  	"RRA:AVERAGE:0.5:6:336",
  	"RRA:AVERAGE:0.5:24:360",
  	"RRA:AVERAGE:0.5:288:365",
  	"RRA:MAX:0.5:1:1",
  	"RRA:MAX:0.5:6:1",
  	"RRA:MAX:0.5:24:1",
  	"RRA:MAX:0.5:288:1",
  	);
        print "done\n";
      }
  
      # Insert new data and update the old ones
      for my $d (sort keys %{$bw{$b}}) {
        print "  ($d) http:vod:live -> " . $bw{$b}{$d}{'http'} . 
  	':' . $bw{$b}{$d}{'vod'} . ':' . $bw{$b}{$d}{'live'} . "\n";
        # Updating each service separately does not work
        # maybe it will get fixed in later RRDs versions
        RRDs::update ($rrd, '--template=http:vod:live', 
  	$d . ':' . $bw{$b}{$d}{'http'} .
  	':' . $bw{$b}{$d}{'vod'} . ':' . $bw{$b}{$d}{'live'});
      }
    }
  } else {
    print "RRD dir does not exist, no RRD files will be written!\n";
  }
}

  
sub updatePNG {
  if (-d $outpng) {
    for my $b (sort keys %bw) {
      my $rrd = "$outdb/$b-bw.rrd";
      print "Updating PNG file for $b: ";
      for my $d (sort keys %rng) {
        my ($num, $title) = split(/_/, $d);
        my $unit = lc($title);
        my $png = "$outpng/$b-bw-$unit.png";
        print "$unit ";
        my $setting = $rng{$d};
        my @graph;
        push (@graph, $png, $setting);
      	push (@graph, "--vertical-label=Bits per second");
      	push (@graph, "--title=Akamai: $b ($title)", "--color=MGRID#AAAAAA");
        my $sc = 0;
        for my $s (sort keys %svc) {
          my $su = sprintf "%-6s", uc($s);
          my $ss = uc(substr($s, 0, 1));
          my $sq = $sc / 3;
          my $sr = $sc % 3;
          my $sh = sprintf "%s", join('',@{$clr[(180/6**$sr+$sq)]});
          #my $sh = sprintf "%s", join('',@{$clr[(5**2*$sr+5+$sq)]});
          # Graphing the various services for each division
      	  push (@graph, "DEF:$s=$rrd:$s:AVERAGE");
      	  push (@graph, "CDEF:line$ss=$s,1000,*,1000,*");
      	  push (@graph, "LINE:line$ss#" . $sh . ":$su");
      	  push (@graph, "GPRINT:line$ss:MAX:  Max\\: %7.2lf %sb/s");
      	  push (@graph, "GPRINT:line$ss:AVERAGE:  Avg\\: %7.2lf %sb/s");
      	  push (@graph, "GPRINT:line$ss:LAST:  Cur\\: %7.2lf %sb/s\\n");
          $sc++;
        }
      	push (@graph, "COMMENT:Last Modified\\: $now\\r");
        #print Dumper(@graph) . "\n";
        RRDs::graph @graph;
        my $ERROR = RRDs::error;
        print "RRDs::graph ERROR: $ERROR\n" if $ERROR ;
      }
      print "\n";
    }
  } else {
    print "PNG dir does not exist, no PNG files will be written!\n";
  }
}

  
sub updateTotal {
  if (-d $outpng) {
    for my $d (sort keys %rng) {
      my @graph;
      my ($num, $title) = split(/_/, $d);
      print "Updating Total $title PNG file\n";
      my $unit = lc($title);
      my $png = "$outpng/Total-bw-$unit.png";
      my $setting = $rng{$d};
      push (@graph, $png, $setting);
      push (@graph, "--vertical-label=Bits per second");
      push (@graph, "--title=Akamai: Total ($title)", "--color=MGRID#AAAAAA");
      my $sc = 0;
      for my $s (sort keys %svc) {
        my @area;
        my $ss = uc(substr($s, 0, 1));
        push (@area, "CDEF:area$ss=");
        my $bc = 0;
        for my $b (sort keys %bw) {
          my $rrd = "$outdb/$b-bw.rrd";
      	  push (@graph, "DEF:$s$b=$rrd:$s:AVERAGE");
      	  #push (@area, "$s$b") if (!$bc);
          #push (@area, ",$s$b,+") if ($bc);
      	  push (@area, "$s$b,UN,0,$s$b,IF") if (!$bc);
          push (@area, ",$s$b,UN,0,$s$b,IF,+") if ($bc);
          $bc++;
        }
        push (@area, ",1000,*,1000,*");
        push (@graph, join('',@area));
        my $su = sprintf "%-6s", uc($s);
        my $sq = $sc / 3;
        my $sr = $sc % 3;
        my $sh = sprintf "%s", join('',@{$clr[(180/6**$sr+$sq)]});
        #my $sh = sprintf "%s", join('',@{$clr[(5**2*$sr+5+$sq)]});
        my $stack = ($sc) ? ':STACK' : '';
      	push (@graph, "AREA:area$ss#" . $sh . ":$su" . $stack);
      	push (@graph, "GPRINT:area$ss:MAX:  Max\\: %7.2lf %sb/s");
      	push (@graph, "GPRINT:area$ss:AVERAGE:  Avg\\: %7.2lf %sb/s");
      	push (@graph, "GPRINT:area$ss:LAST:  Cur\\: %7.2lf %sb/s\\n");
        $sc++;
      }
      push (@graph, "COMMENT:Last Modified\\: $now\\r");
      #print Dumper(@graph) . "\n";
      RRDs::graph @graph;
      my $ERROR = RRDs::error;
      print "RRDs::graph ERROR: $ERROR\n" if $ERROR ;
    }
  } else {
    print "PNG dir does not exist, no PNG files will be written!\n";
  }
}

  
sub updateHTML {
  if (-d $outhtml) {
    my $fc = 1;
    my @full;
    push (@full, "<tr>\n");
    my @tmp = sort keys %bw;
    unshift(@tmp, 'Total');
    for my $b (@tmp) {
      my $html = "$outhtml/$b-bw.html";
      my @grid;
      push (@grid, "<html>\n<head>\n");
      push (@grid, "<title>".$b."</title>\n");
      push (@grid, "<meta http-equiv=Refresh content=60>\n");
      push (@grid, "<meta http-equiv=Cache-Control content=no-cache>\n");
      push (@grid, "</head>\n<body>\n<h1>".$b."</h1>\n\n");
      for my $d (sort keys %rng) {
        my ($num, $title) = split(/_/, $d);
        my $unit = lc($title);
        #push (@grid, "<hr>\n<b>$title Graph</b><br>\n<img src=../png/$b-bw-$unit.png>\n\n");
        push (@grid, "<img src=../png/$b-bw-$unit.png><br>\n");
      }
      push (@grid, "</body>\n</html>\n");
      if (! -e $html) {
        if(open(O,">$html")) {
          print O @grid;
          close(O);
        } else {
          die "Could not write to $html: $!\n";
        }
      } else {
        print "HTML already exists, skipping $html\n";
      }
      push (@full, "  <td><a href=../html/$b-bw.html><img border=0\n");
      push (@full, "\tsrc=../png/$b-bw-daily.png></a></td>\n");
      $fc++;
      if ($fc > 1) {
        push(@full, "</tr><tr>\n");
        $fc = 0;
      }
    }
    push (@full, "</tr>\n");
    if(open(O,">$outhtml/akamai.inc")) {
      print O @full;
      close(O);
    } else {
      die "Could not write to $outhtml/akamai.inc: $!\n";
    }
  } else {
    print "HTML dir does not exist, no HTML files will be written!\n";
  }
}



#------------------
# MAIN
#------------------

print "=====  Starting at " . strftime("%D %r", localtime(time)) . "  =====\n";

my %t;
my ($s, $b, $d);
for $s (sort keys %svc) {
  $service = eval 'new ' . $svc{$s}{'xsd'} . ';';
  #print "$s acquire_bandwidth($s,$service,$svc{$s}{'get'},$svc{$s}{'xsd'});\n";
  %t = acquire_bandwidth($s,$service,$svc{$s}{'get'},$svc{$s}{'xsd'});
  for $b (sort keys %t) {
    for $d (sort keys %{$t{$b}}) {
      $bw{$b}{$d}{$s} = $t{$b}{$d}{'bits'}; 
    }
  }
}

# zero out the missing values
for $s (sort keys %svc) {
  for $b (sort keys %bw) {
    for $d (sort keys %{$bw{$b}}) {
      $bw{$b}{$d}{$s} = 0 if (!$bw{$b}{$d}{$s});
    }
  }
  #print "\n";
}
print "\n----- DEBUG -----\n" . Dumper(%bw) .
	"\n----- DEBUG -----\n" if $opt{d};

updateRRD();
updatePNG();
updateHTML();
updateTotal();

print "=====  Finished at " . strftime("%D %r", localtime(time)) . "  =====\n";


        
#------------
# Subroutines
#------------

sub help {
    exec("perldoc $0");
}

sub inarray {
      if (ref($_[0]) eq 'ARRAY') { return "$_[0]" =~ m/$_[1]/; }
}

__END__

#--------------
# Documentation
#--------------

=cut

=head1 NAME

B<akarrd.pl> - Retrieve http and streaming reports bandwidth data via WebServices

=head1 SYNOPSIS

S<usage: B<akarrd.pl> >

=head1 DESCRIPTION

Akamai Web Services. 
Retrieve the http and video traffic

=head1 OPTIONS

Command line arguments include:

	-h	help
	-d	debug
	-v	verbose
	-u user	login for access
	-p pass	password for access
	-o dir	output directory
	-s hr	start Akamai collection hours ago (default: 1 hr)


=head1 AUTHOR

ikenticus

=cut<table border=0 cellspacing=0 cellpadding=5>
<?php
  include(
    preg_replace(
        '/^.*\/([^\/]+)\.php$/',
        '

.inc',
        $_SERVER['PHP_SELF']
    )
  );
?>
</table>



and then I symlink it as:


ln -s generic.php akamai.php



The reason behind this is that I may want to include multiple *.inc files into my main page,

but the generic.php file lets me view just that one include (all other individual X.inc files

have a corresponding symlink from X.php to that generic.php file as well).


The akarrd.pl is as follows:


#!/usr/bin/perl 
#
# Akamai Traffic Acquisition and Graphing
# Copyright (c) 2008.  All Rights Reserved.
# Author: ikenticus
#
# Adapted several of Akamai's sample code to create a unified
# script that will sort and dump all data into rrdtool and
# then created the PNG graphs and HTML code
#
# Complete EdgeControl Web Services Developers guide can be found at:
# https://control.akamai.com/portal/content/webservices/docs/awsv2.jsp
#
# You will need the RRDs module in addition to any Akamai perl requirements
# Make sure to check your perl modules using the Akamai mod-check.pl
#
# IMPORTANT NOTES:
#  * Database/graphs are organized by the CAPITALIZED PREFIX of each cpcode name
#  * Create a username/password to an read-only Accounting/Reporting user
#  * Create all output directories that you need beforehand as this script does NOT
#	(safety measure...feel free to change that if you want, not that complex)
#

use strict;
use vars qw/ %opt %bw %svc %rng @clr /;
use RRDs;
use Date::Manip;
use Data::Dumper;
use POSIX qw(strftime);
use Getopt::Std;
use HttpContentDeliveryReportService;
use HttpContentDeliveryReportService_Constants;
use StreamingReportService;
use StreamingReportService_Constants;

my $now = strftime("%b %d %H\\:%M", localtime(time));
my $tzd = strftime("%s", gmtime(time)) - strftime("%s", localtime(time));

$svc{'vod' }{'xsd'} = 'StreamingReportService';
$svc{'vod' }{'get'} = 'getVODStreamTrafficForCPCode';
$svc{'live'}{'xsd'} = 'StreamingReportService';
$svc{'live'}{'get'} = 'getLiveStreamTrafficForCPCode';
$svc{'http'}{'xsd'} = 'HttpContentDeliveryReportService';
$svc{'http'}{'get'} = 'getTrafficSummaryForCPCode';

# default range: start=-1d, x-grid=autoconfigure
$rng{'1_Daily'  } = '--x-grid=MINUTE:60:HOUR:1:HOUR:2:0:%k';
$rng{'2_Weekly' } = '--start=-1w';
$rng{'3_Monthly'} = '--start=-1m';
$rng{'4_Yearly' } = '--start=-1y';


#------------------
# Argument Checking
#------------------

my $opts = 'hdvo:s:u:p:';
getopts( "$opts", \%opt ) or help();
help() if $opt{h};


#--------------------------
# Set IMPORTANT info here
#--------------------------
my $user	= $opt{u} || 'LOGIN';
my $pass	= $opt{p} || 'PASSWD';
my $output	= $opt{o} || 'DATADIR';
my $outdb	= $output . '/db';
my $outpng	= $output . '/png';
my $outhtml	= $output . '/html';
my $start	= $opt{s} || 60;


#----------------------
# Permutation of colors
#----------------------

# Unfortunately, RRD doesn not have random auto-colors
sub permute {
  my $last = pop @_;
  return map [$_], @$last if(!@_);
  return map {
    my $left = $_;
    map [@$left, $_], @$last
  } permute(@_);
}
my @hex = ('00','33','66','99','CC','FF'); 
my @clr = permute(\@hex,\@hex,\@hex);


#--------------------
# Setup SOAP Services
#--------------------

# setup the HTTP Basic Auth parameters
sub SOAP::Transport::HTTP::Client::get_basic_credentials {
        return $user => $pass;
}


# initialize the service stub
my $service;


#------------------
# Retrieve cp codes
#------------------

sub acquire_bandwidth {
    my $type = shift;
    my $service = shift;
    my $getTraffic = shift;
    my $xsdService = shift;
    my %bandw = ();

    # !! Import Akamai Customer Care troubleshooting tip !!
    # !! uncomment following two lines to enable debugging !!
    #
    # $service->readable(1);
    # $service->on_debug(sub {print @_, "\n";});
                                                                                    
    # catch faults if any
    #$service->on_fault(sub {my ($soap, $res) = @_; 
    #                        print "\nFault ... \n", $res->faultstring,"\n"; });
                            #die "\nFault ... \n", $res->faultstring,"\n"; });
    
    # SOAP::Lite needs us to setup the XML schemas explicitly.
    $service->xmlschema("http://www.w3.org/2001/XMLSchema");

    $service->serializer
        ->namespaces
        ->{'https://control.akamai.com/'.$xsdService.'.xsd'} = 'akasiteDeldt';

    my $cpcodes = $service->getCPCodes(); # WS Call

    my %data;
    for (@$cpcodes) {
        #print "Cpcode Index# $_->{cpcode} with Name: \"$_->{description}\" ",
        #  "and Service: \"$_->{service}\"\n";
        my $div = $_->{description};
           $div =~ s/^([A-Z]+).*/

/;
        push @{$data{$div}}, $_->{cpcode} if (!inarray(@{$data{$div}},$_->{cpcode}));
    }
    print "For $type, there are " . scalar @{$cpcodes} . " cpcodes in "
      . scalar( keys %data ) . " divisions\n";

    my $serial1 = strftime("%Y-%m-%dT%H:%M:%S.0", localtime(time - 60*$start));
    my $serial2 = strftime("%Y-%m-%dT%H:%M:%S.0", localtime(time));
    my $tz = 'GMT';	#strftime("%Z", localtime(time));

    my @columns;
    my @cpCodes;
    my $returnResult; 

    for my $key (sort keys %data) {
        @cpCodes = $data{$key};
        #print Dumper(@cpCodes);
        #print "$serial1 - $serial2 ($tz)\n";
	#print 'DEBUG $returnResult = $service->' . $getTraffic . '(@cpCodes, $serial1, $serial2, $tz, \@columns);' . "\n";
	eval '$returnResult = $service->' . $getTraffic . '(@cpCodes, $serial1, $serial2, $tz, \@columns);';
        print "--- $key ---\n" . Dumper($returnResult) . "\n" if ($opt{d});
        $returnResult = "\n0,0,0,0,0,0,0,0,0,0" if (!$returnResult || $returnResult eq '1');
	
	my $stamp;
        my @fields;
        my @results = split(/\n/, $returnResult);
        for (my $i=scalar(@results); $i>=0; $i--) {
            if ($results[$i] && $results[$i] =~ /^".+,\d+/) {
                my $epoch = 0;
                print "   $key: $results[$i]\n" if $opt{v};
                @fields = split(/,/, $results[$i]);
		$stamp = $fields[0];
		$stamp =~ s/"//g;
                $epoch = $tzd + UnixDate(ParseDate($stamp),'%s') if ($stamp);
			# add time zone difference since Akamai reports in GMT
                $bandw{$key}{$epoch}{'bits'} = $fields[1] if ($epoch);
            }
        }
        #print Dumper(@results);
    }
    return %bandw;
}


#------------------
# Update functions
#------------------

sub updateRRD {
  if (-d $outdb) {
    for my $b (sort keys %bw) {
      my $rrd = "$outdb/$b-bw.rrd";
      print "Updating RRD file: $rrd\n";
      if (! -e $rrd) {
        print "$rrd does not exist, creating...";
        RRDs::create ($rrd, "--start","12am 01/01/06", "--step",300,
  	"DS:http:GAUGE:600:0:1250000000",
  	"DS:live:GAUGE:600:0:1250000000",
  	"DS:vod:GAUGE:600:0:1250000000",
  	"RRA:AVERAGE:0.5:1:105120",
  	"RRA:AVERAGE:0.5:6:336",
  	"RRA:AVERAGE:0.5:24:360",
  	"RRA:AVERAGE:0.5:288:365",
  	"RRA:MAX:0.5:1:1",
  	"RRA:MAX:0.5:6:1",
  	"RRA:MAX:0.5:24:1",
  	"RRA:MAX:0.5:288:1",
  	);
        print "done\n";
      }
  
      # Insert new data and update the old ones
      for my $d (sort keys %{$bw{$b}}) {
        print "  ($d) http:vod:live -> " . $bw{$b}{$d}{'http'} . 
  	':' . $bw{$b}{$d}{'vod'} . ':' . $bw{$b}{$d}{'live'} . "\n";
        # Updating each service separately does not work
        # maybe it will get fixed in later RRDs versions
        RRDs::update ($rrd, '--template=http:vod:live', 
  	$d . ':' . $bw{$b}{$d}{'http'} .
  	':' . $bw{$b}{$d}{'vod'} . ':' . $bw{$b}{$d}{'live'});
      }
    }
  } else {
    print "RRD dir does not exist, no RRD files will be written!\n";
  }
}

  
sub updatePNG {
  if (-d $outpng) {
    for my $b (sort keys %bw) {
      my $rrd = "$outdb/$b-bw.rrd";
      print "Updating PNG file for $b: ";
      for my $d (sort keys %rng) {
        my ($num, $title) = split(/_/, $d);
        my $unit = lc($title);
        my $png = "$outpng/$b-bw-$unit.png";
        print "$unit ";
        my $setting = $rng{$d};
        my @graph;
        push (@graph, $png, $setting);
      	push (@graph, "--vertical-label=Bits per second");
      	push (@graph, "--title=Akamai: $b ($title)", "--color=MGRID#AAAAAA");
        my $sc = 0;
        for my $s (sort keys %svc) {
          my $su = sprintf "%-6s", uc($s);
          my $ss = uc(substr($s, 0, 1));
          my $sq = $sc / 3;
          my $sr = $sc % 3;
          my $sh = sprintf "%s", join('',@{$clr[(180/6**$sr+$sq)]});
          #my $sh = sprintf "%s", join('',@{$clr[(5**2*$sr+5+$sq)]});
          # Graphing the various services for each division
      	  push (@graph, "DEF:$s=$rrd:$s:AVERAGE");
      	  push (@graph, "CDEF:line$ss=$s,1000,*,1000,*");
      	  push (@graph, "LINE:line$ss#" . $sh . ":$su");
      	  push (@graph, "GPRINT:line$ss:MAX:  Max\\: %7.2lf %sb/s");
      	  push (@graph, "GPRINT:line$ss:AVERAGE:  Avg\\: %7.2lf %sb/s");
      	  push (@graph, "GPRINT:line$ss:LAST:  Cur\\: %7.2lf %sb/s\\n");
          $sc++;
        }
      	push (@graph, "COMMENT:Last Modified\\: $now\\r");
        #print Dumper(@graph) . "\n";
        RRDs::graph @graph;
        my $ERROR = RRDs::error;
        print "RRDs::graph ERROR: $ERROR\n" if $ERROR ;
      }
      print "\n";
    }
  } else {
    print "PNG dir does not exist, no PNG files will be written!\n";
  }
}

  
sub updateTotal {
  if (-d $outpng) {
    for my $d (sort keys %rng) {
      my @graph;
      my ($num, $title) = split(/_/, $d);
      print "Updating Total $title PNG file\n";
      my $unit = lc($title);
      my $png = "$outpng/Total-bw-$unit.png";
      my $setting = $rng{$d};
      push (@graph, $png, $setting);
      push (@graph, "--vertical-label=Bits per second");
      push (@graph, "--title=Akamai: Total ($title)", "--color=MGRID#AAAAAA");
      my $sc = 0;
      for my $s (sort keys %svc) {
        my @area;
        my $ss = uc(substr($s, 0, 1));
        push (@area, "CDEF:area$ss=");
        my $bc = 0;
        for my $b (sort keys %bw) {
          my $rrd = "$outdb/$b-bw.rrd";
      	  push (@graph, "DEF:$s$b=$rrd:$s:AVERAGE");
      	  #push (@area, "$s$b") if (!$bc);
          #push (@area, ",$s$b,+") if ($bc);
      	  push (@area, "$s$b,UN,0,$s$b,IF") if (!$bc);
          push (@area, ",$s$b,UN,0,$s$b,IF,+") if ($bc);
          $bc++;
        }
        push (@area, ",1000,*,1000,*");
        push (@graph, join('',@area));
        my $su = sprintf "%-6s", uc($s);
        my $sq = $sc / 3;
        my $sr = $sc % 3;
        my $sh = sprintf "%s", join('',@{$clr[(180/6**$sr+$sq)]});
        #my $sh = sprintf "%s", join('',@{$clr[(5**2*$sr+5+$sq)]});
        my $stack = ($sc) ? ':STACK' : '';
      	push (@graph, "AREA:area$ss#" . $sh . ":$su" . $stack);
      	push (@graph, "GPRINT:area$ss:MAX:  Max\\: %7.2lf %sb/s");
      	push (@graph, "GPRINT:area$ss:AVERAGE:  Avg\\: %7.2lf %sb/s");
      	push (@graph, "GPRINT:area$ss:LAST:  Cur\\: %7.2lf %sb/s\\n");
        $sc++;
      }
      push (@graph, "COMMENT:Last Modified\\: $now\\r");
      #print Dumper(@graph) . "\n";
      RRDs::graph @graph;
      my $ERROR = RRDs::error;
      print "RRDs::graph ERROR: $ERROR\n" if $ERROR ;
    }
  } else {
    print "PNG dir does not exist, no PNG files will be written!\n";
  }
}

  
sub updateHTML {
  if (-d $outhtml) {
    my $fc = 1;
    my @full;
    push (@full, "<tr>\n");
    my @tmp = sort keys %bw;
    unshift(@tmp, 'Total');
    for my $b (@tmp) {
      my $html = "$outhtml/$b-bw.html";
      my @grid;
      push (@grid, "<html>\n<head>\n");
      push (@grid, "<title>".$b."</title>\n");
      push (@grid, "<meta http-equiv=Refresh content=60>\n");
      push (@grid, "<meta http-equiv=Cache-Control content=no-cache>\n");
      push (@grid, "</head>\n<body>\n<h1>".$b."</h1>\n\n");
      for my $d (sort keys %rng) {
        my ($num, $title) = split(/_/, $d);
        my $unit = lc($title);
        #push (@grid, "<hr>\n<b>$title Graph</b><br>\n<img src=../png/$b-bw-$unit.png>\n\n");
        push (@grid, "<img src=../png/$b-bw-$unit.png><br>\n");
      }
      push (@grid, "</body>\n</html>\n");
      if (! -e $html) {
        if(open(O,">$html")) {
          print O @grid;
          close(O);
        } else {
          die "Could not write to $html: $!\n";
        }
      } else {
        print "HTML already exists, skipping $html\n";
      }
      push (@full, "  <td><a href=../html/$b-bw.html><img border=0\n");
      push (@full, "\tsrc=../png/$b-bw-daily.png></a></td>\n");
      $fc++;
      if ($fc > 1) {
        push(@full, "</tr><tr>\n");
        $fc = 0;
      }
    }
    push (@full, "</tr>\n");
    if(open(O,">$outhtml/akamai.inc")) {
      print O @full;
      close(O);
    } else {
      die "Could not write to $outhtml/akamai.inc: $!\n";
    }
  } else {
    print "HTML dir does not exist, no HTML files will be written!\n";
  }
}



#------------------
# MAIN
#------------------

print "=====  Starting at " . strftime("%D %r", localtime(time)) . "  =====\n";

my %t;
my ($s, $b, $d);
for $s (sort keys %svc) {
  $service = eval 'new ' . $svc{$s}{'xsd'} . ';';
  #print "$s acquire_bandwidth($s,$service,$svc{$s}{'get'},$svc{$s}{'xsd'});\n";
  %t = acquire_bandwidth($s,$service,$svc{$s}{'get'},$svc{$s}{'xsd'});
  for $b (sort keys %t) {
    for $d (sort keys %{$t{$b}}) {
      $bw{$b}{$d}{$s} = $t{$b}{$d}{'bits'}; 
    }
  }
}

# zero out the missing values
for $s (sort keys %svc) {
  for $b (sort keys %bw) {
    for $d (sort keys %{$bw{$b}}) {
      $bw{$b}{$d}{$s} = 0 if (!$bw{$b}{$d}{$s});
    }
  }
  #print "\n";
}
print "\n----- DEBUG -----\n" . Dumper(%bw) .
	"\n----- DEBUG -----\n" if $opt{d};

updateRRD();
updatePNG();
updateHTML();
updateTotal();

print "=====  Finished at " . strftime("%D %r", localtime(time)) . "  =====\n";


        
#------------
# Subroutines
#------------

sub help {
    exec("perldoc $0");
}

sub inarray {
      if (ref($_[0]) eq 'ARRAY') { return "$_[0]" =~ m/$_[1]/; }
}

__END__

#--------------
# Documentation
#--------------

=cut

=head1 NAME

B<akarrd.pl> - Retrieve http and streaming reports bandwidth data via WebServices

=head1 SYNOPSIS

S<usage: B<akarrd.pl> >

=head1 DESCRIPTION

Akamai Web Services. 
Retrieve the http and video traffic

=head1 OPTIONS

Command line arguments include:

	-h	help
	-d	debug
	-v	verbose
	-u user	login for access
	-p pass	password for access
	-o dir	output directory
	-s hr	start Akamai collection hours ago (default: 1 hr)


=head1 AUTHOR

ikenticus

=cut
