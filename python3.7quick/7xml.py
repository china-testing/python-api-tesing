#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-11-12
import xml.dom.minidom

doc = xml.dom.minidom.parse("test.xml");

# print out the document node and the name of the first child tag
print (doc.nodeName)
print (doc.firstChild.tagName)
# get a list of XML tags from the document and print each one
expertise = doc.getElementsByTagName("expertise")
print ("{} expertise:".format(expertise.length))
for skill in expertise:
    print(skill.getAttribute("name"))

# create a new XML tag and add it into the document
newexpertise = doc.createElement("expertise")
newexpertise.setAttribute("name", "BigData")
doc.firstChild.appendChild(newexpertise)
print (" ")

expertise = doc.getElementsByTagName("expertise")
print ("{} expertise:".format(expertise.length))
for skill in expertise:
    print (skill.getAttribute("name"))
