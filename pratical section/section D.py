#1)electric bill
# electric_bill = int(input("enter unit of eletricity:"))
# if electric_bill > 200 :
#     c = electric_bill - 200
#     d = c * 10
#     print(d)
# elif electric_bill > 100 and electric_bill <=200 :
#     b = electric_bill - 100
#     e = b * 5
#     print(e)
# else :
#     print("no charge")
from random import choice

#5) student result system
# a = int(input("negter the number"))
# if  a>= 90 and a<= 100:
#     print("A")
# elif a>= 80 and a<= 89:
#     print("B")
# elif a>= 70 and a<= 79:
#     print("C")
# elif a>= 60 and a<= 69:
#     print("D")
# else:
#     print("fail")

#2)ATM

# print("************** ATM MENU **************")
# balance = 10000
# choice_for_while = 0
# while choice_for_while != 4:
#     print("1.Check Balance")
#     print("2.Deposit money")
#     print("3.withdraw money")
#     print("4.Exit")
#     choice = int(input("Enter your choice: "))
#     choice_for_while = choice
#     if choice == 1:
#         print("1.your balance is: ",balance)
#         print("***************************************")
#     elif choice == 2:
#         if balance > 0:
#             amount = int(input("Enter amount you want to deposit: "))
#             balance += amount
#             print(f" 2.your deposit {amount} is successfully deposited")
#             print("Your balance is: ",balance)
#             print("***************************************")
#         else:
#             print("try again")
#     elif choice == 3:
#         amount = int(input("Enter amount you want to withdraw: "))
#         balance -= amount
#         print(f" 3.your withdraw {amount} is successfully")
#         print("Your balance is: ",balance)
#         print("***************************************")
#     elif choice == 4:
#         print("Exited")
#         print("thank you !")
#         print("****************************************")
#
#     else:
#         print("*******************")
#         print("! invalid choice !")
#         print("*******************")

#3)
import random
random_generated_number = random.randint(1, 100)
trying = 0
while True:
    enter_num = int(input("Enter a number: "))
    trying += 1
    if enter_num > random_generated_number:
        print('Try Again it is "too high" !')
    elif enter_num < random_generated_number:
        print('Try Again it is "too low" !')
    else:
        print("*****************************")
        print(f'it is "correct" {enter_num}')
        print("victory")
        print("*****************************")
#4)strong password

# print("***********************************")
# enter_pass=str(input("enter password:"))
# while enter_pass!="hadhi":
#     print("enter password not correct")
#     enter_pass=str(input("enter password"))
# print(" correct")
# print("***********************************")



