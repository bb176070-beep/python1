# a={"name":"zaman","age":25}
# print(a)
# # dict()
# print(len(a))
# print(a["name"])
#

# a = {
#     "name": "hadhi",
#      "age" : 39,
#      "born" : 1978
# }

#consrtuctor

# a=dict(a=1,b=2,c=3)
# print(a)

# a = {
#     "name": "hadhi",
#      "age" : 39,
#      "born" : 1978
# }
# a.pop("born")
# print(a)


# k = a.update({"place " : "goa"})
# print(a)
#
# j =a.get("name")
# print(j)

# k = a.items()
# print(k)

# k = a.copy()
# print(k)

# j = a.clear()
# print(j)
#
# l = a.popitem()
# print(l)


# a = {
#     "name": "hadhi",
#     "age" : 39,
#     "born" : 1978
# }
# b=a.keys()
# print(b)
#
# c =a.values()
# print(c)
# d = a.fromkeys(a)
# print(d)

# a = {
#     "name": "hadhi",
#     "age" : 39,
#     "born" : 1978
# }
#
# p = {
#     "name" : "jhghj",
#     "age" : 33,
#     "born": 1998
# }
#
# hallo = {
#          "a" : a,
#          "b" : p
# }
#
# print(hallo)


m = {
    "hallo_1" :{
        "name" : "john",
        "email" : "john123@gmail.com",
        "number" : 76565545
    },

    "hallo_2" : {
        "name" : "junaid",
        "email" : "junaid123@gmail.com",
        "number" : 78260183
    },
    "hallo_3": {
        "name" : "hadhi",
        "email" : "hadhi123@gmail.com",
        "number" : 782024573
    }
}

# print(m)

# z = {
#     "name" : "manu",
#     "email" : "manu1542@gmail.com",
#      "number": 723545467
# }

# k = m.get("hallo_1")
# print("\n","get = ",k)

# m["hallo_1"].update({"place": "kerala"})
#
# print(m)

# k = m.pop()
# print("\n","get = ",k)

# del m["hallo_2"]["name"]
# print("\n","remove = ",m)

# m["hallo_3"].copy()
# print(m)
#
# k = m.clear()
# print(k)

# k = m["hallo_2"].items()
# print(k)
#
# z = m["hallo_3"].values()
# print(z)

# d = m["hallo_1"].fromkeys()
# print(d)

l = m["hallo_1"].keys()
print(l)