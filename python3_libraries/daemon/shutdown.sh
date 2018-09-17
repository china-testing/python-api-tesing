#!/bin/sh
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-02-08 qq群： 144081101
# shutdown.sh

APP_MAIN=older.py
PID=0

getPID(){
    pythonps=`ps aux | grep $APP_MAIN | grep -v grep`
    if [ -n "$pythonps" ]; then
        PID=`echo $pythonps | awk '{print $2}'`
    else
        PID=0
    fi
}

shutdown(){
    getPID
    echo "================================================================================================================"
    if [ $PID -ne 0 ]; then
        echo -n "Stopping $APP_MAIN(PID=$PID)..."
        kill -9 $PID
        if [ $? -eq 0 ]; then
            echo "[Success]"
            echo "================================================================================================================"
        else
            echo "[Failed]"
            echo "================================================================================================================"
        fi
        getPID
        if [ $PID -ne 0 ]; then
            shutdown
        fi
    else
        echo "$APP_MAIN is not running"
        echo "================================================================================================================"
    fi
}

shutdown
exit 0
