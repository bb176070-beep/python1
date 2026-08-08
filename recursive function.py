# recursive function

# def hai(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * hai(n-1)
#
# print(hai(5))


# sum
# def hai(n):
#     if n == 1:
#         return 1
#     else:
#         return n + hai(n - 1)
# a = int(input("enter the number:-"))
# print(hai(a))


# find the maximum element in list
# count the numbers of vowels in a string using recursion
# find the smallest element in a list

# 1)find the maximum element in list
# num = [1, 6, 9, 67, 9]
# def hai(n):
#     if len(n) == 1:
#         return n[0]
#     m = hai(n[1:])
#     if n[0] > m:
#         return n[0]
#     else:
#         return m
# print(hai(num))

## [1, 6, 9, 67, 9]
## [ 6, 9, 67, 9]
## [ 9, 67, 9]
## [ 67, 9]
## [ 67]

#2)count the numbers of vowels in a string using recursion
# def count_vowels(s):
#     if s == "":
#         return 0
#
#     if s[0].lower() in "aeiou":
#         return 1 + count_vowels(s[2:])
#     else:
#         return count_vowels(s[1:])
#
# text = input("Enter a string: ")
# print("Number of vowels:", count_vowels(text))

## hadhi
##  h = "aeiou"  , count_vowels(s[0:])
## a = "aeiou"   , count_vowels(s[1:])
## d = "aeiou"   , count_vowels(s[1:])
## h = "aeiou"   , count_vowels(s[1:])
## i = "aeiou"   , count_vowels(s[2:])

# find the smallest element in a list
# num = [6,9,67,9,1]
# def hai(n):
#     small = n[0]
#     for i in n:
#         if i < small:
#             small = i
#     return small
# print(hai(num))

##i < small
## 1 < small  # small = 1
## 6 < small  # small = 1
## 9 < small  # small = 1
## 67 < small  # small = 1
## 9 < small  # small = 1




