# Class Beans
class Beans:
    def type(self):
        print("Vegetable")
    
    def color(self):
        print("Green")

# Class Mango
class Mango:
    def type(self):
        print("Fruit")
    
    def color(self):
        print("Yellow")

# Generic function demonstrating polymorphism
def func(obj):
    obj.type()
    obj.color()

# Create objects
b = Beans()
m = Mango()

# Pass objects to the generic function
func(b)
func(m)