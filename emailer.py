#!/usr/bin/env python
import re
import sys
from email.mime.multipart import MIMEMultipart

def create_addresses(from_addr,to_addr,cc=[],bcc=[]):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    if cc:
        msg['CC'] = cc
    if bcc:
        msg['BCC'] = bcc
    return msg.as_string()

def check_email_valid(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+",email) != None
