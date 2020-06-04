from functools import reduce
from math import sqrt
class Vectors(object):
    def __init__(self):
        pass

    def add(self,a,b):
        return [a_i + b_i for a_i,b_i, in zip(a,b)]

    def add_multiple(self,vectors):
        return reduce(self.add,vectors)

    def subtract(self,a,b):
        return [a_i - b_i for a_i,b_i in zip(a,b)]

    def scalar_multiply(self,c,a):
        return [c*a_i for a_i in a]

    def mean(self,vectors):
        n = len(vectors)
        return self.scalar_multiply(1/n, self.add_multiple(vectors))

    def dot(self,a,b):
        return sum(a_i*b_i for a_i, b_i in zip(a,b))

    def sum_of_squares(self, a):
        return self.dot(a,a)

    def magnitude(self,a):
        return sqrt(self.sum_of_squares(a))

    def distance(self,a,b):
        return self.magnitude(self.subtract(a,b))
