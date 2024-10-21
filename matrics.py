import numpy as np

# scalars, vectors, matrices must be the same lengths.
# scalars

s = 5
print(s)

#vectors is either rows or colon
print("vectors.."*5)

v = np.array([5, -2, 4])
print(v)
print(v.shape)
print(v.reshape(3,1)) #reshapes gives an array a new shape, without changing its data. the first the determine it either a row or colon

print("matrices.."*5)
# matrices

m = np.array([[5 ,13, 6, 8], [-3, 0, 15, 80]])
print(m)
print(m.shape) #it returns the shapes dimensions of a variable

s_a = np.array(5)
print(type(s_a))

print("tensorflow.."*5)
#Tensorflow is not different from db array
m1 = np.array([[29, 39, 48], [4, 8, 22]])
m2 = np.array([[40, 85, 72], [-9, 65, 76]])
t = np.array([(m1 * 2) + (m2 * 2)])
print(t)
print(t.shape)

print("transpose.."*5)
#transposing matrices is reshape the matrices and it works like reshape and one dimensions cant be transpose or reshape.
t = np.array([[94, 96, 98], [41, 43, 45]])
print(t.T) #To transposing you use T

print("dot.."*5)
#dot product is use to multiply the row and add the column
xd = np.array([50, 56, 60])
yd = np.array([300, 505, 393])
print(np.dot(xd, yd))

d1 = np.array([[59, 95, 49], [-6, 59, 40], [60, 59, 80]])
d2 = np.array([[40, 95, 45], [90, 59, 48], [33, 59, 30]])
print(np.dot(d1, d2))

#why is linear algebra  1. vectorized code 2. image recognition 3. Dimensionality reduction

a1 = np.arange(24, dtype=float).reshape(2, 3, 4)
print(a1[1])