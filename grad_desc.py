import sys
import corr
import math
import time
import numpy as np
import matplotlib.pyplot as plt

iteration = []
costs = []

# quiz_question param is used if function is used to solve Andrew Ng's Coursera quiz question, which involves mean normalization

def  ft_mean_normalization(x, quiz_question = False):
	if (quiz_question):
		std_dev_arr = np.max(x, axis=0) - np.min(x, axis=0)
	else:
		std_dev_arr = np.std(x, axis=0)
	mean_arr = np.mean(x, axis=0)
	print(mean_arr)
	print(std_dev_arr)
	new_x = np.ndarray((x.shape[0], x.shape[1]))

	for i in range(mean_arr.shape[0]):
		mean_value = float(mean_arr[i])
		std_dev_val = float(std_dev_arr[i])
		for j in range(x.shape[0]):
			new_x[j][i] = ((x[j][i] - mean_value) / std_dev_val)
	return (new_x)

def 	ft_scale_features(x):
	max_x = x.max(axis=0)
	new_x = np.ndarray((x.shape[0], x.shape[1]))

	for i in range(max_x.shape[0]):
		max_value = float(max_x[i])
		for j in range(x.shape[0]):
			new_x[j][i] = (x[j][i] / max_value)

	return (new_x)

def 	h_func(thethas, x):
	summ = 0
	print(x.shape)
	for i in range(x.shape[0] - 1):
		summ += thethas[i] * x[i]
	return (summ)

def 	cost_func(x, y, thethas):
	print(y.shape)
	m = float(len(x))
	total_cost = 0
	for i in range(y.shape[1]):
		total_cost += h_func(thethas[i], x[i]) - y[i]
	return (total_cost / m)


def step_gradient(x_arr, y_arr, thethas, learning_rate):
	new_thethas = np.ndarray((x_arr.shape[0], x_arr.shape[1]))
	N = float(x_arr.shape[1])
	#print("Brand New thethas: {}".format(new_thethas))
	print(y_arr.shape, x_arr.shape)
	for i in range(y_arr.shape[1]):
		for j in range(x_arr.shape[1] - 1):
			# print("I digit:{}, {}".format(i, thethas[i]))
			curr_thetha = - (2 / N) * x_arr[i][j] *  ( h_func ( thethas[i], x_arr[i] ) - y_arr[i] )
			# curr_thetha = - (2 / N) * x_arr[i][j] * ( cost.h_func ( thethas[i], x_arr[i] ) - y_arr[i] )
			new_thetha = thethas[i][j] - (learning_rate * curr_thetha)
			new_thethas[i][j] = (new_thetha if j != 0 else 1)
	#print("New thethas: {}".format(new_thethas))
	return new_thethas

def gradient_descent_runner(x, y, thethas, learning_rate, num_iterations):
	with open("costs.txt", "w") as file:
		for i in range(num_iterations):
			thethas = step_gradient(x, y, thethas, learning_rate)
			# storing info for plotting the graph
			if (i % 1000) == 0:
				costs.append(cost_func(x, y, thethas))
				iteration.append(i)
	return thethas


# number of iteration should be done till we consider that we have found our optimal line
# learning rate, controls the step made in searching new linear line(new thetha1 and new thetha0)
def     main(x, y, thethas, num_iterations = 100000, learning_rate = 0.000000000000001):
	# setting the start point
	start_time = time.time()
	# finding the best fitting thethas, with which we got the lowest error rate
	thethas = gradient_descent_runner(x, y, thethas, learning_rate, num_iterations)
	# calculating time of processing
	end_time = time.time() - start_time

	result = cost_func(x, y, thethas)
  	# print("Thethas: {}".format(thethas))
  	print("Cost: {}. Time: {}".format(result, end_time))
  	# print(costs)
  	plt.plot(iteration, costs)
  	plt.ylabel("Cost function values")
  	plt.xlabel("Number of iterations")
  	plt.show()
  	#plt.savefig("grad_desc.png")

def 	ft_get_data(filename):
	data = []

	try:
		with open(filename) as file:
			for string in file:
				string.replace('\n', '')
				if len(string) > 1:
					data.append(corr.prepare_arrs(string))
	except IOError:
		print("File can not be opened.")
		sys.exit(1)
	return (data)

def 	ft_split_getting_data(filename):
	x_data = []
	y_data = []

	try:
		with open(filename) as file:
			for string in file:
				string.replace('\n', '')
				if len(string) > 1:
					string = string.split('\t')
					data_point = float(string[0])
					x_data.append(data_point)
					y_data.append(float(string[1]))
	except IOError:
		print("File can not be opened.")
		sys.exit(1)
	return (x_data, y_data)


if __name__ == '__main__':
	if len(sys.argv) == 2 or len(sys.argv) == 3:
		if len(sys.argv) == 2:
			x_arr, y_arr = np.array(ft_split_getting_data(sys.argv[1]))
			thethas = np.zeros((1, x_arr.shape[0]))
		else:
			x_arr = np.array(ft_get_data(sys.argv[1]))
			y_arr = np.array(ft_get_data(sys.argv[2]))
			if not (y_arr.shape[0] == x_arr.shape[0] and y_arr.shape[1] == 1):
				print("Recieved anwers for data set have wrong dimension.")
				sys.exit(1)
			thethas = np.zeros((x_arr.shape[0], x_arr.shape[1]))
		print(x_arr)
		print("-----------------------------------------------AFTER ADDING X0, which is zero-------------------------------------------")
		print(x_arr)
		print(y_arr)
		print(thethas)

		x_arr = ft_scale_features(x_arr)
		x_arr = ft_mean_normalization(x_arr, True)
		print(x_arr)
		
		# x_arr[:, 0] = 1
		# main(x_arr, y_arr, thethas)
	else:
		print("Unsuffiecient amount of passed arguments")

