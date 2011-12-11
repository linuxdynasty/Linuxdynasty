#!/bin/bash
# This is my second firewall to date....4/11/05
# In my new house...
# Been greatly Modified since 4/11/05 Todays date May 18 2005

ipt="/sbin/iptables"
Onet="eth1"
Inet="eth0"
Local="lo"
Internal_net="192.168.101.0"
Internal_lan="192.168.101.0/24"
Internal_voice="192.168.101.4"
Internal=`ifconfig eth0 | grep "inet addr:" | cut -d : -f2 | cut -d " " -f 1`
Chewbaca="192.168.101.9"
Vadar="192.168.101.32"
bad_ips=`cat /etc/bad_ips`
IMask="24"
External=`ifconfig eth1 | grep "inet addr:" | cut -d : -f2 | cut -d " " -f 1`
External_tcp_dports="25,993,443,80,873"
External_tcp_sports="25,993,443,80,873"
Internal_tcp_dports="22,25,389,636,993,443,80,514,49777"
Internal_tcp_sports="22,25,389,636,993,443,80,514,49777"
External_udp_dports="67,68,53,123"
External_udp_sports="53,67,68,123"
Internal_udp_sports="53,68,67,123,514"
Internal_udp_dports="53,68,67,123,514"
Established_tcp_dports="21,873"
IANA_addr="128.0.0.0/16 169.254.0.0/16 172.16.0.0/12 191.255.0.0/16 192.0.0.0/24 192.0.2.0/24 192.88.99.0/24 192.168.0.0/16 198.18.0.0/15 224.0.0.0/4 240.0.0.0/4 $External"
ROOT_UID=0
 
 if [ "$UID" -eq "$ROOT_UID" ]
	then
	:
else
	printf 'Y0U @R3 N07 Y37 R3@DY, Y0U @R3 N07 R007n'
		exit 1
fi

restart () {
	stop
	start
	}
stop () {
$ipt -P INPUT ACCEPT
$ipt -P OUTPUT ACCEPT
$ipt -P FORWARD ACCEPT
$ipt -F
$ipt -X
$ipt -Z
$ipt -F -t nat
$ipt -F -t mangle
$ipt -Z -t nat
$ipt -Z -t mangle
	echo "Chewbaca's Firewall has been tamed!!!"
	}
