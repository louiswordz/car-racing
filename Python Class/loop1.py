#loops are repititive functions carried on an item

x = "Hello"
for i in x:
    print(i)
    
y = ['Bag',"Candle","Shoes","pencil","Pen"]

for x in y:
    print(x)
    
for num in range(1,10+1):
    print(num)
    
d = 0
e = 10
while d < e :
    print(d)
    d+=1
    
u = ['a','b','c','d','e']

while u:
    g = []
    r = u.pop() 
    g.append(r)
    print(g)
    
# Conditions
w = 20
if w == 20:
    print("Yes")
    
if w < 20:
    print(True)
else:
    print(False)
    
print((w < 20))

if 10 < 5:
    print("Yes")
elif 10 == 11:
    print("Maybe")
else:
    print("No")
    
# Inputs

cat = input("Enter the name of your cat: ")
print(cat)

num = int(input("Enter a number: "))
print(num * 3)

# Dict

B = {"House":"NTA","Hubby":"Chess", "Diet":"Salad"}
print(B.keys())
print(B.values())
B['Place'] = 'Church'
print(B)

B.update({"Run":"100Km"})
print(B)

B.pop("Run")
print(B)

B.popitem()