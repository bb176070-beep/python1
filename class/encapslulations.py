# class Ecap:
#     def __init__(self, account_number,balance):
#         self.__account_number = account_number
#
#         self.balance = balance
#
#     def print_ac(self):
#         print(self.account_number)
#
# obj=Ecap(45,100)
# print(obj.balance)
# obj.print_ac()
#
#
# class BankAccount:
#     def __init__(self,balance,name,age):
#         self.balance = balance
#         self.name = name
#         self.__age = age
#
#     def age(self):
#         print("Your age is",self.__age)
#
# account = BankAccount(100,"hgfghfg",18)
# print(account.name)
# print(account.balance)
# account.age()






class Library:
    def __init__(self, books):
        self.books = books

    def store_book(self):
        print("Library books:", self.books)


class AddBook(Library):
    def __init__(self, books, new_book):
        super().__init__(books)
        self.__new_book = new_book

    def store_book(self):
        self.books.append(self.__new_book)
        print("Book added:", self.__new_book)


class RemoveBook(Library):
    def __init__(self, books, remove_book):
        super().__init__(books)
        self.__remove_book = remove_book

    def store_book(self):
        if self.__remove_book in self.books:
            self.books.remove(self.__remove_book)
            print("Book removed:", self.__remove_book)
        else:
            print("Book not found")


books = ["Hadi", "Hai", "C"]

print("Available books:", books)

new_book = input("Enter the book to add: ")
add = AddBook(books, new_book)
add.store_book()

remove_book = input("Enter the book to remove: ")
remove = RemoveBook(books, remove_book)
remove.store_book()


print("Final books:", books)

