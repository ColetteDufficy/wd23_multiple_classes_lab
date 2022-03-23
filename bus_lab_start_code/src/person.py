class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.passengers = []
        
    def num_of_passengers(self):
        return len(self.passengers)