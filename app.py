# # Loops
# # For Loop
# fruits = ["apple", "banana", "cherry"]
# # fruits and their index
# for index, x in enumerate(fruits):
#     print(f"{x}{index}")
# # elemets in the list
# for y in fruits:
#     print(y)
# # to know if an elemet exists in a list
# x = "banana" in fruits
# print(x)
# name = "john"
# for n in name:
#     print(n)

# for fruit in fruits:
#     if fruit == "banana":
#         print("yes")

# betty = [1, 2, 3, 4, 5]
# for b in betty:
#     if 3 in betty:
#         print("yes")
#     else:
#         print("no")


# # While Loop


# # dictionaries

# person = {
#     "name": "john",
#     "age": 30,
#     "city": "New York",
#     "gender": "male"
# }
# print(person["city"])
# for key, value in person.items():
#     print(f"{key}: {value}")


# # functions in python
# def greet(name):
#     print(f"Hello, {name}!")


# def square_number(num):
#     return num * num


# result = square_number(4)
# print(result)

# result = square_number(10)
# print(result)


# #  print sum of even numbers
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def even_sum(numbers):
#     total = 0
#     for n in numbers:
#         if n % 2 == 0:
#             total += n
#     return total


# print(even_sum(num))

# largest = max(num)
# print(largest)


# def greeting(first_name, last_name):
#     print(f"Hello, {first_name} {last_name}!")


# greeting("John", "Doe")


# def sum_two_numbers(a, b):
#     return a + b


# result = sum_two_numbers(5, 10)
# print(result)

# # using return value in conditional statements


# def sum_two_numbers(a, b):
#     return a + b


# result = sum_two_numbers(5, 10)

# if result > 10:
#     print("The sum is greater than 10.")
# else:
#     print("The sum is 10 or less.")

# # using result in loops


# def sum_two_number(a, b):
#     result = (a + b)/2
#     if result > 10:
#         print("The sum is greater than 10.")
#     elif result > 5:
#         print("The sum is greater than 5.")
#     else:
#         print("The sum is 10 or less.")


# sum_two_number(5, 10)
# sum_two_number(3, 4)


# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for n in num:
#     result = n*2
#     print(result)


salaries = [1, 2, 3, 4]
increment = []
for each_salary in salaries:
    increment.append(each_salary+10000000)
print(increment)
for each_salary in salaries:
    print(each_salary)
