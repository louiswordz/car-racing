d = []
t = list()

x  = [2,4,5,6,7,8,9,10,2,3,4,5]
print(x[0])
print(x[1])

x.append(11)
print(x)

x.insert(2, 12)
print(x)

x.remove(10)
print(x)

names = ['John', "Micheal","Abigal","Nancy","Paul","Andre"]

names.append("Caroline")
print(names)

names.remove("Abigal")
print(names)

b = names.pop(1)
print(b)

bag = ["Paul","Kolade","Ifector","Brown"]
print(names + bag)

names.extend(bag)
print(names)


