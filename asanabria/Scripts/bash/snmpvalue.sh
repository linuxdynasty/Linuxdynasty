#!/bin/bash
showUsage() {
  cat << EOF

Usage: ${0###} -c community -o oid -H host

   -c community community string
   -o oid   	oid to look up
   -H host   	host to lookup

EOF
  exit 1
}

while getopts "c:o:H:" option; do
  case $option in
    c) community=$OPTARG ;;
    o) oid=$OPTARG ;;
    H) host=$OPTARG ;;
  esac
done
[ -z "$community" -o -z "$oid" -o -z "$host" ] && showUsage

output=`snmpget -v1 -c $community $host $oid |awk '{print $4}'`

echo -n $output
