#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-11-12

import urllib.request
# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://china-testing.github.io/address.html')

#get the result code and print it
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
print (data)