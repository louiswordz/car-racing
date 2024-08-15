d = dict()
f = {}
print(type(d), type(f))

g = {'name':"Paul", 'age':25, 'Job':"Student"}
print(g)
print(g.keys())
print(g.values())
print(g['name'])
print(g['age'])
g['food'] = 'Noodels'
print(g)
g.update({"hubby":'dancing'})
print(g)

gy = ['e','f','g','h']
y = [1,2,3,4]

gi = []

for i in gy:
    for k in y:
       q= i +":" + str(k)
       gi.append(q)
print(gi)

for i in g:
    print(i)
    
for j in g.keys():
    print(j)
    
for n in g.values():
    print(n)
    
for i,j in g.items():
    print(j,":",i)
    
print('Job' in g)
print('age' in g)
w = g.copy()
print(w)

#ets
u = set()
print(type(u))
yy = {1,2,3,4,5,6,7,8,2,4,5,7}    
print(yy)

z = {"a", "b","c", "d","e","f","a","c"}
print(z)

print("c" in z)

set1 = {"Tom","Brown", "Jerry", "Ranger", "Disnwy", "puddy"}
set2 = {"Brown", "bernard", "Scott", "Rawl","Jerry"}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
set3 = set1.update(set2)
print(set3)