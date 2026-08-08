# class MyClass:
#     x = 5
# obj = MyClass()
# print(obj.x)

# class Person:
#     def __init__(self):
#         self.name = "hadhi"
#         self.age = 78
# p1 = Person()
# p2 = Person()
# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# obj = Person("hadhi", 18)
# obj2 = Person("hallo", 198)
# print(obj.name)
# print(obj.age)
# print(obj2.name)
# print(obj2.age)



# class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #
# #     def displayyyyy(self):
# #         print("my name is ",self.name)
# #         print("my age is ",self.age)
# #
# # obj = Person("hadhi", 18)
# # obj.displayyyyy()
# #
# # obj1= Person("hadhiiiiiiiii", 18)
# # obj1.displayyyyy()

# class hello:
#     def __init__(self,lenght ,breadth):
#         self.lenght=lenght
#         self.breadth=breadth
#         self.total=self.lenght*self.breadth
#
#     def display(self):
#         print(self.total)
#
# obj = hello(10,5)
# obj.display()

# class bank:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#     def display(self):
#         print(self.balance)
#         print(self.name)
#         choices = 0
#         balance = (self.balance)
#         while choices != 4:
#             print("1.Check Balance")
#             print("2.Deposit money")
#             print("3.withdraw money")
#             print("4.Exit")
#             choice = int(input("Enter your choice: "))
#             choices = choice
#             if choice == 1:
#                 print("1.your balance is: ", balance)
#             elif choice == 2:
#                 if balance > 0:
#                     amount = int(input("Enter amount you want to deposit: "))
#                     balance += amount
#                     print(f" 2.your deposit {amount} is successfully deposited")
#                     print("Your balance is: ", balance)
#             elif choice == 3:
#                 if balance > 0:
#                     amount = int(input("Enter amount you want to withdraw: "))
#                     balance -= amount
#                     print(f" 3.your withdrawal {amount} is successfully withdrawn")
#                     print("Your balance is: ", balance)
#             elif choice == 4:
#                 print("exit")
#                 break
#
#             else:
#                 print("Enter a valid choice")
# obj = bank("hadi",10000)
# obj.display()


# class bank:
#     def __init__(self,name,balance,deposit,withdraw):
#         self.name = name
#         self.balance = balance
#         self.deposit = deposit
#         self.total_deposit = self.balance + self.deposit
#         self.withdraw = withdraw
#
#
#     #balance
#     def balance_up(self,new_bal):
#
#         if new_bal > 0:
#             self.balance = new_bal
#         else:
#             # while new_bal < 0:
#             #     print("error balance")
#             #     bank1.balance_up(int(input("enter your current balance:-")))
#
#             print("not correct balance")
#
#
#
#
#     #name
#     def name_up(self,new_name):
#         self.name = new_name
#
#     #deposit
#     def deposit_up(self,new_des):
#         if self.balance > 0:
#             self.deposit = new_des + self.balance
#         else:
#             print("invalid balance")
#
#
#     #updated bal
#
#     #withdraw
#     def withdraw_up(self,new_withd):
#         if self.balance > 0:
#             self.withdraw = self.deposit - new_withd
#         else:
#             print("invalid balance")
#
#
#     #display case
#     #balance
#     def display_balance(self):
#         print(f"Your current balance is {self.balance}")
#
#     #name
#     def display_name(self):
#         print(f"Your name is {self.name}")
#
#     #deposit
#     def display_deposit(self):
#         print(f"total deposited balance is  {self.deposit}")
#
#
#
#     #withdraw
#     def display_withdraw(self):
#         print(f"Your withdraw is {self.withdraw}")
#
#
# #updated case
# bank1 = bank("",0,0,0)
#
# #balance
# bank1.balance_up(int(input("enter your current balance:-")))
# bank1.display_balance()
#
# #name
# bank1.name_up(str(input("enter your new name:-")))
# bank1.display_name()
#
# #deposit
# bank1.deposit_up(int(input("enter your new deposit:-")))
# bank1.display_deposit()
#
#
# #withdraw
# bank1.withdraw_up(int(input("enter your new withdraw:-")))
# bank1.display_withdraw()



#1)impliment  libary management system that allow added book and borrowing book returning books displaying available books
#2)impliment a movie ticket booking system that allows booking tickets and canceling tickets checking seat availablility

