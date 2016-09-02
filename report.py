import sys

MITIGATION = True

def report(str):
	print(str)

def mitigation(str):
	global MITIGATION
	if MITIGATION == True:
		print(str)

def error(str):
	sys.stderr.write(str)
	#print(str)

def set_mitigation(set):
	global MITIGATION
	MITIGATION = set

