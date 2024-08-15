def AddNum ():
    return 20 + 5

print(AddNum())

def Call (k):
    return f'I just called {k}'

print(Call('Henry'))

#Class Work!!!

# Write a function that takes one argument anf display a text added to the argument

#default argument!!!!

def name(fname="Peter"):
    return f'Hello {fname}'

print(name())
print(name("Paul"))

def Plug(v, l):
    return f'Welcome {v} and {l}'

print(Plug("Kenny", "Brown"))

yy = lambda x : x * 2
print(yy(5))

re = lambda a,b: a * b + 2
print(re(3,5))

def test(n):
    return lambda x : x+ n

t = test(10)
print(t(5))
