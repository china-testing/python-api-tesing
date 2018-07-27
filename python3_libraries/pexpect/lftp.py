#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# 技术支持 钉钉群：21745728(可以加钉钉pythontesting邀请加入) 
# qq群：144081101 591302926  567351477
# CreateDate: 2018-07-27
import pexpect

class Lftp(object):

    client = None

    @classmethod
    def connect(cls, ip, username="andrew", password="654321_", prompt='~>',
                silent=False):
        child = pexpect.spawn('lftp {}:{}@{}'.format(username, password, ip), 
                              maxread=5000)

        i = 1
        # Enter password
        while i != 0:
            i = child.expect([prompt, pexpect.TIMEOUT])
            if not silent:
                print(child.before.decode('utf-8'), child.after.decode('utf-8'))
            if i == 0:  # find prompt
                pass
            else: 
                raise Exception('ERROR TIMEOUT! LFTP could not login. ')
        Lftp.client = child

    @classmethod
    def command(cls, cmd, prompt='~>', silent=False):
        Lftp.client.buffer = b''
        Lftp.client.send(cmd + "\r")
        # Lftp.client.setwinsize(400,400)
        Lftp.client.expect([prompt,])
        if not silent:
            print(Lftp.client.before.decode('utf-8'), 
                  Lftp.client.after.decode('utf-8'))
        return Lftp.client.before, Lftp.client.after

    @classmethod
    def close(cls):
        Lftp.client.close()
        

c = Lftp()
c.connect('172.20.17.200')
c.command("ls -l")
c.command("mirror projects")
c.close()