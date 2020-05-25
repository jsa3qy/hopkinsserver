#!/bin/bash

EMAILS="jessealloy@gmail.com,connorhagan20@gmail.com,adisrikanth.aks@gmail.com,will17.r@gmail.com"
pip3 install -r requirements.txt >/dev/null
python3 main.py $EMAILS > msg.txt
/usr/sbin/ssmtp $EMAILS < msg.txt
