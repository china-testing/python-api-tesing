#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-8
# datas.py
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib



def send_mail(recipients, sub, content, from_name='比对测试',server="smtp.126.com",
    files=[]): 
    EMAIL_SEND_USER = os.environ.get('EMAIL_SEND_USER')
    EMAIL_SEND_PASSPORT = os.environ.get('EMAIL_SEND_PASSPORT')    
    msg =  MIMEMultipart()
    msg.attach(MIMEText(content, 'plain'))
    msg['Subject'] = sub
    msg['From'] = "{}<{}>".format(from_name, EMAIL_SEND_USER)
    msg['To'] = ", ".join(recipients)
    try:
        s = smtplib.SMTP()
        s.connect(server)
        s.login(EMAIL_SEND_USER, EMAIL_SEND_PASSPORT)
        for f in files or []:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=os.path.basename(f)
                )
            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(f)
            msg.attach(part)
            
        print("send email to {}".format(recipients))
        s.sendmail(EMAIL_SEND_USER, recipients, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False
    
if __name__ == '__main__':

    if send_mail(['xurongzhong@sensetime.com'],"活体比对测试结果", "测试结果",
                 files=[r'output.xls']):
        print("发送成功")