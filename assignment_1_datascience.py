import numpy as np

# Problem 1: Matrix Multiplication
print("Problem 1: Matrix Multiplication (M×N by N×A)")

M = int(input("Enter value M: "))
N = int(input("Enter value N: "))
A = int(input("Enter value A: "))

first_array = np.random.rand(M, N)
second_array = np.random.rand(N, A)
dot_product = np.dot(first_array, second_array)

print("\nFirst array:")
print(np.round(first_array, 8))
print("\nSecond array:")
print(np.round(second_array, 8))
print("\nDot product of two arrays:")
print(np.round(dot_product, 8))


# Problem 2: Character Check in Array
print("\n\nProblem 2: Check if each element is digit, lowercase, or uppercase")

arr = np.array(['Python', 'PHP', 'JS', 'Examples', 'html5', '5'])
digits_only = np.array([x.isdigit() for x in arr])
lower_only = np.array([x.islower() for x in arr])
upper_only = np.array([x.isupper() for x in arr])

print("Original Array:", arr)
print("Digits only =", digits_only)
print("Lower cases only =", lower_only)
print("Upper cases only =", upper_only)


# Problem 3: Subtract Two Arrays
print("\n\nProblem 3: Create and subtract two arrays")

X, Y = map(int, input("Enter values for X and Y (space-separated): ").split())
lst1 = list(range(1, 1 + 16 * X, X))[:16]
lst2 = list(range(1, 1 + 16 * Y, Y))[:16]

np1 = np.array(lst1).reshape(4, 4)
np2 = np.array(lst2).reshape(4, 4)
np3 = np1 - np2

print("\nnp1:")
print(np1)
print("\nnp2:")
print(np2)
print("\nSubtracted result (flattened):")
print(np3.flatten())


# Problem 4: Element-wise subtraction of matrices
print("\n\nProblem 4: Matrix P - Q")

P_values = list(map(int, input("Enter 9 values for matrix P (space-separated): ").split()))
Q_values = list(map(int, input("Enter 9 values for matrix Q (space-separated): ").split()))

P = np.array(P_values).reshape(3, 3)
Q = np.array(Q_values).reshape(3, 3)
result = P - Q

print("\nElement-wise difference (P - Q):")
print(result)
