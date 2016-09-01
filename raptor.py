import sys
import getopt
import subprocess
import fs_tests

#List of tests to perform. These are defined by the CIS hardening guidelines for CentOS Linux 07
FILESYSTEMS = True


def main():                     #Arguments for main set the tests which are to be disbaled
	global FILESYSTEMS

	if len(sys.argv) == 1:
		print("Please enter a command. For a list of available commands and flags, add -help")

	if "-help" in str(sys.argv):
		print("       runtest       initiate a test for the system")
		print("       -dfs          disable filesystem tests")

	if "-dfs" in str(sys.argv):
		FILESYSTEMS = False

	if "runtest" in str(sys.argv):
		init_test()


def init_test():                 #The main testing phase
	
	global FILESYSTEMS           #Relocalization of Global Variables

	FSTESTS = 8.0                #Total number of filesystem tests
	FSPASS = 0.0                 #Total number of tests passed
	

	if FILESYSTEMS == True:

		#Tests for mountable filesystems
		#-------------------------------
		if fs_tests.mounting("cramfs"):
			FSPASS += 1
		if fs_tests.mounting("freevxfs"):
			FSPASS += 1
		if fs_tests.mounting("hfs"):
			FSPASS += 1
		if fs_tests.mounting("hfsplus"):
			FSPASS += 1
		if fs_tests.mounting("squashfs"):
			FSPASS +=1
		if fs_tests.mounting("udf"):
			FSPASS += 1
		if fs_tests.mounting("vfat"):
			FSPASS += 1
		
		#Tests for world-writable directories
		#------------------------------------
		if fs_tests.partition("/tmp"):
			FSPASS += 1

	FSGRADE = FSPASS/FSTESTS * 100
	print ("Filesystem overall score = {}".format(FSGRADE))


def report(str):
	print(str)


if __name__ == "__main__":
	main()
