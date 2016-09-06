import sys
import subprocess
import report
from test_result import TestResult

def run( d , dname ):

	partitionTestResult = TestResult()
	partitionTestResult.set_total_points(1)
	partitionScore = 0
	print("Validating that {} has a separate partition...".format(d))
	try:

		#Input:
		#>>> mount | grep `d`
		#Expected output:
		#>>> tmpfs on `d` type tmpfs (rw,nosuid,nodev,noexec,relatime)

		fsTest1 = subprocess.Popen(('mount'), stdout=subprocess.PIPE)
		try:
			fstTest1Output = subprocess.check_output(('grep', d), stdin=fsTest1.stdout)
			partitionScore += 1
			print("......Passed!")
			partitionScore += output_verification(fstTest1Output)
		except subprocess.CalledProcessError as e:
			report.report("(X)...{} does not exist in a separate partition.".format(d))
			mit(d, dname)
			

	except OSError:
		report.report("(!)...Tools do not support the use of the mount command.".format(fs))


	partitionTestResult.set_points(partitionScore)
	return partitionTestResult

def output_verification(str):
	return 0

def mit(d, dname):
			report.mitigation("      Mitigation: run systemctl unmask {}.mount".format(dname))
			report.mitigation("                      systemctl enable {}.mount\n".format(dname))
			report.mitigation("             Edit /etc/systemd/system/local-fs.target.wants/{}.mount to contain:".format(dname))
			report.mitigation("                      [Mount]")
			report.mitigation("                      What=tmpfs")
			report.mitigation("                      Where=".format(d))
			report.mitigation("                      Type-tmpfs")
			report.mitigation("                      Options=mode=1777,strictatime,noexec,nodev,nosuid")
			print("......Failed!")