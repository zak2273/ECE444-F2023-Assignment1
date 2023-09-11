from utils import utils

print("Testing reverse function..\n")

print("integer test")
test = utils(21)
print(test.reversed())

print("float test")
test = utils(21.4)
print(test.reversed())

print("string test")
test = utils("21")
print(test.reversed())

print("")
print("Testing formatter function..\n")

print("integer test")
test = utils(21)
print(test.formatter())

print("float test")
test = utils(21.4)
print(test.formatter())

print("string test")
test = utils("21")
print(test.formatter())