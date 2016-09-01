import sys
import getopt
import subprocess

#List of tests to perform. These are defined by the CIS hardening guidelines for CentOS Linux 07
FILESYSTEMS = True

#Arguments for main set the tests which are to be disbaled
def main():
	global FILESYSTEMS

	if len(sys.argv) == 1:
		print("Please enter a command. For a list of available commands and flags, add -help")

	if "-help" in str(sys.argv):
		print("       runtest       initiate a test for the system")
		print("       -dfs          disable filesystem tests")

	if "-dfs" in str(sys.argv):
		FILESYSTEMS = False

	if "runtest" in str(sys.argv):
		initTest()

def initTest():
	global FILESYSTEMS

	if FILESYSTEMS == True:
		filesystemGrade = filesystemTest()
		print (filesystemGrade)

def filesystemTest():
	passedCramfs = True
	try:
		cramfsTest1 = subprocess.check_output(('modprobe', '-n', '-v', 'cramfs'))
		if cramfsTest1 == "install /bin/true":
			print(passedCramfs)
		else:
			passedCramfs = False
		cramfsTest2 = subprocess.Popen(('lsmod'), stdout=subprocess.PIPE)
		try:
			cramfsTest2Output = subprocess.check_output(('grep', 'cramfs'), stdin=cramfsTest2.stdout)
			passedCramfs = False
		except subprocess.CalledProcessError as e:
			if str(e) != "Command '('grep', 'cramfs')' returned non-zero exit status 1":
				passedCramfs = False
				print str(e)
			

	except OSError:
		print "No such file or directory"
		passedCramfs = False

	return passedCramfs
	
if __name__ == "__main__":
	main()
