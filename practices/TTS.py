#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 技术支持：https://www.jianshu.com/u/69f40328d4f0 
# 技术支持 https://china-testing.github.io/
# https://github.com/china-testing/python-api-tesing/blob/master/practices/TTS.py
# 项目实战讨论QQ群630011153 144081101
# CreateDate: 2018-11-22

import win32com.client as wincl
from tkinter import *


def text2Speech():
 text = e.get()
 speak = wincl.Dispatch("SAPI.SpVoice")
 speak.Speak(text)


#window configs
tts = Tk()
tts.wm_title("Text to Speech")
tts.geometry("225x105")
tts.config(background="#708090")


f=Frame(tts,height=280,width=500,bg="#bebebe")
f.grid(row=0,column=0,padx=10,pady=5)
lbl=Label(f,text="Enter your Text here : ")
lbl.grid(row=1,column=0,padx=10,pady=2)
e=Entry(f,width=30)
e.grid(row=2,column=0,padx=10,pady=2)
btn=Button(f,text="Speak",command=text2Speech)
btn.grid(row=3,column=0,padx=20,pady=10)
tts.mainloop()
