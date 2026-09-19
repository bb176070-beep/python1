# print(10/0)
# try:
#     x=10/0
#     print(x)
#
# except:
#     print("cant divide")
# from abstration import Area


# a=[12,2,3,3,33,33]
# print(a[10])

# try:
#     a=[12,2,33,45,67]
#     print(a[2])
# except:
#     print("error")

# try:
#     n = int(input("enter the number: "))
#
# except:
#     print("error")
#
# else:
#     print("ok")

#
# try:
#     n = int(input("enter the number: "))
#     b = 10/n
#     print(b)
# except (ZeroDivisionError, ValueError) as e:
#     print(f"error cause {e}")
#
# else:
#     print("ok")


# class Hallo(Exception):
#     pass
#
# try:
#     n = int(input("enter the number "))
#     if n < 18:
#         raise Hallo("it is small number")
#
# except Hallo  as e:
#     print(f" enter  the number greater than 18 {e}")
#
# except ValueError as e:
#     print(f" it cause {e}")
#
# except ZeroDivisionError as e:
#     print(f" it cause {e}")
#
# else:
#     print(f"your entered number is {n}")
#
# finally:
#     print("ok")

# def add(a,b):
#     try:
#         return a+b
#     except TypeError:
#         return f"input  type error"
# print(add(1,2))
# print(add(9,"h"))

# def division(a,b):
#     try:
#         return a/b
#     except TypeError:
#         return f"input error"
#
# print(division(1,2))
# print(division(3,"gh"))
#
# def subtract(a,b):
#     try:
#         return a-b
#     except TypeError:
#         return f"input error"
# print(subtract(1,2))
# print(subtract(3,"gh"))

# def sum_natural(n):
#     try:
#         if n == 1:
#             return n
#         else:
#             return n + sum_natural(n-1)
#     except TypeError:
#         return f"input error"
#
# print(sum_natural(4))
# print(sum_natural("g"))
# print(sum_natural(1))

# def area_circle(n):
#     try:
#         if n == 0:
#             return n
#         else:
#             return 3.14 * n * n
#     except TypeError:
#         return f"input error"
#
# print(area_circle(5))

# class Product:
#     def __init__(self, name, price):
#         try:
#             self.name = name
#             self.price = float(price)
#         except TypeError:
#             print("integer type only")
#     def apply_discount(self, percentage):
#         try:
#             discount = self.price * (percentage/100)
#             final_price = self.price + discount
#             print("price = ",final_price)
#         except Exception as e:
#             print("error",e)
# p1 = Product("P1", 100)
# p1.apply_discount(10)


# class Student:
#     def __init__(self, name, mark):
#         try:
#             self.name = name
#             self.mark = float(mark)
#         except TypeError:
#             print("number type only")
#
#     def add_bonus(self, bonus):
#         try:
#             final_mark = self.mark + bonus
#             print("final mark =", final_mark)
#         except Exception as e:
#             print("error", e)
# s1 = Student("Hadhi", 80)
# s1.add_bonus(5)
