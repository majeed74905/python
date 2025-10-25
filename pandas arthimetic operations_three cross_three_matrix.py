import numpy as np

# Program 8: 3x3 arrays and arithmetic operations
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[9,8,7],[6,5,4],[3,2,1]])

print("Array A:\n", a)
print("Array B:\n", b)

print("\nAddition:\n", a + b)
print("Subtraction:\n", a - b)
print("Multiplication:\n", a * b)
print("Division:\n", a / b)

print("\nA Sum:", a.sum(), "Mean:", a.mean(), "Std:", a.std())
print("B Sum:", b.sum(), "Mean:", b.mean(), "Std:", b.std())
