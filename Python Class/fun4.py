def Catwalk(name, age):
    print(f'My name is {name} and i am {age} years old!')
    
Catwalk("Benny", 20)
Catwalk(age=20, name="Benny") #KeyWord Argument!!!

def Exam(test, score):
    print(f"The exam was about {test} and the avearge score was {score}")

Exam("Python Class", 68.9) # Positional Arguments
Exam(score=68.9, test="Python Class")

#Lambda
fit = lambda a : a * 5

def fitt(a):
    print(a * 5)
    
print(fit(5))
fitt(5)

user = lambda first, last : f'Welcome to class {first} {last}'
print(user('John', 'Micheal'))

# Map, Filter & Reduce functions:
r = list(map(lambda x : x * 2, [2,3,4,5,6]))
print(r)

u = list(map(fitt, [2,3,4,5,6,7]))

x = list(filter(lambda x : x if x % 2 == 0 else False, [3,4,5,6,7,8,9,10]))
print(x)

e = list(filter(lambda a : a if a % 3 == 0 else False, [3,4,5,6,7,8,9,10]))
print(e)