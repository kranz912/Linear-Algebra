
from LinearAlgebra import Vectors
vector = Vectors()

a = [3,5]
b = [6,5]

## test add
assert vector.add(a,b) == [9,10]


## test subtract

assert  vector.subtract(a,b) ==[-3,0]


## test add_multiple vectors
assert vector.add_multiple([a,b])== [9,10]


## test scalar_multiply
assert  vector.scalar_multiply(10,a) == [30,50]
