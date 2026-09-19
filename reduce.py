# from functools import reduce
# def add(a,b):
#     return a+b
# result = [1,2,3,4]
# result = reduce(add,result)
# print(result)

# from functools import reduce
#
# num = [1,2,4]
# hai = reduce(lambda x,y:x*y,num)
# print(hai)

# from functools import reduce
#
# num = [4, 7, 8,9]
# hai = (list(filter(lambda x: x % 2 == 1, num)))
# z = reduce(lambda x, y: x + y, hai)
# print(hai)
# print(z)


#1)factorial of a number using reduce

# from functools import reduce
#
# k = 5
# f = reduce(lambda x, y: x * y, range(1, k + 1))
# print(f)

# #2)find the longest word in  a list
# from functools import reduce
# k = ["hai","hallo","hadhi rr"]
# h =(list(map(lambda x:x if len("hai")> len("hallo") else len("hadhi rr"),k)))
# print(h)
# result = reduce(lambda x,y:x,h)
# print(result)



#3)add 5 to every num in a list and find the smallest value
# from functools import reduce
#
# num = [10, 4, 7, 2, 9]
# result = list(map(lambda x: x + 5, num))
# print(result)
# small = reduce(lambda x, y: x if x < y else y, result)
# print( small)

# 4)find the total length of all in a list
# from functools import reduce
# hai = ["hai","hallo","hadhi"]
# total = reduce(lambda x,y:x+len(y),hai,0)
# print(total)


