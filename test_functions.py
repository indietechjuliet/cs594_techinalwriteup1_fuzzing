# fuzzing/test_functions.py
# Rachel Offutt 2021
#
# Some test functions to apply fuzzing to. They will fail in various, intended ways.

from fuzzing import KnownException

def test_add_integers(a, b):
	"""Test adding integers by simply converting inputs to int
	"""

	a_int = int(a)
	b_int = int(b)

	return a_int + b_int

def test_add_integers_with_exc(a, b):
	"""Test adding integers, but check that a and b are actually strings with numbers first.
	"""
	# If they are not both integers
	if not (is_integer(str(a)) and is_integer(str(b))):
		raise KnownException()
	return a_int + b_int

def is_integer(val):
	"""Use a very smoothbrained method to check if a string represents an integer

	Args:
		val (str): A string

	Returns:
		bool: Whether it is an integer or not.
	"""
	numbers = '1234567890'
	for character in str(val):
		if not character in numbers:
			return False
	return True
