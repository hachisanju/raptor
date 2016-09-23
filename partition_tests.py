import sys
import os
import subprocess
import report
from test_result import TestResult

def run( d , dname, full ):

	partitionTestResult = TestResult()
	if full == True:
		partitionTestResult.set_total_points(4)
	else:
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
			if full == True:
				partitionScore += output_verification(fstTest1Output, d, dname)
			print partitionScore
		except subprocess.CalledProcessError as e:
			report.report("(X)...{} does not exist in a separate partition.".format(d))
			mit(d, dname)
			

	except OSError:
		report.report("(!)...Tools do not support the use of the mount command.".format(fs))


	partitionTestResult.set_points(partitionScore)
	return partitionTestResult

def output_verification(output, d, dname):
	result = 0
	for line in output.split(os.linesep):
		if "on {} ".format(d) in line:
			result += options(line, d)
			print line
	return result

def options(partition, d):
	result = 0
	print("Ensuring nodev option is set on {} partition".format(d))

	if "nodev" in partition:
		result += 1
		print("......Passed!")
	else:
		print("......Failed!")

	print("Ensuring nosuid option is set on {} partition".format(d))

	if "nosuid" in partition:
		result += 1
		print("......Passed!")
	else:
		print("......Failed!")

	print("Ensuring noexec option is set on {} partition".format(d))

	if "noexec" in partition:
		result += 1
		print("......Passed!")
	else:
		print("......Failed!")

	return result

def mit(d, dname):
	if dname == "tmp":
			report.mitigation("      Mitigation: run systemctl unmask {}.mount".format(dname))
			report.mitigation("                      systemctl enable {}.mount\n".format(dname))
			report.mitigation("             Edit /etc/systemd/system/local-fs.target.wants/{}.mount to contain:".format(dname))
			report.mitigation("                      [Mount]")
			report.mitigation("                      What=tmpfs")
			report.mitigation("                      Where={}".format(d))
			report.mitigation("                      Type=tmpfs")
			report.mitigation("                      Options=mode=1777,strictatime,noexec,nodev,nosuid")
			print("......Failed!")
