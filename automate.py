#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import time
import random


while True: 
	cmd = ['python3', '/home/pi/NetzclubChecker/Checker.py']
	subprocess.Popen(cmd).wait()

	with open("/home/pi/NetzclubChecker/status.log", "w") as f:
		f.write("Programm ausgefuehrt")
	waittime = random.randint(10, 36000)
	print("Wait for {} seconds ({} hours)".format(waittime, waittime/60/60))
	time.sleep(waittime)

