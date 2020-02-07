#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import time
import random
import os
import datetime

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CHECKER_PATH = "./Checker.py"
CHECKER_PATH_ABS = os.path.join(DIR_PATH, CHECKER_PATH)

LOG_PATH = "./status.log"
LOG_PATH_ABS = os.path.join(DIR_PATH, LOG_PATH)

while True: 
	cmd = ['python3', CHECKER_PATH_ABS]
	subprocess.Popen(cmd).wait()

	with open(LOG_PATH_ABS, "w") as f:
		f.write("Programm ausgefuehrt zuletzt am {}".format(datetime.datetime.now()))
	waittime = random.randint(10, 36000)
	print("Wait for {} seconds ({} hours)".format(waittime, waittime/60/60))
	time.sleep(waittime)

