#!/usr/local/bin/perl
#This is a project to be able to run the nmap command, which is a security scanner originally written by Gordon Lyon. 
#The user will be prompt to enter two variables, the box and the port. 

print "Please enter your box:\n";
$box = <STDIN>;
chomp($box);

print "Please enter your port:\n";
$port = <STDIN>;
chomp($port);

@scannet =`nmap $box -p $port`;

if (($box eq "") && ($port eq ""))
	{
	 print "Your box and port are empty";
	}
elsif(($box ne "") && ($port ne ""))
	{
	 print "Your results are:\n @scannet";
	}
else
	{
	print "You are ignoring something, please try again";
	}




