#student details 
def details(**info):
    print(info)
    

details(name="yogesh",age=22,course="btech")


# factorial of a no
print("_"*67)


def fact(i):
    if i>1 :
       return i*fact(i-1)
    else :
        return 1

     
print(fact(4))
    