#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-02-08 qq群： 144081101
# daemon1.py

import daemon
import time

with daemon.DaemonContext():
    f = open("/tmp/test.log",'w')
    while True:
        f.write('''
        Library to implement a well-behaved Unix daemon process.

This library implements the well-behaved daemon specification of PEP 3143, “Standard daemon process library”.

A well-behaved Unix daemon process is tricky to get right, but the required steps are much the same for every daemon program. A DaemonContext instance holds the behaviour and configured process environment for the program; use the instance as a context manager to enter a daemon state.
''')
        f.write("{0}\n".format(time.ctime(time.time())))
        time.sleep(1)