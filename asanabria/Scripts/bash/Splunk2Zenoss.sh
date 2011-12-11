#!/bin/sh

gunzip $8
UNZIPPED_FILE=`echo $8|sed -re "s/.gz$//g"`
CSV_HEADER=`head -n1 $UNZIPPED_FILE`
CSV_BODY=`cat $UNZIPPED_FILE | sed -e "1D"`
NUM_EVENTS=$1
SEARCH_TERMS=`echo $2 | sed -re "s/^/\'/g" -e "s/$/\'/g"`
SEARCH_STRING=`echo $3 | sed -re "s/^/\'/g" -e "s/$/\'/g"`
NAME_SAVED_SEARCH=$4
REASON_TRIGGERED=`echo $5 | sed -re "s/^/\'/g" -e "s/$/\'/g"`
LINK_SAVED_SEARCH=`echo $6 | sed -re "s/^/\'/g" -e "s/$/\'/g"`
ZENOSS="zenoss"
ZENOSS_EVENT_MAPPING="/Splunk/Alert"
ZENOSS_EVENT_KEY="Alert"
/opt/splunk/bin/scripts/zensendevent -c "$ZENOSS_EVENT_KEY_MAPPING" -k "$ZENOSS_EVENT_KEY" --server="$ZENOSS" -s Debug -p "$NAME_SAVED_SEARCH" -o SPLUNK_LINK="$LINK_SAVED_SEARCH" -o TRIGGERED="$REASON_TRIGGERED" -o NUMBER_OF_EVENTS="$NUM_EVENTS" -o SEARCH_STRING="$SEARCH_STRING" -o CSV_HEADER="$CSV_HEADER" -o CSV_BODY="$CSV_BODY" -o SAVED_SEARCH="$NAME_SAVED_SEARCH" $CSV_BODY
