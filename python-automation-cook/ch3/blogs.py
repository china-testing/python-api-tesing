#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-10-16

import requests
from bs4 import BeautifulSoup

def get_upcoming_events(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    events = soup.findAll('article')

    for event in events:
        event_details = {}
        event_details['name'] = event.find('h1').find("a").text
        print(event_details)

get_upcoming_events('https://china-testing.github.io/')
