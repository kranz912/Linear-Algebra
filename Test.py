
from LinearAlgebra import Vectors
vector = Vectors()

a = [3,5]
b = [6,5]

## test add
assert vector.add(a,b) == [9,10]

## test subtract
assert  vector.subtract(a,b) == [-3,0]

## test add_multiple vectors
assert vector.add_multiple([a,b]) == [9,10]

## test scalar_multiply
assert  vector.scalar_multiply(10,a) == [30,50]

## test mean
assert vector.mean([a,b,a,b,b,b]) ==  [5.0,5.0]

## test dot
assert vector.dot(a,b) ==  43

## test sum_of_squares
assert vector.sum_of_squares(a) == 34

## test magnitude
assert vector.magnitude(a) == 5.830951894845301

## test distance
assert vector.distance(a,b) == 3
