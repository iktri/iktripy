# def my_function():
#     print("Hello From My Function!")
#
# def my_function_with_args(username, greeting):
#     print("Hello, %s, From My Function!, I wish you %s" % (username, greeting))
#
# def sum_two_numbers(a, b):
#     return a + b
#
# def sum(a, b):
#     print(f"{a}+{b}={a+b}")
#
# sum(2, 3)
#
# def my_function(x):
#     return 5 * x
#
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))
#
# def printinfo(name, age):
#     print("Name: ", name)
#     print("Age: ", age)
#
# printinfo(age=10, name="miki")
#
# def list_benefits():
#     return "More organized code", "More readable code"
#
# def build_sentence(benefit):
#     return "%s is a benefit of functions!" % benefit
#
# def name_the_benefits_of_functions():
#     for benefit in list_benefits():
#         print(build_sentence(benefit))
#
# name_the_benefits
#
# # Contoh  built-in functions
# def absolute_value(num):
#     if num >= 0:
#         return num
#     else:
#         return -num
#
# print(absolute_value(2))
# print(absolute_value(-4))
#
#
# def absolute_value2(num):
#     num = abs(num)
#     return num
#
# print(absolute_value2(2))
# print(absolute_value2(-4))
#
#
# # This function adds two numbers
# def add(x, y):
#     return x + y
#
# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y
#
# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y
#
# # This function divides two numbers
# def divide(x, y):
#     return x / y
#
#
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
#
# # Take input from the user
# choice = input("Enter choice (1/2/3/4): ")
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if choice == '1':
#     print(num1, "+", num2, "=", add(num1, num2))
# elif choice == '2':
#     print(num1, "-", num2, "=", subtract(num1, num2))
# elif choice == '3':
#     print(num1, "*", num2, "=", multiply(num1, num2))
# elif choice == '4':
#     print(num1, "/", num2, "=", divide(num1, num2))
# else:
#     print("Invalid input")
#
# # Contoh script berikut disimpan dalam file rumus.py
# import numpy as np
#
# def luasling(r):
#     L = np.pi * r**2
#     return L
#
# from rumus import luasling
#
# # Menggunakan fungsi untuk satu nilai
# a = luasling(2)
# print(a)
#
# # Menggunakan fungsi dengan range nilai
# r = range(1, 10)
# for i in r:
#     print(f"r: {i}, L: {luasling(i)}")
#
# # Menyimpan hasil dalam list
# L = []
# for i in r:
#     L.append(luasling(i))
#
# print(L)
#
# # Lambda Functions
# myvar = lambda a, b: (a * b) + 2
# print(myvar(3, 5))
#
# # Lambda Operator untuk Persamaan Kuadrat
# def quad_equation(a, b, c):
#     return lambda x: a * x**2 + b * x + c
#
# y = quad_equation(2, 3, -5)(3)
# print(y)
#
# # Recursion Function (Faktorial)
# def facto(n):
#     if n == 1:
#         return 1
#     return n * facto(n - 1)
#
# print(facto(3))
