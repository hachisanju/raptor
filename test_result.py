class TestResult(object):

	def __init__(self):
		self.points = 0.0
		self.totalpoints = 0.0
		self.error = None
		self.errorstatus = None

	def set_points(self, points):
		self.points = points

	def set_total_points(self, totalpoints):
		self.totalpoints = totalpoints

	def set_error(self, error):
		self.error = error

	def set_error_status(self, errorstatus):
		self.errorstatus = errorstatus