# class Animal:
#     def hallo(self):
#         print("Hai hai")
#
# class Dog(Animal):
#     def hallo(self):
#         print("Hai guys")
#
# class Cat(Animal):
#     def hallo(self):
#         print("Hai guys cat")
#
# def main(x):
#     x.hallo()
#
# a = Dog()
# b = Cat()
# d = Dog()
#
# main(a)
# main(b)
# main(d)


# class BMW:
#     def hai(self,price):
#         print(f"amount of car price is {price}")
#
# class Benz:
#     def hai(self,price):
#         print(f"amount of car price is {price}")
#
# class Audi:
#     def hai(self,price):
#         print(f"amount of car price is {price}")
#
# def main(x,amount):
#     x.hai(amount)
#
# a = Audi()
# b = Benz()
# c = BMW()
#
# main(a,29)
# main(b,239)
# main(c,259)




#banking system

class Bank:
    def hai(self):
        pass

class Balance:
    def hai(self,balance):
        print(f" balance {balance}")

class Deposit():
    def hai(self,balance):
        print(f" deposited {balance}")

class Withdraw():
    def hai(self,balance):
        print(f" withdrawn {balance}")


a = int(input("Enter the balance amount:"))
b = int(input("Enter the amount of deposit:"))
c = int(input("Enter the amount of withdraw:"))

def main(x,y):
    x.hai(y)

i = Balance()
j = Deposit()
k = Withdraw()

main(i,a)
main(j,a-b)
main(k,(a-b)-c)

