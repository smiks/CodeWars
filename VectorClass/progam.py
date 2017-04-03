class Vector:

  @staticmethod
  def error():
      raise ValueError("Invalid dimensions");

  def __init__(self, v):
      self.v = v

  def add(self, v2):
      if len(self.v)!= len(v2.v):
          return Vector.error()
      return Vector([i+j for i,j in zip(self.v, v2.v)])

  def subtract(self, v2):
      if len(self.v)!= len(v2.v):
          return Vector.error()
      return Vector([i-j for i,j in zip(self.v, v2.v)])

  def dot(self, v2):
      if len(self.v)!= len(v2.v):
          return Vector.error()
      return sum(i*j for i,j in zip(self.v, v2.v))

  def norm(self):
      return sum(i**2 for i in self.v)**0.5

  def equals(self, v2):
      return all(i==j for i,j in zip(self.v, v2.v))

  def __str__(self):
      tmp = "("
      for i in self.v:
          tmp += "{0}," . format(i)
      return tmp.strip(",")+")"


a = Vector([1,2,3])
b = Vector([3,4,5])
c = Vector([5,6,7,8])
#a.add(b) # should return Vector([4,6,8])
#a.subtract(b) # should return Vector([-2,-2,-2])
#a.dot(b) # should return 1*3+2*4+3*5 = 26
#a.norm() # should return sqrt(1^2+2^2+3^2)=sqrt(14)
#a.add(c) # raises an exception