# class India:
#     def hallo(self):
#         pass
#
# class Kerala(India):
#     def hallo(self):
#         print("hai i am here")
#
# class Goa(India):
#     def hallo(self):
#         print("hai i am in goa")
#
# obj = [Kerala(),Goa()]
# for x in obj:
#     x.hallo()

# class Car:
#     def hai(self,num):
#         print(f"number is {num}")
#
# class Bike:
#     def hai(self,num):
#         print(f"number of bike is {num}")
#
# class Truck:
#     def hai(self,num):
#         print(f"number of truck is {num}")
#
# Vehicles = [
#     (Car(),67),
#     (Bike(),456),
#     (Truck(),4996)
# ]
# for x,num in Vehicles:
#     x.hai(num)


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



accounts = [
    (Balance(),a),
    (Deposit(),a-b),
    ( Withdraw(),(a-b)-c),
]

for x,balance in accounts:
    x.hai(balance)

