import numpy as np

# Program 9: 5x4 arrays and arithmetic operations
a = np.random.randint(1, 10, (5, 4))
b = np.random.randint(1, 10, (5, 4))

print("Array A:\n", a)
print("Array B:\n", b)

print("\nAddition:\n", a + b)
print("Mean of A:", a.mean(), "Std of B:", b.std())
