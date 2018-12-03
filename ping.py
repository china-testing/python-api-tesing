#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 技术支持：https://www.jianshu.com/u/69f40328d4f0 
# 技术支持 https://china-testing.github.io/
# https://github.com/china-testing/python-api-tesing/blob/master/practices/ping.py
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-11-22

import os 
import argparse 
import socket
import struct
import select
import time


ICMP_ECHO_REQUEST = 8 # Platform specific
DEFAULT_TIMEOUT = 2
DEFAULT_COUNT = 3


class Pinger(object):
    """ Pings to a host -- the Pythonic way"""

    def __init__(self, target_host, count=DEFAULT_COUNT, timeout=DEFAULT_TIMEOUT):
        self.target_host = target_host
        self.count = count
        self.timeout = timeout


    def do_checksum(self, source_string):
        """  Verify the packet integritity """
        sum = 0
        max_count = (len(source_string)/2)*2
        count = 0
        while count < max_count:

            val = source_string[count + 1]*256 + source_string[count]                   
            sum = sum + val
            sum = sum & 0xffffffff 
            count = count + 2

        if max_count<len(source_string):
            sum = sum + ord(source_string[len(source_string) - 1])
            sum = sum & 0xffffffff 

        sum = (sum >> 16)  +  (sum & 0xffff)
        sum = sum + (sum >> 16)
        answer = ~sum
        answer = answer & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer

    def receive_pong(self, sock, ID, timeout):
        """
        Receive ping from the socket.
        """
        time_remaining = timeout
        while True:
            start_time = time.time()
            readable = select.select([sock], [], [], time_remaining)
            time_spent = (time.time() - start_time)
            if readable[0] == []: # Timeout
                return

            time_received = time.time()
            recv_packet, addr = sock.recvfrom(1024)
            icmp_header = recv_packet[20:28]
            type, code, checksum, packet_ID, sequence = struct.unpack(
       "bbHHh", icmp_header
   )
            if packet_ID == ID:
                bytes_In_double = struct.calcsize("d")
                time_sent = struct.unpack("d", recv_packet[28:28 + bytes_In_double])[0]
                return time_received - time_sent

            time_remaining = time_remaining - time_spent
            if time_remaining <= 0:
                return


    def send_ping(self, sock,  ID):
        """
        Send ping to the target host
        """
        target_addr  =  socket.gethostbyname(self.target_host)

        my_checksum = 0

        # Create a dummy heder with a 0 checksum.
        header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
        bytes_In_double = struct.calcsize("d")
        data = (192 - bytes_In_double) * "Q"
        data = struct.pack("d", time.time()) + bytes(data.encode('utf-8'))

        # Get the checksum on the data and the dummy header.
        my_checksum = self.do_checksum(header + data)
        header = struct.pack(
      "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1
  )
        packet = header + data
        sock.sendto(packet, (target_addr, 1))


    def ping_once(self):
        """
        Returns the delay (in seconds) or none on timeout.
        """
        icmp = socket.getprotobyname("icmp")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        except socket.error as e:
            if e.errno == 1:
                # Not superuser, so operation not permitted
                e.msg +=  "ICMP messages can only be sent from root user processes"
                raise socket.error(e.msg)
        except Exception as e:
            print ("Exception: %s" %(e))

        my_ID = os.getpid() & 0xFFFF

        self.send_ping(sock, my_ID)
        delay = self.receive_pong(sock, my_ID, self.timeout)
        sock.close()
        return delay


    def ping(self):
        """
        Run the ping process
        """
        ip = socket.gethostbyname(self.target_host)
        print ("PING {} ({}) 56(84) bytes of data.".format(
            self.target_host, ip))
        datas = []
        start = time.time()
        for i in range(self.count):          
            try:
                delay  =  self.ping_once()
            except socket.gaierror as e:
                print ("Ping failed. (socket error: '%s')" % e[1])
                break

            if delay  ==  None:
                print ("Ping failed. (timeout within %ssec.)" % self.timeout)
            else:      
                delay = delay * 1000
                datas.append(delay)
                print ("64 bytes from {0} in {1:0.3f} ms".format(ip, delay))
            time.sleep(0.1)
        total_time = time.time() - start
        print('--- {} ping statistics ---'.format(ip))
        print('{0} packets transmitted, {1} received, {2:0.2f}% packet loss, time {3} ms'.format(
            self.count, len(datas), (self.count - len(datas))/self.count*100, int(10000*total_time)))
        print('rtt min/avg/max = {:0.3f}/{:0.3f}/{:0.3f} ms'.format(
            min(datas), sum(datas)/len(datas), max(datas)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python ping')
    parser.add_argument('host', action="store", help=u'host')
    parser.add_argument('-c', action="store", dest="count", default=3, type=int,
                        help=u'number of ping')    
    parser.add_argument('-t', action="store", dest="timeout", default=2, 
                        type=int, help=u'timeout')      
    given_args = parser.parse_args()  
    pinger = Pinger(target_host=given_args.host, count=given_args.count, 
                    timeout=given_args.timeout)
    pinger.ping()