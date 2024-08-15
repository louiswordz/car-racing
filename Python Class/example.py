print(5)
print(5+4)
print(20-10)
print(22/11)
print(22//11) # floor division
print(5 % 3)
print(-22)
print(abs(-22))
print(pow(10, 2))
print(10 ** 2)


r = 10
print(r)

# Strings
print('Hello Everyone!')
print("Where are you?")

ft = "Today is Wednesday"
p = '1234567'
print(ft)
print(ft.upper())
print(ft.lower())
print(ft.title())
print(ft.capitalize())
print(ft.isalnum())
print(p.isalnum())
print(p.isalpha())
Q = "ABCDE"
print(Q.isalpha())
print(Q.islower())
k = "123.45"
print(k.isdecimal())
print(k.isalnum())


print(Q[0])
print(Q[1])

print(k[:3])

from functools import reduce

print(reduce(lambda a,b: a+b, [2,3,4,5,6,7]))