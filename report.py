import sys

MITIGATION = True
ERROR = True

def report(str):
	print(str)

def mitigation(str):
	global MITIGATION
	if MITIGATION == True:
		print(str)

def error(str):
	global ERROR
	if ERROR:
		sys.stderr.write(str)
	#print(str)

def set_mitigation(set):
	global MITIGATION
	MITIGATION = set

def set_error(set):
	global ERROR
	ERROR = set

