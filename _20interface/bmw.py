from interface import implements
from _20interface import ICar

class BMW (implements(ICar)):
    def milegae (self):
        return "10"
    
    def color (self):
        return "silver"
    
    
car1=BMW()
print(car1.color())
print(car1.milegae())
    