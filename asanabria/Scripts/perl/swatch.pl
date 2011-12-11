#!/usr/bin/perl
#

$mode = join (' ',@ARGV);
chomp $mode;
$swatch = "/usr/bin/swatch -c /etc/.swatchrc -t /var/log/Auth-priv.log --awk-field-syntax --pid-file=/var/run/swatch.pid --daemon";
$kill = "kill -9";
$rm = "/usr/bin/rm -f";
$pid_file = "/var/run/swatch.pid";



if ($mode =~ /^stop$/){
        &STOP;
        }

if ($mode =~ /^start$/){
        &START;
        }

if ($mode =~ /^restart$/){
	&STOP;
	&START;
	}

if ($mode =~ /^status$/){
        &STATUS;
        }


sub START{	
	if (-e $pid_file){
		$pid =`/usr/bin/cat /var/run/swatch.pid`;
		chomp $pid;
		print "Swatch is already running, PID = $pid\n";
		
		}
		else {
			print "Starting swatch with $swatch\n";
			system $swatch;
			}
	}


sub STOP{
	if (-e $pid_file){
		print "Stopping Swatch\n";
		$pid =`/usr/bin/cat /var/run/swatch.pid`;
		chomp $pid;
	  	$tail_pid = `/bin/ps --ppid $pid | /bin/egrep -o "(([0-9]{3})|([0-9]{4})|([0-9]{5})|([0-9]{6}))"`;
		if ($tail_pid){
	  		$tail_pid = `/bin/ps --ppid $pid | /bin/egrep -o "(([0-9]{3})|([0-9]{4})|([0-9]{5})|([0-9]{6}))"`;
			chomp $tail_pid;
			}
		system "$kill $pid";
		system "$kill $tail_pid";
		system "$rm $pid_file";
		}
		else{
			print "Swatch isnt running\n";
			}
	}

sub STATUS{
	if (-e $pid_file){
		$pid =`/usr/bin/cat /var/run/swatch.pid`;
	  	chomp $pid;
	  	$tail_pid = `/bin/ps --ppid $pid | /bin/egrep -o "(([0-9]{3})|([0-9]{4})|([0-9]{5})|([0-9]{6}))"`;
	  	if ($tail_pid){
		chomp $tail_pid;
	  	print "Swatch is running, Swatch-PID = $pid\tChild Tail-PID = $tail_pid\n";
		        }
		}
	  		else{
	  			print "Swatch is dead\n";
				}
}
