#Create a class Employee with attributes emp_name, emp_id, and salary.
#Create 3 objects and display their details.
'''task 1'''
class Employee:
    def __init__(self,emp_name= "none",emp_id= 000,salary= 00000):
        self.emp_name=emp_name
        self.emp_id = emp_id
        self.salary = salary
    def details(self):
        print( "!!!"*20)
        print(f"emp_name: {self.emp_name}")
        print(f"emp_id: {self.emp_id}")
        print(f"emp_salary: {self.salary}") 
        print( "!!!"*20)

e1= Employee("yogesh",1,35000)  
e2= Employee("vishnu",2,50000)  
e3= Employee("shaurab",3,35000)    

e1.details()
e2.details()
e3.details()

'''Create a class Calculator with methods for addition, subtraction,
multiplication, and division.
  task 2  '''
    
    
class Calculator :
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def addition(self):
        print(self.a+self.b)
        return self.a+self.b
    def subtraction(self):
        print(self.a-self.b)
        return self.a-self.b
    def multiplication(self):
        print(self.a*self.b)
        return self.a*self.b
    def division(self):
        if self.b!=0 :
            print(self.a/self.b)
            return self.a/self.b
        else :
            print("not possible when zero is in denominator") 

x1= Calculator(23,45)  
x2= Calculator(23,0)  
x3= Calculator(45,3) 

x1.addition()
x2.division()
x3.multiplication() 
 
'''
 Create a class Book with a constructor to initialize title, author, and price,
then print details.
 task 3
 '''
class Book:
    def __init__(self,title= "none",author= "none",price= 0):
        self.title=title
        self.author = author
        self.price = price
    def details(self):
        print( "!!!"*20)
        print(f"title: {self.title}")
        print(f"author: {self.author}")
        print(f"price: {self.price}") 
        print( "!!!"*20)

e1= Book("true immortality","yogesh",450)  
e2= Book("future of vr","vishnu",500)  
e3= Book("super intelligence","shaurab",1299)    

e1.details()
e2.details()
e3.details()

'''Create a class Vehicle with method display(). Inherit it into class Car and
call parent method.
task 4
'''
class Vehicle:
    def display(self):
        print("This is a Vehicle")

class Car(Vehicle):
    def show(self):
        Vehicle.display(self)   
        print("This is a Car")

c = Car()
c.show()
 
'''
 Write a Python program using regex to find all digits from the string:
"Python123Assignment456"
task 5
 '''
 
 
import re

text = "Python123Assignment456"

digits = re.findall(r"\d", text)

print(digits)