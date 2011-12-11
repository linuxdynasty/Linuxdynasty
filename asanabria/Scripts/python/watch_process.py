#!/usr/bin/env python

import os, sys, re, string

uptime = os.popen('uptime |grep -oP "load average: [0-9]+\.[0-9]+" | grep -oP [0-9]+\.[0-9]+').readlines()
