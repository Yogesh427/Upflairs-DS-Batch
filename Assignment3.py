# Assignment 3 - User Defined Functions
# Name: Yogesh Singh

# Q1
def calculate_bill(price, quantity, discount):
    total = price * quantity
    final = total - (total * discount / 100)
    return final

print("Final Bill:", calculate_bill(500, 3, 10))

# Q2
def calculate_salary(basic, bonus=2000, tax=10):
    gross = basic + bonus
    net = gross - (gross * tax / 100)
    return net

print(calculate_salary(30000))
print(calculate_salary(30000, 5000, 5))

# Q3
def find_max(*numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_max(10, 45, 23, 67, 12))

# Q4
def student_details(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

student_details(Name="Yogesh Singh", Age=22, Course="AI & ML", City="Jaipur")

# Q5
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 6
for i in range(n):
    print(fibonacci(i), end=" ")
print()

# Q6
numbers = [5, 12, 17, 18, 24, 32]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squares = list(map(lambda x: x ** 2, even_numbers))

print("Even Numbers:", even_numbers)
print("Squares:", squares)
