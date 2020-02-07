#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import time
import random
import os


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CHECKER_PATH = "./Checker.py"
CHECKER_PATH_ABS = os.path.join(DIR_PATH, CHECKER_PATH)

while True: 
	cmd = ['python3', 'CHECKER_PATH_ABS'] 
	subprocess.Popen(cmd).wait()

	with open("/home/pi/NetzclubChecker/status.log", "w") as f:
		f.write("Programm ausgefuehrt")
	waittime = random.randint(10, 36000)
	print("Wait for {} seconds ({} hours)".format(waittime, waittime/60/60))
	time.sleep(waittime)

