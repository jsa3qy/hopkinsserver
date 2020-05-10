#!/bin/bash

EMAILS="jessealloy@gmail.com jalloy@yext.com"
pip3 install -r requirements.txt >/dev/null
python3 main.py EMAILS > msg.txt
for email in $EMAILS; do
    ssmtp $email < msg.txt
done
