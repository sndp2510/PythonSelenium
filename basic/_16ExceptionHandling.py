#try except block of code

'''
try:
    statment with possible exception steps'
except:
    handle step for exception if thrown
else:
    if no exception 
'''

import os

#Get the current working directory
currentWorkingDirectory = os.getcwd()
print (currentWorkingDirectory)

absolutePathToNoFile= currentWorkingDirectory + "\Resources\oFile.txt"

try:
    fw=open(absolutePathToNoFile,"r")
    fw.write("Hello World..!!")
except:
    print("Exception :: The File : ",absolutePathToNoFile," not found.")
else:
    print("No Exception Found. File Successfully written")    
    fw.close()
    
    
    
#get the exception message
print("===Fetching Exception Message===")    
try:
    fw=open(absolutePathToNoFile,"r")
    fw.write("Hello World..!!")
except Exception as e:
    print("Exception :: The File : ",absolutePathToNoFile," not found.")
    print("Python message : ",format(e))
else:
    print("No Exception Found. File Successfully written")    
    fw.close()