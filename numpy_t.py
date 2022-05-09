import numpy
import numpy as np

def task_10x10():
    ret = np.zeros((10, 10), dtype=int)
    ret[0] += 1
    return ret

def task_border():
    ret = np.zeros((10, 10), dtype=int)
    ret[0] += 1
    ret[9] += 1
    ret += ret.transpose()
    ret[ret >= 2]//=2
    return ret

def task_2_5x5():
    return np.ones((5,5), dtype = int)*2

def task_0123():
    ret = np.zeros((10,10), dtype = int)
    ret[0:5, 5:10] += 1
    ret[5:10, 5:10] += 3
    ret[5:10, 0:5] += 2
    return ret

def task_chess():
    ret = np.zeros((10, 10), dtype=int)
    ret[::2, ::2] += 1
    ret[1::2, 1::2] += 1
    return ret

def task_1_to_9_lines():
    return (np.zeros((9, 9), dtype=int) + np.array([i for i in range(1, 10)])).transpose()

def task_1_to_100():
    return (np.zeros((10, 10), dtype=int) + np.array([i for i in range(10)])).transpose()*10 + \
           np.zeros((10, 10), dtype=int) + np.array([i for i in range(1, 11)])

def task_multiplication_table():
    return (np.array([[i for i in range(1, 10)]]).transpose())*np.array([[i for i in range(1, 10)]])

def task_3_diags(n, a, b):
    ret = np.zeros((n, n), dtype=int)
    ret[range(n), range(n)] += a
    ret[range(1, n), range(n - 1)] += b
    ret[range(n - 1), range(1, n)] += b

    return ret

def task_double_chess():
    return np.array([[(i%4)//2 for i in range(20)]])*np.array([[(i%4)//2 for i in range(20)]]).transpose() + \
           np.array([[((i + 2)%4)//2 for i in range(20)]])*np.array([[((i + 2)%4)//2 for i in range(20)]]).transpose()

def task_chukh(n):
    vert = np.array([i for i in range(n)])*np.ones((n, n), dtype = int)
    ret = np.array([i%2 + 1 for i in range(n)])*np.ones((n, n), dtype = int)
    ret[vert >= vert.transpose()] = ret.transpose()[vert >= vert.transpose()]
    # Было бы мило, если бы работало     ret[vert >= vert.transpose()] = ret.transpose(),
    # но numpy для такого недостаточно продвинут
    return ret


print(task_chukh(2))