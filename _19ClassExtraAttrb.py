
class Student:
    #Constructor in python
    def __init__(self,name, grade, extraAttrb):
        self.name=name
        self.grade=grade
        
    def printStudent(self):
        print("Name:",self.name, " Grade:", self.grade)
        

#Inheritence - CollgeStudent inherits Student
class CollgeStudent(Student):
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        
    def summerTraining(self):
        print(self.name," goes for summer internship")
    
col1 = CollgeStudent("Ab", "A");
col2 = CollgeStudent("Xy", "C");

col1.summerTraining()
col2.printStudent()