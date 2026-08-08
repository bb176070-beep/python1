# class H:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def poly(self):
#         print(self.name,self.age)
#
# class B:
#     def __init__(self,price,total):
#         self.price=price
#         self.total=total
#
#     def poly(self):
#         print(self.price,self.total)
#
# obj=H("aa",12)
# obj1=B(12,289)
#
# obj.poly()
# obj1.poly()
#
#
#


# class A:
#     def hai(self):
#         return "hallo"
#
# class B(A):
#     def hai(self):
#         return "hallo  hai"
#
# class C(A):
#     def hai(self):
#         return "hallo  world"
#
#
# a1 =A()
# a2 = B()
# a3 = C()
#
# print(a1.hai())
# print(a2.hai())
# print(a3.hai())



# #banking system
#
# class Bank:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def transaction(self, amount):
#         pass
#
#     def transaction_2(self, amount2):
#         pass
#
#     def display(self):
#         print(f"{self.name} balance = {self.balance}")
#
# class Deposit(Bank):
#     def transaction(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}")
#
#
# class Withdraw(Bank):
#     def transaction_2(self, amount2):
#         if amount2 <= self.balance:
#             self.balance -= amount2
#             print(f"Withdrawn {amount2}")
#         else:
#             print("Insufficient balance")
#
# a = int(input("Enter the balance amount:"))
# b = int(input("Enter the amount of deposit:"))
# c = int(input("Enter the amount of withdraw:"))
#
# obj1 = Deposit("Hadi", a)
# obj2 = Withdraw("Hadi", a)
#
# accounts = [obj1, obj2]
#
# for x in accounts:
#     x.transaction(b)
#     x.transaction_2(c)
#     x.display()





class Library:
    def __init__(self, books):
        self.books = books

    def store_book(self):
        print("Library books:", self.books)


class AddBook(Library):
    def __init__(self, books, new_book):
        super().__init__(books)
        self.new_book = new_book

    def store_book(self):
        self.books.append(self.new_book)
        print("Book added:", self.new_book)


class RemoveBook(Library):
    def __init__(self, books, remove_book):
        super().__init__(books)
        self.remove_book = remove_book

    def store_book(self):
        if self.remove_book in self.books:
            self.books.remove(self.remove_book)
            print("Book removed:", self.remove_book)
        else:
            print("Book not found")


books = ["Python", "Java", "C"]

print("Available books:", books)

new_book = input("Enter the book to add: ")
add = AddBook(books, new_book)
add.store_book()

remove_book = input("Enter the book to remove: ")
remove = RemoveBook(books, remove_book)
remove.store_book()

print("Final books:", books)

