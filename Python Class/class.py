import time

class Test:
    x = 20
    
print(Test.x)

class Pick: 
    def Happy():
        print("Today is a happy day!")
        
Pick.Happy()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        print(f"Your name is {self.name} and you are {self.age} years old!")
        
        
S1 = Student("Rowland", 30)
print(S1.name)
print(S1.age)

class Holiday:
    def __init__(self, venue, date):
        self.venue = venue
        self.date = date
        
    def Date(self):
        print(f"The Holiday party will hold at {self.venue} and it will hold on {self.date}")
      
H1 = Holiday("12 omomo street", time.strftime('%d-%m-%Y'))  
H1.Date()


class Car:
    def __init__(self, Model, Year):
        self.Model = Model
        self.Year = Year
        
    def DescribeCar(self):


        return f"My car model is {self.Model} and was produced in the year {self.Year}"
    
C = Car("Audi", "C2021")
print(C.Model)