import sys
import math


def mean(arr):
        total_mean = 0
        for mem in arr:
                total_mean = mem + total_mean
        return (float)(total_mean / len(arr))

def multiplicate_means(arr1, arr2):
        total_res = 0
        for i in range(len(arr1)):
                total_res = total_res + arr2[i] * arr1[i]
        return total_res

def square_elems(arr):
        total_res = 0
        for elem in arr:
                total_res = total_res + elem * elem
        return (total_res)

def substract_mean(mean, arr):
        print(mean)
        for i in range(len(arr)):
                arr[i] = arr[i] - mean
        return arr

def prepare_arrs(arr):
        data = []
        arr = arr.split('\t')
        for elem in arr:
                data.append(float(elem))
        return data

def main():
        x = prepare_arrs(sys.argv[1])
        y = prepare_arrs(sys.argv[2])
        x_mean = substract_mean(mean(x), x)
        y_mean = substract_mean(mean(y), y)
        print(x_mean)
        print(y_mean)
        mean_mult = multiplicate_means(x_mean, y_mean)
        squared_x = square_elems(x_mean)
        squared_y = square_elems(y_mean)

        print(mean_mult)
        print(squared_x)
        print(squared_y)
        res = (float)(mean_mult / math.sqrt(squared_x * squared_y))
        return (res)

if __name__ == "__main__":
        print len(sys.argv)
        if len(sys.argv) is 3:
                print ("Pearson's corr: {}".format(main()))
