#!/usr/bin/perl

use strict;
use Getopt::Std;

our ( $opt_P, $opt_L, $opt_S, $opt_D, $opt_h );
getopts('P:L:S:D:h');

if ($opt_h) {
    &help();
}
elsif ( $opt_P =~ /\w+/ && $opt_L =~ /\w+/ ) {
    &WorkersSub( $opt_P, $opt_L );
}
else {
    &help();
}

sub WorkersSub {
    unless ( defined($opt_S) ) {
        $opt_S = "/root/$opt_P.txt";
    }
    my $projectinfo = "doit -w $opt_P";
    system `$projectinfo > $project_tmp_file`;
    my $worker_properties;
    unless ( defined($opt_D) ) {
        $opt_D = "/etc/apache/sites/worker.properties";
    }
    my @line;
    my $i = 0;
    my $j = 0;
    open( TMP, "$opt_S" ) or die "Couldn't open $opt_S : $!\n";
    while (<TMP>) {
        if ( $_ !~ /\w+/ ) {
            next;
        }
        else {
            $line[$i] = $_;
            chomp $line[$i];
            $i++;
        }
    }
    close TMP;

    my @nline = @line;
    foreach my $host (@nline) {
        $host = "$host,";
    }

    open( WORKERS, ">$opt_D" ) or die "Couldn't open $opt_D for writing : $!\n";
    select WORKERS;
    print "workers.tomcat_home=/usr/share/tomcat6\n";
    print "workers.java_home=/usr/java/jdk1.6.0_01\n";
    print "ps=/\n\n";
    print "worker.list=@nline $opt_L, jkstatus, template\n";
    print "worker.maintain=30\n\n";
    print "#Basic Template\n";
    print "worker.template.port=8009\n";
    print "worker.template.type=ajp13\n";
    print "worker.template.socket_timeout=10\n";
    print "worker.template.socket_keepalive=1\n";
    print "worker.template.connection_pool_timeout=600\n";
    print "worker.template.lbfactor=1\n\n";

    foreach (@line) {
        print "#worker-$j\n";
        print "worker.$line[$j].host=$line[$j]-fe\n";
        print "worker.$line[$j].reference=worker.template\n\n";
        $j++;
    }

    print "#LB-info\n";
    print "worker.$opt_L.type=lb\n";
    print "worker.$opt_L.balance_workers=@nline $opt_L\n\n";
    print "#Status info\n";
    print "worker.jkstatus.type=status\n";

    close WORKERS;
}

sub print_usage {
    print
"Usage: $0 -P <PROJECT> -L <PROJECT-lb> -S <server_list> -D <worker.properties>\n";
}

sub help {
    print "\nKeeps Workers.proprites (mod_jk) file up2date\n";
    print "GPL licence, (c)2007-2007 Allen Sanabria\n\n";
    print_usage();
    print <<EOT;
-h, 
   print this help message
-P, -P <PROJECT>
   name of project
-L, -L <PROJECT-lb>	     name of LB for project
   For every project there has to be a lb defined which is actually 
   every server in the project so a name like sho-lb can be used
-D -D <workers.properties> so if you do not pass the -D option it will use 
   /etc/apache/sites/worker.properties unless specified
-S -S <src_server_file> so if you do not pass the -D option it will use 
   /root/$opt_P.txt unless specified. this is where doit saves the list of servers to

EOT
}