start () {

$ipt -P INPUT DROP
$ipt -P OUTPUT DROP
$ipt -P FORWARD DROP
$ipt -F
$ipt -X
$ipt -Z
$ipt -F -t nat
$ipt -F -t mangle
$ipt -Z -t nat
$ipt -Z -t mangle
$ipt -N IANA
$ipt -N INTERNAL_NET_IN
$ipt -N EXTERNAL_NET_IN
$ipt -N INTERNAL_NET_OUT
$ipt -N EXTERNAL_NET_OUT
$ipt -N ONET_LOG

echo '1' > /proc/sys/net/ipv4/ip_forward
echo '1' > /proc/sys/net/ipv4/ip_dynaddr
#################NAT Table#########################################################################################
$ipt -t nat -A POSTROUTING -o $Onet -j MASQUERADE
$ipt -t nat -A PREROUTING -i $Onet -p tcp --dport 3389 -j DNAT --to-destination 192.168.101.15:3389
$ipt -t nat -A PREROUTING -i $Onet -p tcp --dport 22 -j DNAT --to-destination 192.168.101.9:22
$ipt -t nat -A PREROUTING -i $Onet -p tcp --dport 8000 -j DNAT --to-destination 192.168.101.9:80
$ipt -t nat -A PREROUTING -i $Onet -p tcp --dport 113 -j DNAT --to-destination 192.168.101.15:113


#################FILTER Table######################################################################################
###################################################################################################################
#################Block SOURCE IP's FROM SSH ATTACKS################################################################
$ipt -A INPUT -i $Onet -j ONET_LOG
for log_badip in $bad_ips; do
        $ipt -A ONET_LOG -p tcp -i $Onet --dport 22 -s $log_badip -j LOG --log-level info --log-prefix "SSH ATTACKS"
        done

for badip in $bad_ips; do
	$ipt -A INPUT -i $Onet -s $badip -j DROP
	done
#################Block SPoofers####################################################################################
$ipt -A INPUT -i $Onet -j IANA
for sip in $IANA_addr; do
	$ipt -A IANA -i $Onet -s $sip -j DROP
	done
#################INPUT LAN Chain###################################################################################
$ipt -A INPUT -i $Local -j ACCEPT
$ipt -A INPUT -i $Inet -j INTERNAL_NET_IN
$ipt -A INTERNAL_NET_IN -i $Inet -p icmp -s  $Internal_lan -j ACCEPT
$ipt -A INTERNAL_NET_IN -i $Inet -p tcp -m multiport --destination-ports $Internal_tcp_dports -m state --state NEW,ESTABLISHED -j ACCEPT
$ipt -A INTERNAL_NET_IN -i $Inet -p tcp -m multiport --source-ports $Internal_tcp_sports -m state --state ESTABLISHED -j ACCEPT
$ipt -A INTERNAL_NET_IN -i $Inet -p udp -m multiport --destination-ports $Internal_udp_dports -j ACCEPT
$ipt -A INTERNAL_NET_IN -i $Inet -p udp -m multiport --source-ports $Internal_udp_sports -j ACCEPT
#################INPUT WAN Chain###################################################################################
$ipt -A INPUT -i $Onet -j EXTERNAL_NET_IN
$ipt -A EXTERNAL_NET_IN -i $Onet -p tcp -m multiport --destination-ports $External_tcp_dports -m state --state NEW,ESTABLISHED -j ACCEPT
$ipt -A EXTERNAL_NET_IN -i $Onet -p tcp -m multiport --source-ports $External_tcp_sports -m state --state ESTABLISHED -j ACCEPT
$ipt -A EXTERNAL_NET_IN -i $Onet -p tcp -m multiport --destination-ports $Established_tcp_dports -m state --state ESTABLISHED -j ACCEPT
$ipt -A EXTERNAL_NET_IN -i $Onet -p udp -m multiport --source-ports $External_udp_sports -j ACCEPT
#################OUTPUT LAN Chain##################################################################################
$ipt -A OUTPUT -o $Local -j ACCEPT
$ipt -A OUTPUT -o $Inet -j INTERNAL_NET_OUT
$ipt -A INTERNAL_NET_OUT -o $Inet -p icmp --icmp-type echo-request -j ACCEPT
$ipt -A INTERNAL_NET_OUT -o $Inet -p tcp -m multiport --destination-ports $Internal_tcp_dports -m state --state NEW,ESTABLISHED -j ACCEPT
$ipt -A INTERNAL_NET_OUT -o $Inet -p tcp -m multiport --source-ports $Internal_tcp_sports -m state --state ESTABLISHED -j ACCEPT
$ipt -A INTERNAL_NET_OUT -o $Inet -p tcp -m multiport --destination-ports $Established_tcp_dports -m state --state ESTABLISHED -j ACCEPT
$ipt -A INTERNAL_NET_OUT -o $Inet -p udp -m multiport --source-ports $Internal_udp_sports -j ACCEPT
$ipt -A INTERNAL_NET_OUT -o $Inet -p udp -m multiport --destination-ports $Internal_udp_dports -j ACCEPT
################OUTPUT WAN Chain###################################################################################
$ipt -A OUTPUT -o $Onet -j EXTERNAL_NET_OUT
$ipt -A EXTERNAL_NET_OUT -o $Onet -p icmp --icmp-type echo-request -j ACCEPT
$ipt -A EXTERNAL_NET_OUT -o $Onet -p tcp -m multiport --destination-ports $External_tcp_dports -m state --state NEW,ESTABLISHED -j ACCEPT
$ipt -A EXTERNAL_NET_OUT -o $Onet -p tcp -m multiport --source-ports $External_tcp_sports -m state --state ESTABLISHED -j ACCEPT
$ipt -A EXTERNAL_NET_OUT -o $Onet -p tcp -m multiport --destination-ports $Established_tcp_dports -m state --state ESTABLISHED -j ACCEPT
$ipt -A EXTERNAL_NET_OUT -o $Onet -p udp -m multiport --source-ports $External_udp_sports -j ACCEPT
$ipt -A EXTERNAL_NET_OUT -o $Onet -p udp -m multiport --destination-ports $External_udp_dports -j ACCEPT
$ipt -A EXTERNAL_NET_OUT -o $Onet -p tcp --dport 21 -m state --state NEW,ESTABLISHED -j ACCEPT
$ipt -A EXTERNAL_NET_OUT -o $Onet -p tcp --sport 1023:65335 --dport 1023:65335 -m state --state ESTABLISHED,RELATED -j ACCEPT
################FORWARD Chain######################################################################################
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --dport 22 -m state --state NEW -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --dport 3724 -j ACCEPT
$ipt -A FORWARD -i $Inet -o $Onet -p tcp --dport 3724 -j ACCEPT
$ipt -A FORWARD -i $Inet -o $Onet -p tcp --dport 6112 -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --dport 6112 -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p udp --sport 514 -m state --state ESTABLISHED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --sport 514 -m state --state ESTABLISHED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p udp --dport 514 -m state --state ESTABLISHED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --dport 514 -m state --state ESTABLISHED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --dport 80 -m state --state NEW -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --sport 119 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
$ipt -A FORWARD -i $Inet -o $Onet -p tcp --dport 119 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --sport 113 -m state --state ESTABLISHED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --sport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p udp --sport 53 -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p udp --dport 53 -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --dport 6881 -j DROP
$ipt -A FORWARD -o $Inet -i $Onet -p tcp --dport 6881 -j DROP
$ipt -A FORWARD -o $Inet -i $Onet -p tcp --dport 6882 -j DROP
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --dport 6882 -j DROP
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --dport 3389 -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --sport 873 -m state --state NEW,ESTABLISHED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --sport 1023:65335 -m state --state ESTABLISHED,RELATED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --sport 995 -m state --state NEW,ESTABLISHED -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p tcp --sport 587 -m state --state NEW,ESTABLISHED -j ACCEPT
$ipt -A FORWARD -i $Inet -o $Onet -p udp --sport 10000:60000 --dport 10000:60000 -j ACCEPT
$ipt -A FORWARD -o $Onet -i $Inet -p udp --sport 10000:60000 --dport 10000:60000 -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -p udp --sport 10000:60000 --dport 10000:60000 -j ACCEPT
$ipt -A FORWARD -o $Inet -p udp --dport 67 -j ACCEPT
$ipt -A FORWARD -o $Inet -p udp --sport 67 -j ACCEPT
$ipt -A FORWARD -o $Inet -p udp --dport 68 -j ACCEPT
$ipt -A FORWARD -o $Inet -p udp --sport 68 -j ACCEPT
$ipt -A FORWARD -i $Inet -o $Onet -j ACCEPT
$ipt -A FORWARD -i $Onet -o $Inet -j ACCEPT
echo "Chebaca's Firewall is ON!!!"
}
        case "$1" in
        start)
          start;;
        stop)
          stop;;
        restart)
          restart;;
             *)
         echo "Usage: $0 {start|stop|restart}"
	 exit 1
	 esac

