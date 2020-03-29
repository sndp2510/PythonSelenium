
class Student:
    #Constructor in python
    def __init__(self,name, grade):
        self.name=name
        self.grade=grade
        
    def printStudent(self):
        print("Name:",self.name, " Grade:", self.grade)
        

roll1 = Student("Abhi","A")
roll2 = Student("Ben","A+")
roll3 = Student("Chaita","A+")

roll2.printStudent()


#Inheritence - CollgeStudent inherits Student
class CollgeStudent(Student):
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        
    def summerTraining(self):
        print(self.name," goes for summer intern-ship")
    
col1 = CollgeStudent("Ab", "A");
col2 = CollgeStudent("Xy", "C");

col1.summerTraining()
col2.printStudent()