def Greet():
    print("What did you do this morning!")
    print("Hope you slept well")
    print("Today is Friday")
    
Greet()

def Roll():
    print("I woke up sound and healthy this morning!")
    print("How did you get here today?")
    print("What did you have for breakfast")
    
Roll()

# Create a function call it Pray then 
# 1. print i pray everyday 
# 2. I love to code
# 3. I pray everywhere! 

def Learn(name):
    print("My name is " + name)
    
Learn("Bennard")

def addNum (num):
    print(num * 20)
    
addNum(50)

def Minus(num1, num2):
    print(num1 - num2)
Minus(3, 10)

# Default Argument!!
def Divide(num1=27, num2=3):
    print(num1 /num2)
    
Divide()    
Divide(15)
Divide(15,5)

# Keyword Argument!!!!
def Username(fname, lname="Micheal"):
    '''Conditions are programs that runs based on a criteria!'''
    if fname or lname == "":
        print(fname + " "+ lname)
    else:
        print(fname)
        
Username("Macson")
Username("Brian", "Scott")

#Assignment!!
# 1. Create a functional with two positional argument then

        
