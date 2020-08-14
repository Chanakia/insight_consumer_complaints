#!/bin/bash

#
# Use this shell script to compile (if necessary) your code and then execute it. Belw is an example of what might be found in this file if your program was written in Python 3.7
APP_HOME=$PWD

python3.8 "$APP_HOME"/src/consumer_complaints.py "$APP_HOME"/input/complaints.csv "$APP_HOME"/output/report.csv