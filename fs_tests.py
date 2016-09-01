import sys
import subprocess
from raptor import report

#"mounting" provides a quick way to test which file systems are allowed to be mounted by
#the current machine. According to the CIS benchmarks, removing support for unneeded
#filesystem types reduces the local attack surface of the system. If a filesystem type
#is not needed, it should be disabled.

def mounting( fs ):
	passedTest = True
	print("Validating that {} support is disabled...".format(fs))
	try:
		fsTest1 = subprocess.check_output(('modprobe', '-n', '-v', fs))
		if "install /bin/true" not in fsTest1:
			report("(X)...Support for mounting {} is not disabled.".format(fs))
			passedTest = False
		fsTest2 = subprocess.Popen(('lsmod'), stdout=subprocess.PIPE)
		try:
			fsTest2Output = subprocess.check_output(('grep', fs), stdin=fsTest2.stdout)
			passedTest = False
			print("(X) ... A module exists in /proc/modules for {}.")
		except subprocess.CalledProcessError as e:
			if str(e) != "Command '('grep', '{}')' returned non-zero exit status 1".format(fs):
				passedTest = False
			

	except OSError:
		report("(!)...Tools do not support running a scan for {}".format(fs))
		passedTest = False

	if passedTest == True:
		print("......Passed!")
	else:
		print("......Failed!")
	return passedTest

def partition( d ):
	passedTest = True
	print("Validating that {} has a separate partition...".format(d))
	try:
		fsTest1 = subprocess.Popen(('mount'), stdout=subprocess.PIPE)
		try:
			fstTest1Output = subprocess.check_output(('grep', d), stdin=fsTest1.stdout)
		except subprocess.CalledProcessError as e:
			report("(X)...{} does not exist in a separate partition.".format(d))
			passedTest = False

	except OSError:
		report("(!)...Tools do not support the use of the mount command.".format(fs))
		passedTest = False
	if passedTest == True:
		print("......Passed!")
	else:
		print("......Failed!")

	return passedTest