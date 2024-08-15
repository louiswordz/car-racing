d = 'Louis'
print(d)

print("Good Morning " + d)

game = "Chess"
name = "Louis"
print(name + " plays "+game)

n = '5' 
num = '5'
print(n + num) 

h = "Happy"
t = "hour"

print(f"{h} {t}")

print(h.upper())
print(h.lower())
print(t.capitalize())

print(type(h))

m = "John!"
print(m)

r = "How are you "+ m
print(r)

book = "how to play scrabble!"
print(book.upper())
print(type(m))
print(book.title())
print(book.capitalize())

names = "       Blessing!    "
print(names.lstrip())
print(names.rstrip())
print(names.strip())

print(len(book))

print(book[2])

s = "The cats that stays in our compound is scared of bigger cats"
print(s.count("cats"))

print(len(s))

can = "I have a canned juice"
print(can)

user = "Rowland"

C = user +" "+can[2:4] + "s " + can[7:]
print(C)

ky = "This is python"
dy = "class"
f = f"{ky} {dy}"
print(f)

gy = "Welcome to"
yy = "Excellent digital center"
ce = "{} {}".format(gy, yy)
print(ce)

print(gy.index('Welcome'))
print(yy.index("E"))
print(yy.index('e'))
p = yy.partition("center")
print(p)
print(p[1])

print(isinstance(type(yy), str))
print(isinstance(yy, str))
print(yy.isalpha())

nn = "This is 10:31"
print(nn.isalpha())

print(nn.isprintable())

print(gy.isalpha())

fy = " This is  12"
print(fy.isalpha())
print(fy.isspace())
print(fy.endswith("12"))

gg = "This dog is scared of the mouse that fought the other dog!"
print(gg.count("dog"))

print(gg.find("mouse"))
print(gg[26:])

print(gg.casefold())
print(gg.zfill(0))

#Assignment 
# create three string variables use the format, f and + to add them together
# use .upper, .title, use count method on each of them
#print("123".isalnum())
#print("good".upper().isalpha())

er = "emeka"
print(er.upper().isalpha())

bi = "John is here!"
ci= "Today is monday"
di = "How are you"

print(bi +" "+ci +" "+di)

ret = "John!"
print(ret)

Greet = "Good morning"
print(Greet + ' '+ ret)

e = "Where do you stay \nWhat is your name"
print(e)

f = "peter said 'Today is monday'"
print(f)

gg = "John told Philip that \"Yesterday was sunday\""
print(gg)