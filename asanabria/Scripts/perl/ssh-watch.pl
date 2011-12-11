#!/usr/bin/perl -w


use strict;
use Net::SMTP;

my $smtp = Net::SMTP->new('mailer.communityconnect.com');
$smtp->mail($ENV{USER});
$smtp->to('asanabria\@mail.communityconnect.com');
$smtp->data();

use vars qw "$data $ssh_host $ssh_restart $ssh_output";

$ssh_host = "/usr/bin/ssh localhost echo ok 2>&1";
$ssh_restart = "/etc/init.d/sshd restart";

open SSH, "$ssh_host|" || die "couldnt execute $ssh_host\n";
	while ($ssh_output = <SSH>){
		chomp($ssh_output);
			if ($ssh_output =~ /(ssh_exchange_identification)/) {
				print "ssh error\n";
				system $ssh_restart;
		                $smtp->datasend("To: asanabria\@mail.communityconnect.com\n");
                		$smtp->datasend("Subject: SSH was restarted\n");
                		$smtp->datasend("\n");
                		$smtp->datasend("\tRemote Exchange identification was Encountered $1.\n\n");
                		$smtp->datasend(" Since this was encountered ssh was restarted.\n");
                		$smtp->dataend();
                		$smtp->quit;

				exit 0;
			}
				else{
					print "ssh ok\n";
					exit 0;
				}
	}
