#!/bin/sh
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-02-08 qq群： 144081101
# startup.sh

APP_MAIN=older.py
APP_LOG=logs
PID=0

getPID(){
    pythonps=`ps aux | grep $APP_MAIN | grep -v grep`
    if [ -n "$pythonps" ]; then
        PID=`echo $pythonps | awk '{print $2}'`
    else
        PID=0
    fi
}


startup(){
    getPID
    echo "================================================================================================================"
    if [ $PID -ne 0 ]; then
        echo "$APP_MAIN already started(PID=$PID)"
        echo "================================================================================================================"
    else
        echo -n "Starting $APP_MAIN"
         if [ ! -d "../$APP_LOG" ]; then
            mkdir "../$APP_LOG"
         fi
        nohup python3 $APP_MAIN > ../$APP_LOG/nohup.log 2>&1 &
        sleep 2
        getPID
        if [ $PID -ne 0 ]; then
            echo "(PID=$PID)...[Success]"
            echo "================================================================================================================"
        else
            echo "[Failed]"
            echo "================================================================================================================"
        fi
    fi
}

startup
