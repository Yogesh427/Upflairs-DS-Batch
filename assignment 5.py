# peterson no.
import math

n = int(input("Enter a number: "))
temp = n
sum_fact = 0

while temp > 0:
    digit = temp % 10
    sum_fact += math.factorial(digit)
    temp //= 10

if sum_fact == n:
    print("Peterson Number")
else:
    print("Not a Peterson Number")
  
#circular prime no.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = input("Enter a number: ")

flag = True
for i in range(len(n)):
    rotated = int(n[i:] + n[:i])
    if not is_prime(rotated):
        flag = False
        break

if flag:
    print("Circular Prime")
else:
    print("Not Circular Prime")
    
#harshad no.
n = int(input("Enter a number: "))

digit_sum = sum(int(d) for d in str(n))

if n % digit_sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")
    
    
    
#magic no.
n = int(input("Enter a number: "))

while n > 9:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    n = s

if n == 1:
    print("Magic Number")
else:
    print("Not a Magic Number")
    
#generate pascal triangle

rows = int(input("Enter number of rows: "))

for i in range(rows):
    num = 1
    for j in range(rows - i):
        print(" ", end="")
    
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    
    print()
    
    
#duck no.
n = input("Enter a number: ")

if '0' in n and n[0] != '0':
    print("Duck Number")
else:
    print("Not a Duck Number")            