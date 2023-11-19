# calcualte the speed of the operations of Number class


import time
import numpy as np
from number import Number

N = 1000000



def Number_Class_Time():
    def test_add():
        time_arr = [] 
        for i in range(N):
            a = Number(np.random.randint(0, 100))
            b = Number(np.random.randint(0, 100))
            start_time = time.time()
            c = a + b
            end_time = time.time()
            time_arr.append(end_time - start_time)
        return time_arr


    def test_mul():
        time_arr = [] 
        for i in range(N):
            a = Number(np.random.randint(0, 100))
            b = Number(np.random.randint(0, 100))
            start_time = time.time()
            c = a * b
            end_time = time.time()
            time_arr.append(end_time - start_time)
        return time_arr

    time_add = test_add()
    time_mul = test_mul()

    sum = 0
    for i in range(N):
        sum += time_add[i]
    print(f"total time for add in Number: {sum}")

    sum = 0
    for i in range(N):
        sum += time_mul[i]
    print(f"total time for mul in Number: {sum}")


def Numpy_Time():
    def test_add():
        time_arr = [] 
        for i in range(N):
            a = np.random.randint(0, 100)
            b = np.random.randint(0, 100)
            start_time = time.time()
            c = a + b
            end_time = time.time()
            time_arr.append(end_time - start_time)
        return time_arr


    def test_mul():
        time_arr = [] 
        for i in range(N):
            a = np.random.randint(0, 100)
            b = np.random.randint(0, 100)
            start_time = time.time()
            c = a * b
            end_time = time.time()
            time_arr.append(end_time - start_time)
        return time_arr

    time_add = test_add()
    time_mul = test_mul()

    sum = 0
    for i in range(N):
        sum += time_add[i]
    print(f"total time for add in Numpy: {sum}")

    sum = 0
    for i in range(N):
        sum += time_mul[i]
    print(f"total time for mul in Numpy: {sum}")




if __name__ == "__main__":
    Number_Class_Time()
    Numpy_Time()

