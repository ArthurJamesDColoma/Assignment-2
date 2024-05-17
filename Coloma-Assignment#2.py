import numpy as np

# 1. dot method
print("1. dot method examples:")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[2, 3], [4, 5]])
D = np.array([[1, 0], [0, 1]])

# Example 1: Dot product of A and B
print("Example 1:")
print(np.dot(A, B))

# Example 2: Dot product of A and C
print("Example 2:")
print(np.dot(A, C))

# Example 3: Dot product of B and D
print("Example 3:")
print(np.dot(B, D))

print("\n2. transpose method examples:")
# 2. transpose method
E = np.array([[1, 2, 3], [4, 5, 6]])
F = np.array([[1, 4], [2, 5], [3, 6]])
G = np.array([[0, 1], [1, 0]])

# Example 1: Transpose of E
print("Example 1:")
print(np.transpose(E))

# Example 2: Transpose of F
print("Example 2:")
print(np.transpose(F))

# Example 3: Transpose of G
print("Example 3:")
print(np.transpose(G))

print("\n3. linalg.inv method examples:")
# 3. linalg.inv method
H = np.array([[1, 2], [3, 4]])
I = np.array([[2, 3], [1, 2]])
J = np.array([[4, 7], [2, 6]])

# Example 1: Inverse of H
print("Example 1:")
print(np.linalg.inv(H))

# Example 2: Inverse of I
print("Example 2:")
print(np.linalg.inv(I))

# Example 3: Inverse of J
print("Example 3:")
print(np.linalg.inv(J))

print("\n4. linalg.det method examples:")
# 4. linalg.det method
K = np.array([[1, 2], [3, 4]])
L = np.array([[2, 3], [1, 2]])
M = np.array([[4, 7], [2, 6]])

# Example 1: Determinant of K
print("Example 1:")
print(np.linalg.det(K))

# Example 2: Determinant of L
print("Example 2:")
print(np.linalg.det(L))

# Example 3: Determinant of M
print("Example 3:")
print(np.linalg.det(M))

print("\n5. flatten method examples:")
# 5. flatten method
N = np.array([[1, 2], [3, 4]])
O = np.array([[5, 6], [7, 8], [9, 10]])
P = np.array([[11, 12, 13], [14, 15, 16]])

# Example 1: Flatten N
print("Example 1:")
print(N.flatten())

# Example 2: Flatten O
print("Example 2:")
print(O.flatten())

# Example 3: Flatten P
print("Example 3:")
print(P.flatten())
