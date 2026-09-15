print("--------- Identity Operators ---------")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # checks for values
print(x is y)  # checks for pointing to the same object

print("--------- Membership Operators ---------")

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)  # True

text = "Hello World"
print("H" in text)       # True
print("hello" in text)   # False
print("z" not in text)   # True
a = 4
b = 3
print("----------------Bitwise operator in python----------------")

print("a & b =", a & b) #
print("a | b =", a | b) #
print("a ^ b =", a ^ b) #
print("~a =", ~a) #
print("a << 1 =", a << 1) #
print("a >> 1 =", a >> 1) #

print("----------------Ternary operator in python----------------")

num = 15
res = "even" if num % 2 == 0 else "odd"
print("result = ",res) 