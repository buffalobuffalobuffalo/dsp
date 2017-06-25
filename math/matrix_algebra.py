# Matrix Algebra

import numpy as np

#PART 1
#1.1. a = 2x3
#1.2. b = 2x2
#1.3 c = 3x2
#1.4 d = 2x3
#1.5 u = 1x4
#1.6 w = 4x1

#PART 2
#2.1 u + v = [9, 7, -4,, 9]
#2.2 u - v = [3, -3, -2, 1]
#2.3 6u = [36, 12, -18, 30]
#2.4 vdot(u, v) = [18, 10, -3, 20]
#2.5 norm u = sqrt(74)

#PART 3
#3.1 A + C = not defined
#3.2 A + C.transpose = [[-4, -7, -3],[1, 6, 4]]
#3.3 C.transpose + 3D = [[14, 3, 3],[2, 7, 9]]
#3.4

A = [[1, 2, 3], [2, 7, 4]]
B = [[1, -1], [0, 1]]

print np.dot(B,A)

#3.5
At = np.transpose(A)

# print np.dot(A,At)
# answer is undefined
