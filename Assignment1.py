# Assignment 1 - Python Fundamentals
# Name: Yogesh Singh
# Age: 22
# City: Jaipur
# Course: AI & ML

# Q1
print("Name: Yogesh Singh")
print("Course: AI & ML")
print("Age: 22")
print("City: Jaipur")

# Q2
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old")

# Q3
text = input("Enter a string: ")
print("Reverse:", text[::-1])
print("Total Characters:", len(text))

# Q4
s = {1, 2, 2, 3, 4, 4, 5}
print("Original Set:", s)
s.add(6)
print("After Add:", s)
s.remove(3)
print("After Remove:", s)

# Q5
t = (10, 20, 30, 20, 40, 50)
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Count of 20:", t.count(20))
print("Index of 40:", t.index(40))
