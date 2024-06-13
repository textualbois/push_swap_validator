import subprocess
import random

def generate_shuffled_ints(n):
	numbers = list(range(1, n + 1))

	random.shuffle(numbers)
	return ' '.join(map(str, numbers))

def call_push_swap(n):
	exec_location = '../push_swap/push_swap'
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

		for k in range(1, iterations + 1):
			output = call_push_swap(stack_size[i])
			if output is not None:
				sum_operations += output
				max_operations = max(max_operations, output)
				if min_operations != -1:
					min(min_operations, output)
				else:
					min_operations = output
			else:
				return
			
		print(f"for stack size {stack_size[i]} results are:\n" + 
				f"min operations observed = {min_operations}\n" + 
				f"average operations = {sum_operations / k}\n" +
				f"max operations observed = {max_operations}\n")
		
		j = 0
		while j < len(allowed_limits[i]):
			if max_operations > allowed_limits[i][j]:
				break 
			else:
				j += 1
		if j == 5:
			print(f"you got maximum points for stack size of {stack_size[i]}\n\n")
		else:
			print(f"you get only {j} points.\nfor maximum points you need less than {allowed_limits[i][4]} max moves.\n\n")

validate_push_swap()

exit()
