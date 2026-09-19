
def add1(a):

    g = a
    b = 0

    while a > 0:
        c = a % 10
        b = b * 10 + c
        a = a // 10

    print("reverse = ",b)




