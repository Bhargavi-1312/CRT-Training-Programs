a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"a={a}")
print(f"b={b}")
# first logic arithmetic operation
# a = a + b
# b = a - b
# a = a - b
# print("After swapping:")
# print(f"a={a}")
# print(f"b={b}")
#second logic temporary variable
# temp = a
# a = b
# b = temp
# print("After swapping:")
# print(f"a={a}")
# print(f"b={b}")
#third logic is multiple assignment
a, b = b, a
print("After swapping:")
print(f"a={a}")
print(f"b={b}")