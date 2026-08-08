# a=2
# while a<=20:
#     print(a)
#     a+=2
from operator import add

#write a program to print the given series 10 20 ..100
#2)write a program to print first 10 even and first 10 odd numbers
#4)square of first 10 natural numbers
#3)sum of first 10 even numbers

#1)write a program to print the given series 10 20 ..100
# a = 10
# while a <=100:
#     print(a)
#     a+=10

#2)write a program to print first 10 even and first 10 odd numbers
# a = 0
# while a <= 10:
#     print(a)
#     a+= 2

#even
# a =1
# while a <= 10:
#     print(a)
#     a+=2


# 3)sum of first 10 even numbers
# a =2
# c = 0
#
# while a <=20:
#     c+=a
#     a+=2
# print(c)

# 4)square of first 10 natural numbers
# a = 1
# while a <= 10:
#     print(a*a)
#     a+=1

#5)factorial of a number using  while loop
#6)sum of digit of a number using while loop
#7)reverse a number using while loop

#5)factorial of a number using  while loop
# a = 0
# b = 1
# while a < 5:
#     b+=b*a
#     a+=1
# print(b)

#6)sum of digit of a number using while loop
# a = 112
# b = 0
# c = 0
#
# while a > 0:
#
#     b = a%10
#     c = c + b
#
#     # c = temp%10
#     a = a//10
#     # d = c // 10
# print(c)


#
# #7)reverse a number using while loop
# a = int(input("enter num: "))
# b = 0
# while a > 0:
#     c = a % 10
#     b = b*10+c
#     a = a//10
# print(b)





#print th given series
#2 22 122 2222
#
# a = 2
# b = 1
# c = 0
# while a < 2222:
#     b+=b*a
#     c+=
#     a+=1
#     print(b)

# a = 0
# while a <= 4:
#     a += 1
#     print("2" * a)

# a = 0
# while a <= 2222:
#     a = a * 10+2
#     print(a)
#


#palindrome
a = int(input("enter the number:"))
f = a
b= 0
while a > 0:
    c = a % 10
    b = b*10+c
    a = a // 10
if f == b:
    print("it is palindrome=",b)
#
# else:
#     print("it is not palindrome")

#
# a= []
# b = int(input("Enter a range: "))
# z = 0
# while z < b:
#     h = int(input("Enter a number: "))
#     a.append(h)
#     z += 1
# print(a)



#largest number
# a = [10,4,5,7,17,18]
# b =a[0]
#
# while a[i] > b:
#
#     i = a[i]
#     i += 1
#     print(i)



#
# a=[12,4000,56,780,90]
# i=0
# larg=a[0]
# while i<len(a):
#     if a[i]>larg:
#         larg=a[i]
#     i+=1
#
# print(larg)






#how to access list element
# a = [10,4,5,7,17,18]
# i=0
# large = a[0]
# while i<len(a):
#     print(a[i])
#     i+=1
# if i > large:
#     large = a[i]
#     print(large)


#smallest
# a = [30,60,70,40]
# i = 0
# small = a[0]
# while i < len(a):
#     if a[i] < small:
#         small = a[i]
#     i+=1
# print(small)


#second largest
# a = [30,751,768,93,24,12,11,1]
# i = 0
# large = a[0]
# scd_large = a[0]
# while i < len(a):
#     if a[i] > large:
#         scd_large = large
#         large = a[i]
#
#     elif a[i] >scd_large  and a[i] != large:
#         scd_large = a[i]
#     i += 1
# print(scd_large)

#
# a = "halloworld"
# i = 0
#
# while i < len(a):
#     print(i,a[i])
#     i += 1












