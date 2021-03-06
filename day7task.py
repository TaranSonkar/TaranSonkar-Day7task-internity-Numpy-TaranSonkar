# -*- coding: utf-8 -*-
"""Day7task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VcvftOnWektAxoVNYhnEt4FZoGwTiDT2
"""

#Linear Algebra with numpy

'''The Linear Algebra module of NumPy offers various methods to apply linear algebra on any numpy array.
One can find:
rank, determinant, trace, etc. of an array.
eigen values of matrices.
matrix and vector products (dot, inner, outer,etc. product), matrix exponentiation.
solve linear or tensor equations and much more!'''

import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9])
a.mean()

#output=5.0

np.mean(a)

#output=5.0

a.sum()

#output=45

a.min()

#output=1

a.max()

#output=9

a.var()   #16+9+4+1+0+1+4+9+16/9

#output=6.666666666666667

a.std()

#output=2.581988897471611

a.cumsum()

#output=array([ 1,  3,  6, 10, 15, 21, 28, 36, 45])

a = np.arange(25)
a = a.reshape((5,5))
a

#output==array([[ 0,  1,  2,  3,  4],
'''[ 5,  6,  7,  8,  9],
[10, 11, 12, 13, 14],
[15, 16, 17, 18, 19],
[20, 21, 22, 23, 24]])'''

a.mean(axis=0)

#output=array([10., 11., 12., 13., 14.])

a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
a1


#output=
'''array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]'''

a2

#output=a2

a1.dot(a2)


#output=
'''array([[ 30,  36,  42],
       [ 66,  81,  96],
       [102, 126, 150]])'''

np.dot(a1,a2)

#output==array([[ 30,  36,  42],
#[ 66,  81,  96],
#[102, 126, 150]])

from numpy.linalg import det, inv, eig

a = np.arange(16).reshape((4,4))

a

#output=array([[ 0,  1,  2,  3],
#[ 4,  5,  6,  7],
#[ 8,  9, 10, 11],
#[12, 13, 14, 15]])

a * 2

#output==array([[ 0,  2,  4,  6],
#[ 8, 10, 12, 14],
#[16, 18, 20, 22],
#[24, 26, 28, 30]])

det(a)

#output=0.0

eig(a)

'''output==(array([ 3.24642492e+01, -2.46424920e+00,  2.55670932e-15, -1.93389056e-16]),
 array([[-0.11417645,  0.7327781 , -0.54471271,  0.09683789],
        [-0.3300046 ,  0.28974835,  0.76902356,  0.27269982],
        [-0.54583275, -0.15328139,  0.09609099, -0.8359133 ],
        [-0.76166089, -0.59631113, -0.32040185,  0.46637559]]))'''

np.inner(a1,a2)

#output==array([[ 14,  32,  50],
#[ 32,  77, 122],
#[ 50, 122, 194]])

np.outer(a1,a2)

#output==
'''array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9],
       [ 2,  4,  6,  8, 10, 12, 14, 16, 18],
       [ 3,  6,  9, 12, 15, 18, 21, 24, 27],
       [ 4,  8, 12, 16, 20, 24, 28, 32, 36],
       [ 5, 10, 15, 20, 25, 30, 35, 40, 45],
       [ 6, 12, 18, 24, 30, 36, 42, 48, 54],
       [ 7, 14, 21, 28, 35, 42, 49, 56, 63],
       [ 8, 16, 24, 32, 40, 48, 56, 64, 72],
       [ 9, 18, 27, 36, 45, 54, 63, 72, 81]])'''

np.sin(30)

#output==-0.9880316240928618

a = np.array([[1,2],[4,5]])
a2 = np.array([1,2])

np.linalg.solve(a,a2)

#output==
#array([-0.33333333,  0.66666667])

###########################################################################################################################

#Vectorized Operations in NumPy

'''The concept of vectorized operations on NumPy allows the use of more optimal and pre-compiled
functions and mathematical operations on NumPy array objects and data sequences.
The Output and Operations will speed-up when compared to simple non-vectorized operations.
Using vectorized sum method on NumPy array.
We will compare the vectorized sum method along with simple non-vectorized operation i.e the iterative method to calculate the sum of numbers.'''

# Commented out IPython magic to ensure Python compatibility.
import timeit
import math
print("Time taken by vectorized sum : ", end = "")
print(np.sum(np.arange(15000)))
# %timeit np.sum(np.arange(15000))

'''output==Time taken by vectorized sum : 112492500
The slowest run took 11.28 times longer than the fastest. This could mean that an intermediate result is being cached.
10000 loops, best of 5: 25 ??s per loop'''

# Commented out IPython magic to ensure Python compatibility.
# non-vectorized operation
print("Time taken by non-vectorized operation : ", end = "")
# %timeit [math.exp(item) for item in range(150)]

