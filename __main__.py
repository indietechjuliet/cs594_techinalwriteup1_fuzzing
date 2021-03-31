# /__main__.py
# Rachel Offutt 2021
#
# This is called when you execute this package.

from fuzzing import (
	test_add_integers,
	test_add_integers_with_exc,
	KnownException,
)

testing_functions = {
	'dumb': test_add_integers,
	'refined': test_add_integers_with_exc,
}

def use_fuzzingbook(test_function):

	from fuzzingbook.Fuzzer import RandomFuzzer

	f = RandomFuzzer()
	for x in range(999):
		fuz = f.fuzz()
		try:
			#string = buf.decode("ascii")
			test_function(fuz, fuz)
		except KnownException:
			pass
	print("Fuzzingbook found no exceptions")

def use_pythonfuzz(test_function):
	
	from pythonfuzz.main import PythonFuzz
	from html.parser import HTMLParser

	@PythonFuzz
	def fuzz(buf):
		try:
			#string = buf.decode("ascii")
			test_function(buf, buf)
		except KnownException:
			pass

	fuzz()
	# This will run for a very long time on a good function which does not trip exceptions

import sys


fuzzing_lib = 'fuzzingbook'
function_refinement = "dumb"

if testing_functions.get(function_refinement) is None:
	raise ValueError("Unsupported refinement code: '" + str(function_refinement) + "'. Options are: " + str(list(testing_functions.keys())))

t_fn = testing_functions[function_refinement]

if fuzzing_lib == 'fuzzingbook':
	use_fuzzingbook(t_fn)
elif fuzzing_lib == 'pythonfuzz':
	use_pythonfuzz(t_fn)
