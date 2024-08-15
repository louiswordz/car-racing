class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        
    def Running(self):
        return f"{self.name}"