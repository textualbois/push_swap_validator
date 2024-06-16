import subprocess
import random

def generate_input_ints(size_limit):
	random_number = random.randint(1, size_limit)
	numbers = list(range(1, random_number))
	random.shuffle(numbers)
	return ' '.join(map(str, numbers))

def call_push_swap(input):
	exec_location = '../dual_git/push_swap'
	process = subprocess.Popen([exec_location, input],
								stdout=subprocess.PIPE,
								stderr=subprocess.PIPE)
	output, errors = process.communicate()
	if errors:
		print("Error:", errors.decode())
		return
	return output

def school_checker(user_input, user_output):
	exec_location = '../dual_git/checker_Mac'
	process = subprocess.Popen([exec_location, user_input],
								stdin=subprocess.PIPE,
								stdout=subprocess.PIPE,
								stderr=subprocess.PIPE)

	checker_result, errors = process.communicate(input=user_output)
	if errors:
		print("hi, you got an Error:", errors.decode())
		return
	return checker_result.decode().strip().lower()

def your_checker(user_input, user_output):
	exec_location = '../dual_git/checker'
	process = subprocess.Popen([exec_location, user_input],
								stdin=subprocess.PIPE,
								stdout=subprocess.PIPE,
								stderr=subprocess.PIPE)

	checker_result, errors = process.communicate(input=user_output)
	if errors:
		print("hi, you got an Error:", errors.decode())
		return
	return checker_result.decode().strip().lower()

def validate_checker():
	iterations = 600
	size_limit = 600

	k = 0
	while k < iterations:
		if (k % 50 == 0):
			print("{0} out of {1}".format(k + 1, iterations))
		input = generate_input_ints(size_limit)

		output = call_push_swap(input)

		if output is not None:
			school_res = school_checker(input, output)
			your_res = your_checker(input, output)
			if school_res != your_res:
				print("Your checker failed. should be {0} input:\n {1}\n".format(school_res ,input) +
		  				"and output:\n {0}".format(output.decode()))
				return

		else:
			print("output is none\n")
			return
		k = k + 1
	print("your checker works ... or you hardcoded it to say \"ok\" every time\n")

validate_checker()

exit()
