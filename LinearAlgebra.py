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
