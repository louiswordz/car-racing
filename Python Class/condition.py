age = 11

if age == 11:
    print("Happy")
    
name = 'Moses'

if name != "Bassey":
    print("Not correct!")
    
if age < 8:
    print("Child!")
else:
    print("Big child")
    
x = input("Enter a name: ")
if x == name:
    print(x)
else:
    print("Not found")
    
    
list1 = ["John", "Brown", "Moses", "Peter", "Kenny", "Philip"]
for i in list1:
    h = input("Enter a name: ")
    if i == h:
        print(h)
    else:
        print(f"{h} Not Found")
        
b = 60


if b == 20:
    print('Teen')
elif b < 20:
    print("Baby Teen")
elif b >50:
    print("Old")
else:
    print("Advanced")