#1)impliment  libary management system that allow added book and borrowing book returning books displaying available books
# class libary:
#     def __init__(self):
#         self.book = []
#         # self.add_book = add_book
#         # self.borrow_book = []
#         # self.return_book = []
#
#     #add book
#     def add_book(self,new_book):
#         self.book.append(new_book)
#
#     def remove_book(self,remove_book):
#         if remove_book in self.book:
#             self.book.remove(remove_book)
#         else:
#             print("book not found")
#
#     def return_book(self,return_book):
#         # if return_book in self.book:
#             self.book.append(return_book)
#
#     #books
#     def display_book(self):
#         print(f"your books are :-  {self.book}")
#     #add books
#     def display_add_books(self):
#         print(f"your books are :-  {self.add_book}")
#
#     #romove book
#     def display_remove_books(self):
#         print(f"your books are :-  {self.remove_book}")
#
#     #return book
#     def display_return_book(self):
#         print(f"your books are :-  {self.return_book}")
#
# libary1 = libary()
# #books
# libary1.display_book()
#
# #add books
# libary1.add_book("k")
# libary1.add_book("j")
# libary1.add_book("p")
#
# libary1.display_book()
#
#
# #remove case
# libary1.remove_book(str(input("enter your remove book name :")))
# libary1.display_book()
#
# #retrurn book
# libary1.return_book(str(input("enter your return book name :")))
# libary1.display_book()
#
# libary1.add_book(str(input("enter your adding book : ")))
#
# libary1.display_add_books()

#order book


#
# class Animal:
#     def __init__(self, species, sound):
#         self.species = species
#         self.sound = sound
#
#     def make_sound(self):
#         print(f"the {self.species} is making sound{self.sound}")
# class Dog(Animal):
#     pass
#
# x = Dog("hallo", "cat")
# x.make_sound()
# x.make_sound()




#2)impliment a movie ticket booking system that allows booking tickets and canceling tickets checking seat availablility
# class movieticket:
#     def __init__(self):
#         self.tickets = []
#
#
#     def add_ticket(self, new_ticket):
#         self.tickets.append(new_ticket)
#
#     def remove_ticket(self, remove_ticket):
#         if remove_ticket in self.tickets:
#             self.tickets.remove(remove_ticket)
#         else:
#             print("ticket not have")
#
#     def return_tickets(self,return_ticket):
#         self.tickets.append(return_ticket)
#
#
#
#     def display_tickets(self):
#         print(f"your tickets are: {self.tickets}")
#
#     def display_add_tickets(self):
#         print(f"your tickets are: {self.tickets}")
#
#     def display_remove_tickets(self):
#         print(f"your tickets are: {self.tickets}")
#
#     def display_return_tickets(self):
#         print(f"your tickets are: {self.tickets}")
#
#
# ticket = movieticket()
#
# ticket.display_tickets()
#
# ticket.add_ticket(1)
# ticket.add_ticket(2)
# ticket.add_ticket(3)
# ticket.add_ticket(4)
#
# ticket.display_tickets()
#
# ticket.remove_ticket(int(input("enter the remove ticket number: ")))
# ticket.display_tickets()
#
# ticket.return_tickets(int(input("enter the  return ticket number")))
# ticket.display_tickets()
#
# ticket.add_ticket(int(input("enter the add ticket number:")))
# ticket.display_add_tickets()

# class animal:
#     def __init__(self, species, sound):
#         self.species = species
#         self.sound = sound
#
#     def make_sound(self):
#         print(f"the {self.species} goes '{self.sound}'")
#
# class cat(animal):
#     pass
#
# x = cat("cat", "moew")
# x.make_sound()

# class animal:
#     def __init__(self, species, sound):
#         self.species = species
#         self.sound = sound
#
#     def describe(self):
#         print(f"the {self.species} is '{self.sound}'.")
#
# class cat(animal):
#     def __init__(self, species, sound):
#         animal.__init__(self, species, sound)
#
# x = cat("cat", "cat")
# x.describe()
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def hallo(self):
#         print(self.name, self.age)
#
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
# x = Student("John", 18)
# x.hallo()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(self.name, self.age)
#
# class Student(Person):
#     def __init__(self, name, age,year):
#         super().__init__(name, age)
#         self.score = year
#
# x = Student("hadi",23,5009)
# print(x.score)

#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(self.name, self.age)
#
# class Student(Person):
#     def __init__(self, name, age,year):
#         super().__init__(name, age)
#         self.score = year
#
#     def welcome(self):
#         print("welcome",self.name, self.age,"to the class of ", self.score)
#
# x = Student("John",22,2020)
# x.welcome()




