import subprocess
import random

def generate_shuffled_ints(n):
	numbers = list(range(1, n + 1))

	random.shuffle(numbers)
	return ' '.join(map(str, numbers))

def call_push_swap(n):
	exec_location = '../dual_git/push_swap'
	#checker_location = './checker_Mac'
	shuffled_ints = generate_shuffled_ints(n)

	process = subprocess.Popen([exec_location, shuffled_ints],
								stdout=subprocess.PIPE,
								stderr=subprocess.PIPE)

	# Pipe the output to 'wc -l'
	output, errors = subprocess.Popen(['wc', '-l'], stdin=process.stdout, stdout=subprocess.PIPE).communicate()
	#output, errors = subprocess.Popen(['wc', '-l'], stdin=process.stdout, stdout=subprocess.PIPE).communicate()

	if errors:
		print("Error:", errors.decode())
		return

	return int(output.decode().strip())

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
			output = call_push_swap(stack_size[i])
			if output is not None:
				sum_operations = sum_operations + output
				max_operations = max(max_operations, output)
				if min_operations != -1:
					min(min_operations, output)
				else:
					min_operations = output
			else:
				return
			k = k + 1

		print("for stack size {0} results are:\n".format(stack_size[i]) +
				"min operations observed = {0}\n".format(min_operations) +
				"average operations = {0}\n".format(sum_operations / (k - 1)) +
				"max operations observed = {0}\n".format(max_operations))

		j = 0
		while j < len(allowed_limits[i]):
			if max_operations > allowed_limits[i][j]:
				break
			else:
				j += 1
		if j == 5:
			print("you got maximum points for stack size of {0}\n\n".format(stack_size[i]))
		else:
			print("you get only {0} points.\nfor maximum points you need less than {1} max moves.\n\n".format(j, allowed_limits[i][4]))

validate_push_swap()

exit()
