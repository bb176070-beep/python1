# a=[12,4,5,6,7]
# for x in a:
#     print(x)
from itertools import count
from multiprocessing.reduction import duplicate

from pip._internal import index

#
# x="hello world"
# for i in x:
#     print(i)



# for i in range(20,101,20):
#     print(i)


#1)write program to find first 10 even nummbers
#2)write program to find first 10 odd nummbers

# #1)write program to find first 10 even nummbers
# for r in range(0,12,2):
#      print(r)
#
#
# #2)write program to find first 10 odd nummbers


# for i in range(1,20,2):
#     print(i)

#write a program to find the length of list is in for loop
#smallest from the list and largest from the list

#3)write a program to find the length of list is in for loop

# a =[10,20,30,40,50,90]
# b=0
# for x in a:
#     b+=1
# print(b)



#4)smallest from the list and largest from the list
# a =[20,40,60,70,30]
# large = a[0]
# small = a[0]
# for i in a:
#     if i > large:
#         large = i
# print("\n","large = ",large)
#
# for i in a:
#     if i < small:
#         small = i
# print("\n","small =",small)

#5)write the program to count the occurences of each element in a list
#6)sum of element in list using for loop
#7)find the second largest number in list using for loop

#5)write the program to count the occurences of each element in a list
# s = ["car","bike","auto","car","bus","truck","car"]
# j = set(s)
# for i in s:
#         if i not in j:
#                 i = s.count(i)
#                 j.add(i)
#                 print(j)


#6)sum of element in list using for loop
# s = ["car","bike","auto","car","bus","truck","car"]
# a=[11,22,33,44]
# x=0
# for i in a:
#         x+=i
# print(x)



# print("\n","sum of list=",a)


#7)find the second largest number in list using for loop
# f = [10,20,30,40,50]
# largest =second = f[0]
# for i in f:
#     if i = largest :
#         largest = i
#     elif i > second :
#             second = i
# print(second)
# f.sort()
# for i in f[-2:-1]:
#         print(i)





#
# a=[1,2,3,4,2,3]
# b={}
# for i in a:
#         if i in b:
#                 b[i]+=1
#         else:
#                 b[i]=1
#
# print(b)


#write the program to inter change first and last element in a list using or loop
#reverse a list using for loop


# #8)write the program to inter change first and last element in a list using or loop
# g = [12,3,4,5,20]
# for i in range(1):
#     temp = g[0]
#     g[0]=g[-1]
#     g[-1]=temp
# print(g)



#9) reverse a list using for loop
# s = ["car","bike","bmw","truck","bus","bmw"]
# b = []
# for i in s:
#         b.insert(0,i)
# print(b)
#
# for i in range(1,11):
#     for j in range(100,111):
#         print(i,j)

# for i in range(18,21):
# 		for j in range(40,46):
# 					print(i,j)

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()



# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# n = 5
# #space make
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#
#
# #triangle make
#
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#
# n = 5
# #space make
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
# #triangle
#
#     for j in range(n-i):
#         print("*",end=" ")
#     print()


# n = 5
# for i in range(n-2):
#     for j in range(n-2):
#         print(" ", end=" ")
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()


# n = 9
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()


#hour time
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
# for k in range(n):
#     for j in range(n-k):
#         print("",end=" ")
#     for j in range(k+1):
#         print("*",end=" ")
#     print()

#butterfly
# a =int(input("enter the number: "))
# n = a
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     #space
#     for j in range(i+1):
#         print("",end="")
#     for j in range(n-i):
#         print("",end="  ")
#     #right fly up
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#
#     print()
# for k in range(n):
#     for j in range(n-k):
#         print("*",end=" ")
#     #space
#     for j in range(n-k):
#         print("",end="")
#     for j in range(k+1):
#         print("",end="  ")
#
#     #right fly down
#     for j in range(k+1):
#         print(" ",end=" ")
#     for j in range(n-k):
#         print("*",end=" ")
#     print()

#time hour space
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(" ",end="   ")
#     print()
# for k in range(n):
#     for j in range(n-k):
#         print(" ",end=" ")
#     for j in range(k+1):
#         print(" ",end="   ")
#     print()







    #  #space (1)
    # for j in range(n-k):
    #     print(" ",end=" ")
    # print()

#center space(1)
#
# for m in range(n):
#     for j in range(m+1):
#         print(" ", end=" ")
#     for j in range(n-m):
#         print("*",end=" ")


#center space (2)
    #
    # for j in range(n-m):
    #     print("*",end=" ")
    # print()

# for f in range(n):
#     # space (2)
#     # for j in range(n-f):
#     #     print("",end="")
#
    # for k in range(n-f):
    #     print(" ",end=" ")
    # for k in range(f+1):
    #     print("*",end=" ")
#     print()
# for l in range(n):
#     for k in range(l+1):
#         print(" ",end=" ")
#     for k in range(n-l):
#         print("*",end=" ")
#     print()



# n=5
# for i in range (n):
#     for j in range (n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#hollow right triangle
# n = 5
# for i in range(n):
#     for j in range(n):
#         if j==0 or i == n-1 or i == j :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#hollow left triangle
# n = 5
# for i in range(n):
#     #space
#     for j in range(i+1):
#         print("",end="")
#     #left angle
#     for j in range(n):
#         if i == 0 or j == n-1 or i==j:
#             print("*",end=" ")
#         else:
#             print("  ",end="")
#     print()

#diamond
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end="   ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end="   ")
#     print()

#hollow diamond
n = 5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(n):
#         if i==n-1 or j == i or i == j or j==0 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(n):
#         if  j==n-1 or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(n):
#         if   j == i or j ==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(n):
#     for j in range(n - i):
#         print("", end="")
#     # for j in range(i+1):
#     #     print("",end=" ")
#     for j in range(n):
#         if i == 0 or j == i  or j == n-1  :
#             print("*",end="    ")
#
#         else:
#             print("  ",end="  ")
#     print()



#x
# n = 9
# for i in range(n):
#     for j in range(n):
#         if j ==0 or i == 0 or i == n -1 or j == n-1 or i == j or i + j == n -1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#x hollow
# n = 5
# for i in range(n):
#     for j in range(n):
#         if j ==i or i + j== n -1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

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