# class bank:
#     def __init__(self,name,balance,deposit,withdraw):
#         self.name = name
#         self.balance = balance
#         self.deposit = deposit
#         self.withdraw = withdraw
#
#     def name_h(self,new_name):
#         self.name = new_name
#
# class second_bank(bank):
#     def __init__(self,name,balance,deposit,withdraw):
#         super().__init__(name,balance,deposit,withdraw)
#
#
#     def balance_h(self, new_balance):
#         if new_balance > 0:
#             self.balance = new_balance
#
#         else:
#             print(f"Balance Error{self.balance}")
#
#     def deposit_h(self, new_deposit):
#         self.deposit = new_deposit
#         if self.balance > 0:
#             self.balance += new_deposit
#
#         else:
#             print(f"Balance Error{self.balance}")
#
#
#     def withdraw_h(self, new_withdraw):
#         self.withdraw = new_withdraw
#         if self.balance > 0:
#             self.balance -= new_withdraw
#
#         else:
#             print(f"Balance Error{self.balance}")
#
#     def display_balance(self):
#         print(f"your balance is {self.balance}")
#
#     def display_name(self):
#         print(f"your name is {self.name}")
#
#     def display_deposit(self):
#         print(f"your deposit is {self.deposit}")
#
#     def display_withdraw(self):
#         print(f"your withdraw is {self.withdraw}")
#
#
# # updated case
# bank1 = second_bank("", 0, 0, 0)
#
# # balance
# bank1.balance_h(int(input("enter your current balance:-")))
# bank1.display_balance()
#
# # name
# bank1.name_h(str(input("enter your new name:-")))
# bank1.display_name()
#
#     # deposit
# bank1.deposit_h(int(input("enter your new deposit:-")))
# bank1.display_deposit()
# bank1.display_balance()
#
# # withdraw
# bank1.withdraw_h(int(input("enter your new withdraw:-")))
# bank1.display_withdraw()
# bank1.display_balance()




# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info_1(self):
#         print(self.name, self.age)
#
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
# x = Student("nakk", 18)
# x.print_info_1()



#
# class hallo1:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def print_info_2(self):
#         print(self.name, self.age)
#
# class hallo2(hallo1):
#     def __init__(self, name, age,place):
#         super().__init__(name, age)
#         self.new_1 = place
#
#     def print_info_3(self):
#         print("this is your place",self.new_1)
#
# class hallo3(hallo2):
#
#     def print_info_4(self):
#         print("this is your place:-",self.new_1,"\nname is :-",self.name,"\nage is :-",self.age)
#
#
# x = hallo3("nakk", 18, "india")
# x.print_info_4()


#multi inheritance
# class circle:
#     def __init__(self, radius,pi):
#         self.radius = radius
#         self.pi = pi
#         self.area = self.radius*self.radius*self.pi
#
#     def areas(self):
#         print(self.area)

# class triangle:
#
#     def __init__(self, len, brdth):
#         self.len = len
#         self.brdth = brdth
#         self.area = len * brdth
#     def area1(self):
#         print(self.area)
#
# class hallo(triangle):
#
#     def area_to(self):
#         print("area is ",self.area)
# a = int(input("enter the number of lenght: "))
# b = int(input("enter the side length: "))
# x = hallo(a,b)
# x.area_to()
#
# print("\n")
#
# class circle:
#     def __init__(self, radius,pi):
#         self.radius = radius
#         self.pi = pi
#         self.areas = radius * radius * pi
#     def area(self):
#         print(self.areas)
#
# class first(circle):
#
#     def area_j(self):
#         print("area :-  ",self.areas)
# v = int(input("enter the number of radius: "))
# c = first(v,3.14)
# c.area_j()



#
# class rectangle:
#     def __init__(self,side1,side2):
#         self.side1 = side1
#         self.side2 = side2
#
#     def area(self):
#         print(self.side1,self.side2)
#
# class rectangle_1(rectangle):
#     def __init__(self,side1,side2):
#         super().__init__(side1,side2)
#         self.area = side1*side2
#
# class rectangle_2(rectangle_1):
#
#     def printarea(self):
#         print("area is :-  ",self.area)
#
# x = rectangle_2(8,2)
# x.printarea()


#multiple inheritance
# class rectangle:
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#
#     def area(self):
#         print("\nrectangle:-  ",self.length*self.breadth)
#
# class circle:
#     def __init__(self,radius,pi):
#         self.radius = radius
#         self.pi = pi
#         self.circle_area = self.pi*self.radius**2
#
#     def area_circle(self):
#         print("\ncircle:-  ",self.circle_area)
#
# class total(rectangle,circle):
#     def __init__(self,length,breadth,radius,pi):
#         rectangle.__init__(self,length,breadth)
#         circle.__init__(self,radius,pi)
#
# x = total(10,10,10,10)
# x.area()
# x.area_circle()



# #multiple level
# class rectangle:
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#
#     def area(self):
#         print("\nrectangle:-  ",self.length*self.breadth)
#
# class circle(rectangle):
#     def __init__(self,radius,pi,length,breadth):
#         super().__init__(length,breadth)
#         self.radius = radius
#         self.pi = pi
#
#     def area_circle(self):
#         print("\ncircle:-  ",self.pi*self.radius**2)
#
# class total(circle):
#     pass
# a = int(input("enter the radius:"))
# b = int(input("enter the breadth:"))
# c = int(input("enter the length:"))
# x= total(a,3.14,c,b)
# x.area()
# x.area_circle()







