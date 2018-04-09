import sys
import cost
import corr
import math
import time
import numpy as np
import matplotlib.pyplot as plt

iteration = []
costs = []

def step_gradient(thethas, x_arr, y_arr, learningRate):
        new_thethas = [[] * len(x_arr)] * len(y_arr)#[[0] * len(x_arr)] * len(y_arr)
        N = float(len(x_arr))
        for i in range(len(y_arr)):
                y = y_arr[i]
                for j in range(0, len(x_arr)):
                        #print(x_arr[i])
                        curr_thetha = -(2/N) * x_arr[i][j] * (cost.h_func(thethas[i], x_arr[i]) - y)
                        new_thetha = thethas[i][j] - (learningRate * curr_thetha)
                        new_thethas[i].append(new_thetha) if j != 0 else 0
        return new_thethas

def gradient_descent_runner(x, y, thethas, learning_rate, num_iterations):
        cost_file = open("costs.txt", "w")
        for i in range(num_iterations):
                thethas = step_gradient(thethas, x, y, learning_rate)
                # some random if-stmt values(changable), uncomment the for loop above and you will see difference at once
                if (i % 10) == 0:
			costs.append(cost.cost_func(thethas, x, y))
			iteration.append(i)
                #cost_file.write("{}\n".format(str(res)))
        cost_file.close()
        return thethas

def     main(x, y, thethas = [0]):
        # number of iteration should be done till we consider that we have found our optimal line
        num_iterations = 100000
        # learning rate, controls the step made in searching new linear line(new thetha1 and new thetha0)
        learning_rate = 0.000000000000000000001
        arr_x, arr_y = corr.prepare_arrs(x, y)
        #arr_x = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
        #arr_y = [1, 2, 3, 4]
        #thethas = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]#[[0] * len(arr_x)] * len(arr_y)
        #result = cost.cost_func(thethas, arr_x, arr_y)
        #print("Result of cost function: {}".format(result))
        start_time = time.time()
        thethas = gradient_descent_runner(arr_x, arr_y, thethas, learning_rate, num_iterations)
        end_time = time.time() - start_time
        result = cost.cost_func(thethas, arr_x, arr_y)
        print("Thethas: {}".format(thethas))
        print("Cost: {}. Time: {}".format(result, end_time))
	print(costs)
	plt.plot(costs, iteration)
	plt.ylabel("Cost function values")
	plt.xlabel("Number of iterations")
	plt.show()
	#plt.savefig("grad_desc.png")
	
if __name__ == '__main__':
        main(sys.argv[1], sys.argv[2])

