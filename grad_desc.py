import sys
import corr
import math
import time
import numpy as np
import matplotlib.pyplot as plt

iteration = []
costs = []

def 	h_func(thethas, x):
	summ = 0
	for i in range(len(x)):
		summ += thethas[i] * x[i]
	return (summ)

def 	cost_func(x, y, thethas):
	# print(type(x))
	m = float(len(x))
	total_cost = 0
	for i in range(y.shape[0]):
		total_cost += h_func(thethas[i], x[i]) - y[i]
	return (total_cost / m)


def step_gradient(x_arr, y_arr, thethas, learning_rate):
	new_thethas = [[0] * x_arr.shape[1]] * y_arr.shape[1]
	N = float(x_arr.shape[1])
	# print(thethas)
	for i in range(y_arr.shape[0] - 1):
		y = y_arr[i]
		for j in range(x_arr.shape[1] - 1):
			# print("I digit:{}, {}".format(i, thethas[i]))
			curr_thetha = - (1 / N) * x_arr[i][j] *  ( h_func ( thethas[i], x_arr[i] ) - y )
			# curr_thetha = - (2 / N) * x_arr[i][j] * ( cost.h_func ( thethas[i], x_arr[i] ) - y )
			# print(type(curr_thetha))
			new_thetha = thethas[i][j] - (learning_rate * curr_thetha)
			new_thethas[i].append(new_thetha if j != 0 else 1)
	# print(new_thethas)	
	return new_thethas

def gradient_descent_runner(x, y, thethas, learning_rate, num_iterations):
    with open("costs.txt", "w") as file:
    	for i in range(num_iterations):
            thethas = step_gradient(x, y, thethas, learning_rate)
            # storing info for plotting the graph
            if (i % 10) == 0:
				costs.append(cost_func(thethas, x, y))
				iteration.append(i)
    return thethas


# number of iteration should be done till we consider that we have found our optimal line
# learning rate, controls the step made in searching new linear line(new thetha1 and new thetha0)
def     main(x, y, thethas, num_iterations = 100000, learning_rate = 0.000000000000001):
	# setting the start point
	start_time = time.time()
	# finding the best fitting thethas, with which we got the lowest error rate
	thethas = gradient_descent_runner(x, x, thethas, learning_rate, num_iterations)
	# calculating time of processing
	end_time = time.time() - start_time

	result = cost_func(thethas, x, y)
  	# print("Thethas: {}".format(thethas))
  	print("Cost: {}. Time: {}".format(result, end_time))
  	# print(costs)
  	plt.plot(costs, iteration)
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


if __name__ == '__main__':
	if len(sys.argv) == 3:
		x_arr = np.array(ft_get_data(sys.argv[1]))
		y_arr = np.array(ft_get_data(sys.argv[2]))
		if not (y_arr.shape[0] == x_arr.shape[0] and y_arr.shape[1] == 1):
			print("Recieved anwers for data set have wrong dimension.")
			sys.exit(1)
		thethas = np.zeros((x_arr.shape[0], x_arr.shape[1]))
		x_arr[:, 0] = 1
		print(x_arr)
		print(y_arr)
		print(thethas)
		main(x_arr, y_arr, thethas)
	else:
		print("Unsuffiecient amount of passed arguments")

