# a = "a"
# b = ["a", "b", "c"]
# if a in b:
#     print("a is seen in b")
# else:
#     print("a is not seen in b")

# a = ["elephant","loop","dog","cat"]
# x = ["a","e","i","o"]
# for word in a:
#     if word[0].lower() in x:
#         print(word,"it vowel")
#     else:
#         print(word,"it not vowel")
#

# a = "dog"
# b = ["a", "e", "i", "o", "u"]
#
# found = False
#
# for letter in a:
#     if letter in b:
#         found = True
#         break
#
# if found:
#     print("Word contains a vowel")
# else:
#     print("No vowel found")

# ****************************************************************************************


# a = int (input ("enter the number"))
# if  a % 7 == 0:
#     print ("the divisiblr by 7")
# else:
#     print ("the not divisiblr by 7")

# ****************************************************************************************
#
# a = int(input("enter the number"))
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")
#

# ****************************************************************************************

# a = int(input("negter the number"))
# if  a>= 90 and a<= 100:
#     print("A+")
# elif a>= 80 and a<= 90:
#     print("A")
# elif a>= 70 and a<= 80:
#     print("B+")
# elif a>= 60 and a<= 70:
#     print("B")
# elif a>= 50 and a<= 60:
#     print("C+")
# elif a>= 40 and a<= 50:
#     print("C")
# elif a>= 30 and a<= 40:
#     print("D+")
# elif a>= 20 and a<= 30:
#     print("D")
# else:
#     print("fail")

# ***********************************************************************
#
# a = int(input("enter the number"))
# b = int(input("enter the number"))
# c = int(input("enter the number"))
#
# if a > b and a > c:
#     print(a,"is larger")
# elif b > a and b > c:
#     print(b,"is larger")
# else:
#     print(c,"is larget")
#
# ***********************************************************************

#
# a = int(input("enter the number:"))
# if a >= 100 and a < 1000:
#     print("\n","it is 3 digits")
# elif a >= 10 and a <99:
#     print("\n","it is not a 3 digit")
# elif a >=1 and a < 9:
#     print("\n","it is not a 3 digits")
# else:
#     print("\n","it is not a 3 digits")

# ***********************************************************************
# a = [20,230,40]
# large = a[0]
# for i in a:
#     if i < large:
#         large = i
# print(large)


# a = ["bus","car","bus","truck"]
# b = a[0]
# for i in a:
#     if i == "bus":
#         b = a.count("bus")
# print(b)


# a = [11,22,3,45]
# x = 0
# for i in a:
#     x+=i
#     print(x)

# a = [1,23,4,9]
# b = {}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[1]=1
# print(b)

# a=[1,2,3,4,2,3]
# b={}
# for i in a:
#         if i in b:
#                 b[i]+=1
#         else:
#                 b[i]=1
#
# print(b)


# for i in range(1,21,1):
#     if(i%3==0 and i%5==0):
#         print(" fizzbuzz")
#     elif(i%5==0):
#         print(" buzz")
#     elif(i%3==0):
#         print(" fizz")
#     else:
#         print(i)
# print()

# for i in range(18,21):
#     for j in range (40,46):
#         print(i,j)

# n = 10
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# n = 8
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
#

# n = 8
# for i in range (n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end="   ")
#     print()


# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# n = 8
# for i in range (n):
#     for j in range(i+1):
#         print("*",end=" ")
#
#     for j in range(n-i):
#         print("",end="  ")
#
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
#
# for k in range(n):
#     for j in range(n-k):
#         print("*",end=" ")
#
#     for j in range(k+1):
#         print("",end="  ")
#
#     #right fly down
#     for j in range(k+1):
#         print(" ",end=" ")
#     for j in range(n-k):
#         print("*",end=" ")
#     print()


# n = 5
# for i in range(n):
#     for j in range (n):
#         if j == 0 or i ==n-1 or i ==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n= 5
# for i in range(n):
#     for j in range(i+1):
#         print("",end="")
#     for j in range(n):
#         if i== 0 or j==n-1 or i==j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end="   ")
#     print()
# for k in range(n):
#     for j in range(k+1):
#         print(" ",end=" ")
#     for j in range(n-k):
#         print("*",end="   ")
#     print()



# n = 8
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(n):
#         if  j==n-1 or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(n):
#         if   j == i or j ==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# a = 2
# while a <=10:
#     print(a)
#     a+=1

# a = 2
# c = 0
# while a <=10:
#     c+=a
#     a+=2
# print(c)
#
# a = 1
# b =1
# while a < 5:
#     b+=b*a
#     a+=1
# print(b)


# a =112
# c = 0
# while a > 0:
#     b = a%10
#     c = c +b
#     a = a//10
# print(c)

# a = 123
# b =0
# while a > 0:
#     c = a % 10
#     b = b*10 + c
#     a = a // 10
# print(b)

# a = [10,4,79,3,9]
# i = 0
# while i<len(a):
#     print(a[i])
#     i+=1

# a =[12,5,7,9,57,51]
# i =0
# large = a[0]
# while i < len(a):
#     if a[i] < large:
#         large = a[i]
#     i+=1
# print(large)

# a = "hallo hadhi"
# b = 0
# while b < len(a):
#     print(b,a[b])
#     b += 1


