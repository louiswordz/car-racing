a = [2,1,3,4,5,6]
print(a)
print(a[0])
print(a[1])

print(a[0:3])
print(a[2:4])
a.append(7)
print(a)
for i in a:
    print(i)
k = [ "Jump","run",'clap']
print(k)
d=['a','b','c','d']
print(k[0])
print(k[1:3])

print(d)
print(d[0:2])

# Assignment !!!!

# 1. create three variables that contains a list, a number and a string
# 2. print all the variables.

for i in k:
    print
    
de = ["Cat", "Dog","Hen","Goat","Cow"]
print(de[0].upper())
print(de[1].lower())

for i in de:
    print(i.lower())
    
g = [i.upper() for i in de]
print(g)

for i in range(10+1):
    print(i)

f = [e for e in range(10+1)]
print(f)

re = ["Amanda", "Joseph", "Miracle", "Brian", "Shawn", "Moses", "Rowland"]
for x in re:

    print(x)
    
re.append("Stephen")
print(re)


re.insert(2, "Blessing")
print(re)

print(re[-1])

k = re.pop(3)
print(k)

re.remove("Blessing")
print(re)

d = [1,2,3,4,5]
h = [6,7,8,9,10]
print(d+h)

y = ["a","b","c","d","e"]
t = ["f","g","h","y"]
y.extend(t)
print(y)

print("b" in y)
print("k" in y)

j = y.copy()
o = y[:]
print(j)
print(o)

num = [4,2,5,2,5,2,9,1,5,8]
num.sort()
print(num)

ky = [33,12,10,9, 2,5,6,1,3]
ky.reverse()
print(ky)

ty = [20,11,8,4,2,10,6]
ty.sort(reverse=True)
print(ty)

print(ty.index(11))
print(ty.index(2))

u = []
p = list()
print(type(u))
print(type(p))

px =()

# Tuple
gy = tuple()
ey = ()
print(type(gy))
print(type(ey))

j[0] = 9
print(j)

tr = tuple(y)
print(tr)

print(tr[1])

for g in tr:
    print(g)
    
yy = (ge for ge in tr)
print(tuple(yy))

rt = tr[:]

print(rt.index("d"))

dk = [2,4,5,6,7,8,9]
k = sorted(dk)
print(k)

fk = [2,4,6,7,8,1,2,3]
fk.sort()
print(fk)