#output==Time taken by non-vectorized operation : 10000 loops, best of 5: 20.9 ??s per loop

####################################################################################################################################

#universal Function

a = np.array([3,2,5,8,7,3,4,9])
a

#output--array([3, 2, 5, 8, 7, 3, 4, 9])

a.sort()
a

#output--array([2, 3, 3, 4, 5, 7, 8, 9])

np.square(a)

#output--array([ 4,  9,  9, 16, 25, 49, 64, 81])

a2 = np.square(a)
a2

#output--array([ 4,  9,  9, 16, 25, 49, 64, 81])

np.sqrt(a2)

#output--array([2., 3., 3., 4., 5., 7., 8., 9.])

np.abs([-1,-2,-3])

#output--array([1, 2, 3])

a1 = np.array([1,2,3,4])
a2 = np.array([5,6,7,8])
np.add(a1,a2)

#output--array([6, 8, 10, 12])

a1 + a2

np.subtract(a2,a1)

#output--array([4, 4, 4, 4])

np.maximum(a1,a2)

#output--array([5, 6, 7, 8])

a3 = np.array([9,2,3,9])
a4 = np.array([5,6,7,8])

np.maximum(a3,a4)

#output--array([9, 6, 7, 9])

np.minimum(a3,a4)

#output--array([5, 2, 3, 8])

np.power(a1,a2)

#output--array([    1,    64,  2187, 65536])

np.greater(a1,a2)

#output--array([False, False, False, False])

np.less(a3,a4)

#output--array([False,  True,  True, False])

np.log(30)

#OUTPUT--3.4011973816621555

######################################################################################################################

#Broadcasting and shape manipulation

#Broadcasting

'''broadcasting allows us to do the arithmetic operations on arrays of different shape or size'''

a=np.array([[2,3],[4,5],[6,7]])
a

b=np.array([2,3,4])
c=np.array([20,30])
a.shape

c.shape

a+c

a+b

#ValueError: operands could not be broadcast together with shapes (3,2) (3,)

#manipulation

np.size(a)

#output-6

a = np.arange(16)
a

#output--array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])

a1 = a.reshape((4,4))
a1

#output---array([[ 0,  1,  2,  3],
#[ 4,  5,  6,  7],
#[ 8,  9, 10, 11],
#[12, 13, 14, 15]])

a2 = a.reshape((2,8))
a2

#output--array([[ 0,  1,  2,  3,  4,  5,  6,  7],
#[ 8,  9, 10, 11, 12, 13, 14, 15]])

a1.swapaxes(0,1)

#output--array([[ 0,  4,  8, 12],
#[ 1,  5,  9, 13],
#[ 2,  6, 10, 14],
#[ 3,  7, 11, 15]])

################################################################################################################################

#Boolean Mask

'''Every element of the Array A is tested, if it is equal to. The results of these tests are the Boolean elements of the result array.

Of course, it is also possible to check on "<", "<=", ">" and ">=".'''

A = np.array([4, 7, 3, 4, 2, 8])

print(A == 4)

#output---[ True False False  True False False]

print(A < 5)

#output--[ True False  True  True  True False]

B = np.array([[42,56,89,65],
              [99,88,42,12],
              [55,42,17,18]])

print(B>=42)

#output--[[ True  True  True  True]
#[ True  True  True False]
#[ True  True False False]]

##########################################################################################################################################

#Dates and time in numpy

pip install datetime

import datetime

today=np.datetime64('today','D')
today


#output--numpy.datetime64('2021-06-15')

print('June,2021')
print(np.arange('2021-06','2021-07',dtype='datetime64[D]'))

#output--June,2021
'''['2021-06-01' '2021-06-02' '2021-06-03' '2021-06-04' '2021-06-05'
 '2021-06-06' '2021-06-07' '2021-06-08' '2021-06-09' '2021-06-10'
 '2021-06-11' '2021-06-12' '2021-06-13' '2021-06-14' '2021-06-15'
 '2021-06-16' '2021-06-17' '2021-06-18' '2021-06-19' '2021-06-20'
 '2021-06-21' '2021-06-22' '2021-06-23' '2021-06-24' '2021-06-25'
 '2021-06-26' '2021-06-27' '2021-06-28' '2021-06-29' '2021-06-30']'''

print('first sunday in june 2021')
print(np.busday_offset('2021-06',0,roll='forward',weekmask='Sun'))

#output--first sunday in june 2021
#2021-06-06

print(np.busday_count('2021-06','2021-07'))
print('weekdays')

#output--22

##########################################################################################################################
                                    #Day7task-completed-internity-Taran Sonkar
#Date-15/June/2021

