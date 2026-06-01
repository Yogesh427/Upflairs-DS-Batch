# Assignment 2 - Basic Python and Data Types
# Name: Yogesh Singh

# Q1 ATM Withdrawal
correct_pin = 1234
pin = int(input("Enter PIN: "))
balance = float(input("Enter Balance: "))
amount = float(input("Enter Withdrawal Amount: "))

if pin != correct_pin:
    print("Incorrect PIN")
elif amount % 100 != 0:
    print("Invalid Amount")
elif amount > balance:
    print("Insufficient Balance")
else:
    print("Successful Withdrawal")

# Q2 Leap Year and Days in Month
year = int(input("Enter Year: "))
month = int(input("Enter Month: "))

leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if month == 2:
    print("Days:", 29 if leap else 28)
elif month in [4, 6, 9, 11]:
    print("Days: 30")
else:
    print("Days: 31")

# Q3 Arithmetic Operations
a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# Q4 List Comprehension
squares = [x**2 for x in range(1, 21)]
even_squares = [x for x in squares if x % 2 == 0]
print(squares)
print(even_squares)

# Q5 Dictionary
students = {"Rahul": 80, "Aman": 90, "Priya": 85, "Neha": 95, "Riya": 88}
print(students.keys())
print("Marks of Aman:", students["Aman"])
print("Topper:", max(students, key=students.get))
students["Yogesh"] = 92
print(students)

# Q6 Student Details
student = {"name": "Yogesh Singh", "age": 22, "course": "AI & ML"}
numbers = {10, 20, 30, 40, 50}
num = int(input("Enter a Number: "))

print(student)
print(numbers)
print(num)
