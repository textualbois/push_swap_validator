import subprocess
import random

def print_loop_results(stack_size, min_operations, sum_operations, k, max_operations):
		print("for stack size {0} results are:\n".format(stack_size) +
				"min operations observed = {0}\n".format(min_operations) +
				"average operations = {0}\n".format(sum_operations / (k - 1)) +
				"max operations observed = {0}\n".format(max_operations))

def generate_shuffled_ints(n):
	numbers = list(range(1, n + 1))
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

def check_output_is_ok(user_input, user_output):
	exec_location = '../dual_git/checker_Mac'
	process = subprocess.Popen([exec_location, user_input],
								stdin=subprocess.PIPE,
								stdout=subprocess.PIPE,
								stderr=subprocess.PIPE)

	checker_result, errors = process.communicate(input=user_output)
	if errors:
		print("hi, you got an Error:", errors.decode())
		return
	return checker_result.decode().strip().lower() == "ok"

def count_lines(encoded_output):
	decoded_output = encoded_output.decode().strip()
	line_count = decoded_output.count('\n') + 1
	return line_count

def validate_push_swap():
	iterations = 100
	stack_size = [5, 100, 500]
	allowed_limits = [[12, 12, 12, 12, 12], [1500, 1300, 1100, 900, 700], [11500, 10000, 8500, 7000, 5500]]

	for i in range(len(stack_size)):
		min_operations = -1
		max_operations = 0
		sum_operations = 0

		k = 1
		while k <= iterations:
			input = generate_shuffled_ints(stack_size[i])
		#	print(input)
			output = call_push_swap(input)
		#	print(output)
			#print("|")
			if output is not None:
				if check_output_is_ok(input, output):
					operations_current = count_lines(output)
					sum_operations = sum_operations + operations_current
					max_operations = max(max_operations, operations_current)
					if min_operations > -1:
						min_operations = min(min_operations, operations_current)
					else:
						min_operations = output
				else:
					print("You didn't pass the school checker. Stopping here\nInput:\n {0}\n".format(input))
					return

			else:
				print("output is none\n")
				return
			k = k + 1

		print_loop_results(stack_size[i], min_operations, sum_operations, k, max_operations)

		j = 0
		while j < len(allowed_limits[i]):
			if max_operations > allowed_limits[i][j] or max_operations == 0:
				break
			else:
				j += 1
		if j == 5:
			print("you got maximum points for stack size of {0}\n\n".format(stack_size[i]))
			if i == 2:
				print("try validating your checker now for the bonus points\n")
		else:
			print("you get only {0} points.\nfor maximum points you need less than {1} max moves.\n\n".format(j, allowed_limits[i][4]))

validate_push_swap()

exit()
