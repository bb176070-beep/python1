# from abc import ABC, abstractmethod
# class animal(ABC):
#   @abstractmethod
#   def train(self):
#     pass
#   @abstractmethod
#   def train7(self):
#     pass
# class dog(animal):
#
#   def train(self):
#     print("tr")
#   def train7(self):
#     print("truck ")
#
# s1 = dog()
# s1.train()
# s1.train7()



# from abc import ABC, abstractmethod
#
# import math
#
# class Area(ABC):
#     def __init__(self,length,breadth,radius):
#         self.length = length
#         self.breadth = breadth
#         self.radius = radius
#     @abstractmethod
#     def area(self):
#         pass
#
# class rectangle(Area):
#     def area(self):
#         return self.length * self.breadth
#
# class cicle(Area):
#     def area(self):
#         return self.radius * math.pi * self.radius
#
#
#
# triangle = rectangle(3,4)
# print(triangle.area())
#
# hai = cicle(5)
# print(hai.area())
