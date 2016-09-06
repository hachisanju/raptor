import sys
import subprocess
import report
from test_result import TestResult
def run( fs ):

	mountingTestResult = TestResult()
	mountingTestResult.set_total_points(1)
	passedTest = True

	print("Validating that {} support is disabled...".format(fs))

	#In order to run the tests, a try catch block is set up to ensure the needed commands
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