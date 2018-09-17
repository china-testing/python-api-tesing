#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-02-08 qq群： 144081101
# daemon2.py

import time
import logging
import logging.handlers
from daemon import runner

class App():
    
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5
        
    def run(self):
        
        logs = logging.getLogger('MyLogger')
        logs.setLevel(logging.DEBUG)
        fh = logging.handlers.RotatingFileHandler(
            '/tmp/test.log',maxBytes=10000000,backupCount=5)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(u'%(asctime)s [%(levelname)s] %(message)s')
        fh.setFormatter(formatter)
        logs.addHandler(fh)  
        
        while True:
            for i in range(10):
                logs.info("Beginning Scan {0}! \n".format(i))
            time.sleep(1)

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()