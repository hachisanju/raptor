import sys
import subprocess
import report
from test_result import TestResult

#"mounting" provides a quick way to test which file systems are allowed to be mounted by
#the current machine. According to the CIS benchmarks, removing support for unneeded
#filesystem types reduces the local attack surface of the system. If a filesystem type
#is not needed, it should be disabled.

def mounting( fs ):

	mountingTestResult = TestResult()
	mountingTestResult.set_total_points(1)
	passedTest = True

	print("Validating that {} support is disabled...".format(fs))

	#In order to run the tests, a try catch block is set up to ensure the neede commands
	#are available on the system.

	try:

		#Input:
		#>>> modprobe -n -v `fs`
		#Expected output:
		#>>> install /bin/true

		fsTest1 = subprocess.check_output(('modprobe', '-n', '-v', fs))
		if "install /bin/true" not in fsTest1:
			report.report("(X)...Support for mounting {} is not disabled.".format(fs))
			passedTest = False

		#Input:
		#>>> lsmod | grep `fs`
		#Expected output:
		#<NONE>

		fsTest2 = subprocess.Popen(('lsmod'), stdout=subprocess.PIPE)

		#With grep piping, a try catch block is needed to guarantee that if the grep
		#returns no results, the process will not fail.
		try:
			fsTest2Output = subprocess.check_output(('grep', fs), stdin=fsTest2.stdout)
			passedTest = False
			print("(X) ... A module exists in /proc/modules for {}.")
		except subprocess.CalledProcessError as e:
			if str(e) != "Command '('grep', '{}')' returned non-zero exit status 1".format(fs):
				passedTest = False
			
	except OSError as e:                    #Catch if any of our commands fail
		report.error("(!)...Tools do not support running a scan for {}\n".format(fs))
		mountingTestResult.set_error(True)
		mountingTestResult.set_error_status("      {}".format(e))
		return mountingTestResult

	#If passedTest has been set by any of the checks, the test fails
	if passedTest == True:
		report.report("......Passed!")
		mountingTestResult.set_points(1)
	else:
		report.mitigation("      Mitigation: run install {} /bin/true".format(fs))
		report.report("......Failed!")

	
	#Send up the result
	return mountingTestResult

def partition( d , dname ):

	partitionTestResult = TestResult()
	partitionTestResult.set_total_points(1)
	partitionScore = 0
	print("Validating that {} has a separate partition...".format(d))
	try:
		fsTest1 = subprocess.Popen(('mount'), stdout=subprocess.PIPE)
		try:
			fstTest1Output = subprocess.check_output(('grep', d), stdin=fsTest1.stdout)
			partitionScore += 1
			print("......Passed!")
		except subprocess.CalledProcessError as e:
			report.report("(X)...{} does not exist in a separate partition.".format(d))
			report.mitigation("      Mitigation: run systemctl unmask {}.mount".format(dname))
			report.mitigation("                      systemctl enable {}.mount".format(dname))
			print("......Failed!")
			

	except OSError:
		report.report("(!)...Tools do not support the use of the mount command.".format(fs))


	partitionTestResult.set_points(partitionScore)
	return partitionTestResult

