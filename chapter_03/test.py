import numpy as np
import matplotlib.pyplot as plt

def chance_of_collision(N,k):
    print('Now working on', N,k)
    fact = np.math.factorial
    numer = fact(N) / fact(N-k)
    denom = pow(N, k)
    print('denom at', denom)

    return 1 - numer/denom

# A and B contain the same numbers. astype(int) bc linspace returns floats
A = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100]
B = np.linspace(1, 100, 10).astype(int)

print([pow(100, k) for k in A])
print([pow(100, k) for k in B])
print([A[i] == B[i] for i in range(len(B))])
