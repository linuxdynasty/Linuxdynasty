#!/bin/bash
#
# /etc/init.d/swatch
# init script for Swatch.
#
# chkconfig: 2345 90 60
# description: Swatch
#November 11th 2009 Allen Sanabria
#http://linuxdynasty.org
#
CONFIG="/etc/swatch/swatch.conf"
PID="/var/run/swatch.pid"
LOGFILE="/var/log/secure"
PIDS="/tmp/pids.txt"
RETVAL=0

swatch_start() {
if [ -f $PID ]
  then
    echo "Swatch is already running"
    cat $PID
  else
    echo "Starting Swatch"
    /usr/bin/swatch --config-file=$CONFIG --tail-file=$LOGFILE --pid-file=$PID > /dev/null 2>&1 &
    RETVAL=$?
fi
}


swatch_stop() {
if [ -f $PID ]
  then
    echo "Stopping Swatch"
    PARENT="$(< "$PID")"
    INIT_PID=`ps -o ppid $PARENT |awk ' /[0-9]+/ { print $1 } '`
    CPID1=`ps --ppid $PARENT |awk ' /[0-9]+/ { print $1 } '`
    kill -9 $INIT_PID $PARENT $CPID1
    rm -f $PID $PIDS
    RETVAL=$?
  else
    echo "Swatch is not running!"
fi
}

swatch_status() {
if [ -f $PID ]
  then
    echo "Swatch is running"
    PARENT="$(< "$PID")"
    INIT_PID=`ps -o ppid $PARENT |awk ' /[0-9]+/ { print $1 } '`
    ps -o pid -o command --pid $INIT_PID --pid $PARENT --ppid $PARENT
  else
    echo "Swatch is not running" 
  RETVAL=$?
fi
}


case "$1" in
  start)
    swatch_start
    ;;
  stop)
    swatch_stop
    ;;
  restart)
    swatch_stop
    swatch_start
    ;;
  status)
    swatch_status
    ;;
  *)
    echo "Usage: $0 {start|stop|restart|status}"
    exit 1
esac


exit $RETVAL

