# x=lambda a,b,c:a+b+c
# obj=x(12,34,3)
# print(obj)

# x=lambda a:a*a
# obj=x(12)
# print(obj)

# t = lambda a,b,c:a+b+c
# h = t(10,20,30)
# print(h)

# j = lambda a: a*a
# f=j(45)
# print(f)

#find the last digit of number using lambda
#find the average of three number using lambda
#area of circle using lambda
#find the length of string using lambda
#change the string to uppercase using lambda

#1)find the last digit of number using lambda
# x = lambda a:a%10
# f = x(123)
# print(f)

#2)find the average of three number using lambda
# x = lambda a,b,c: (a+b+c)/2
# f =x(5,5,10)
# print(f)




#3)area of circle using lambda
# x = lambda a:3.14*a*a
# f = x(5)
# print(f)

#4)find the length of string using lambda
# a = lambda x: len(x)
# b =a("hello")
# print(b)

#5)change the string to uppercase using lambda
# a = lambda x: x.upper()
# b = a("hadi")
# print(b)


# x=lambda a,b:a if a>b else b
# obj=x(120,34)
# print(obj)

#write the program to check the given number is odd or even
#+ or - using lambda
#greatest among three number
# chack if a number divisible by both 3 and 5

#write the program to check the given number is odd or even
# x = lambda a:a if  a%2==0  else "odd not"
# d = (x(int(input("Enter a number: "))))
# print(d ,"even")

#+ or - using lambda
# d = lambda a,b:"+" if a>b  else "-"
# h = (d(2,3))
# print(h)

#greatest among three number
# x = lambda a,b,c:a if a >b and a>c else b if b > a and b > c else c
# g = (x(9991,3992,3779))
# print(g)

#chack if a number divisible by both 3 and 5
# x = lambda a:a if a%3==0 and a%5==0  else "not divisible 3 and 5"
# j = (x(15))
# print(j)

e = int(input("enter the number:-"))
a =lambda x:x if 5%e==0 and 7%e==0 else "not divisible by 5 and 7"
b = (bool(e))
print(b)

#map
# def hai(a):
#     return a**2
# num = [1,2,3,6]
# hallo=list(map(hai,num))
# print(hallo)

#map lambda
# num = [1,2,3,4,5]
# result =(list(map(lambda x:x ** 2,num)))
# print(result)


#convert all name upper case using lambda and map
#find the length of each using lambda and map
#multiple corresponding element of two list
#find whether each number is even
#reverse each string lambda and map

#1)convert all name upper case using lambda and map
# name = ["hadhi","hai","hallo"]
# h = (list(map(lambda x:x.upper(),name)))
# print(h)

#2)find the length of each using lambda and map
# name = ["hadhi","hai","hallo"]
# h = (list(map(lambda x:len(x),name)))
# print(h)

# #3)multiple corresponding element of two list
# name = [2,5,7]
# name_2 = [5,9,3]
#
# h =(list(map(lambda x,y:x*y,name,name_2)))
# print(h)

#4)find whether each number is even
# num = [10,12,9]
# h = (list(map(lambda x:x if x%2==0 else " odd not",num)))
# print(h)


# a="hello"
# print(a[::-1])
#5)reverse each string lambda and map
# name = ["hadi","hai","car"]
# j = (list(map(lambda x:x[::-1],name)))
# print(name)
# print(j)


#filter


# def hallo(a):
#     return a%2==1
# num = [10,9,12,16,7]
# hallo=list(filter(hallo,num))
# print(hallo)

# num = [17,39,49,10]
# k = (list(filter(lambda x:x%2==0,num)))
# print(k)

#)filter only even numbers
#1)square only the even numbers
#2)convert names to uppercase having morethan 4 letter
#3)square numbers divisible by 3 and 5
#4)reverse only words ending with n



# 1)filter only even numbers
# num = [12,4,76,99,15]
# k = (list(filter(lambda x: x % 2 == 0, num)))
# print(k)


# 2)square only the even numbers
# num = [1,2,3,4,5]
# k = (list(filter(lambda p:p**2, num)))
# p=(list(map(lambda x: x**2,num)))
# print(p)


#3)convert names to uppercase having more than 4 letter
# name = ["hadi","rono","kandeen","missing"]
# k =(list(filter(lambda i:len(i)>4,name)))
# p = (list(map(lambda i:i.upper(),k)))
# print(p)

#4)square numbers divisible by 3 and 5
# num = [10,20,30,94,15]
# k = (list(filter(lambda x:x%3==0 and x%5==0,num)))
# p = (list(map(lambda x:x**2,k)))
# print(p)

#5)reverse only words ending with n
# name = ["ramos","degae","fran"]
# k = (list(filter(lambda x:x[::-1],name)))
# p =(list(map(lambda x:x.endswith("n"),k)))
# print(p)
#


# nums = [1,2,3,4,5,6]
# result = list((map(lambda x:x*x,filter(lambda x:x%2==0,nums))))
# print(result)

# 2)square only the even numbers
# num = [1,2,3,4,5]
# p=(list(map(lambda x: x**2,filter(lambda p:p**2, num))))
# print(p)


#3)convert names to uppercase having more than 4 letter
# name = ["hadi","rono","kandeen","missing"]
# p = (list(map(lambda i:i.upper(),filter(lambda i:len(i)>4,name))))
# print(p)


#4)square numbers divisible by 3 and 5
# num = [10,20,30,94,15]
# p = (list(map(lambda x:x**2,filter(lambda x:x%3==0 and x%5==0,num))))
# print(p)

#5)reverse only words ending with n
# name = ["ramos","degae","fran"]
# p =(list(map(lambda x:x.endswith("n"),filter(lambda x:x[::-1],name))))
# print(p)





