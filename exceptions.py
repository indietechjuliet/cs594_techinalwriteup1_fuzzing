# fuzzing/exceptions.py
#Rachel Offutt 2021
#
# Known exceptions when fuzzing

class KnownException(Exception):
	
	def __init__(self):
		"""Exception raised when our function trips an error but we expected to trip that error.
		"""

		super(Exception, self).__init__("Tripped known exception")
