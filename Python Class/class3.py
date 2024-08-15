
class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        self.eat = ["Grass", "Dungs","Leaf"]
        
    def Running(self):
        return f"{self.name} is running on {self.legs} legs"
    
    def Eating (self):
        for i in self.eat:
            return f"{self.name} eats {i}"
   
A = Animal("Cow", 4)
print(A.Running())
print(A.Eating())