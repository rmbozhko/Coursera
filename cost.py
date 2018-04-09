import sys
import corr#.prepare_arrs as prepare_data

def     h_func(thethas, x):
        #print("Thethas: {}, x: {}".format(thethas, x))
        n = len(x)
        result = 0
        #print(x, thethas)
        for i in range(n):
                result += (float)(thethas[i] * x[i])
        return (result)

def     cost_func(thethas, x, y):
        total = 0
        for i in range(len(y)):
                for j in range(len(x)):
                        res = ((h_func(thethas[i], x[i]) - y[i]) ** 2)
                        total = total + res
        total = total / float(2 * len(x))
        return (total)

def     main(x, y, thethas = [0]):
        arr_x, arr_y = corr.prepare_arrs(x, y)
        thethas = [0] * len(arr_x)
        result = cost_func(thethas, arr_x, arr_y)
        print("Result of cost function: {}".format(result))

if __name__ == '__main__':
        if len(sys.argv) > 2:
        #       if len(sys.argv[1]) == len(sys.argv[2]):
                        if len(sys.argv) == 5:
                                main(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]))
                        elif len(sys.argv) == 4:
                                main(sys.argv[1], sys.argv[2], float(sys.argv[3]))
                        else:
                                main(sys.argv[1], sys.argv[2])
        #       else:
        #               print("Lengths of passed data sets are not same")
        else:
                print("Pass the theta value for one variable cost function\nP.S. Don't forget about data")

