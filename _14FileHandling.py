import os

#Get the current working directory
currentWorkingDirectory = os.getcwd()
print (currentWorkingDirectory)

pathToSampleTxt = currentWorkingDirectory + "\Resources\Sample.txt"

print ("absolute path to sample.txt : " + pathToSampleTxt)
#write a File
fw=open(pathToSampleTxt, "w")
fw.write("Hi dere")
fw.write("\n")
fw.close

#append a file
fw=open(pathToSampleTxt,"a+")
fw.write("Hello what's up.")
fw.close

#read a file
fread=open(pathToSampleTxt,"r")
for line in fread:
    print(line)
    
fread.close()
