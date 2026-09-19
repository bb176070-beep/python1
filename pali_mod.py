def add(a):

    g = a
    b = 0

    while a > 0:
        c = a % 10
        b = b * 10 + c
        a = a // 10

    if g == b:
        print("the number is pali")

    else:
        print("the number is not pali")



