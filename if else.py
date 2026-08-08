# a=19
# # if a>=18:
# #     print("elg")
# #
# # elif a:
# #     print()
# # else:
# #     print("not")
#
# #1) write a prgram to check this give character is vowel or not
#
# #2) write a program check entered the number is divisible by 7 or not
#
# #3) write a program to check the given number even or odd
#
# #1)
# # a = "a"
# # b = ["a","e","i","o","u"]
# # if a in b:
# #     print("it is vowel")
# # else:
# #     print("not vowel")
#
#
# #2)
# a = int(input("enter the number:"))
# if a % 7 ==0 :
#     print("it can divisible by 7")
# else :
#     print("not")
#
# #3) write a program to check the given number even or odd
# a = 10
# if a % 2 ==0 :
#     print("\n","it is even")
# else :
#     print("it is odd")




#4)grade system
#
# a = int(input("enter the number:"))
# if a >= 90 :
#     print("\n","a grade")
# elif a >= 80 :
#     print("\n","b grade")
# elif a >= 70 :
#     print("\n","c grade")
# else:
#     print("\n","d grade")


#5) write a program to check whether a number is 3 digit or not
#6)largest among three numbers


#5) write a program to check whether a number is 3 digit or not
# a = int(input("enter the number:"))
# if a >= 100 and a < 1000:
#     print("\n","it is 3 digits")
# elif a >= 10 and a <99:
#     print("\n","it is not a 3 digit")
# elif a >=1 and a < 9:
#     print("\n","it is not a 3 digits")
# else:
#     print("\n","it is not a 3 digits")




#write a program to accept 3 number and display accending order



#
# 6)largest among three numbers
# a = int(input("enter the number:"))
# b = int(input("enter the number:"))
# c = int(input("enter the number:"))
#
# if a > b and a > c:
#     print("\n","a is largest number")
# elif b > a and b > c:
#     print("\n","b is largest number")
# else:
#     print("\n","c is largest number")


#8)write a program to accept 3 number and display accending order

a = int(input("enter the number:"))
b = int(input("enter the number:"))
c = int(input("enter the number:"))

z = a,b,c
k = b,a,c
v = c,b,a
m = a,c,b
n = b,c,a
d = c,a,b


if a < b and b < c:
    print("\n",list(z),"\nit is accending order")
elif b < a and a < c:
    print("\n",list(k),"\nit is accending order")
elif c < b and b < a:
    print("\n",list(v),"\nit is accending order")
elif a < c and c < b:
    print("\n",list(m),"\nis not an accending order")
elif b < c and c < a:
    print("\n", list(n), "\nis not an accending order")
elif c < a and a < b:
    print("\n", list(d), "\nis not an accending order")
else:
    print("\n","\nis not an descending order")
