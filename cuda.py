import numpy as np
import time


def VectorAdd(a, b):
    return a + b


def main():
    N = 32000000

    A = np.ones(N)
    B = np.ones(N)

    start_time = time.time()

    C = VectorAdd(A, B)
    print(f'Time elapsed {time.time() - start_time}')

if __name__ == '__main__':
    main()