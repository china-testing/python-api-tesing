#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 技术支持：https://www.jianshu.com/u/69f40328d4f0 
# 技术支持 https://china-testing.github.io/
# https://github.com/china-testing/python-api-tesing/blob/master/practices/traceroute.py
# 项目实战讨论QQ群630011153 144081101
# CreateDate: 2018-11-26

import socket
import io
import struct
import sys

class flushfile(io.FileIO):
    def __init__(self, f):
        self.f = f
    def write(self, x):
        self.f.write(x)
        self.f.flush()

sys.stdout = flushfile(sys.stdout)

def main(dest_name):
    dest_addr = socket.gethostbyname(dest_name)
    port = 55285
    max_hops = 30

    ttl = 1
    while True:
        rec_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        timeout = struct.pack("ll", 2, 0)
        rec_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)

        rec_socket.bind(("", port))
        sys.stdout.write(" %d   " % ttl)
        send_socket.sendto(bytes("", "utf-8"), (dest_name, port))

        curr_addr = None
        curr_name = None
        finished = False
        tries = 1
        while not finished and tries > 0:
            try:
                _, curr_addr = rec_socket.recvfrom(512)
                finished = True
                curr_addr = curr_addr[0]
                try:
                    curr_name = socket.gethostbyaddr(curr_addr)[0]
                except socket.error:
                    curr_name = curr_addr
            except socket.error as err:
                tries -= 1
                sys.stdout.write("* ")
        
        send_socket.close()
        rec_socket.close()

        if not finished:
            pass
        
        if curr_addr is not None:
            curr_host = "%s (%s)" % (curr_name, curr_addr)
        else:
            curr_host = ""
        sys.stdout.write("%s\n" % (curr_host))

        ttl += 1
        if curr_addr == dest_addr or ttl > max_hops:
            break

if __name__ == "__main__":
    main("china-testing.github.io")