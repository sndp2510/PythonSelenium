import os

#Get the current working directory
currentWorkingDirectory = os.getcwd()
print (currentWorkingDirectory)

absolutePathToCsv= currentWorkingDirectory + "\Resources\Record.Csv"

fw=open(absolutePathToCsv,"w")
fw.write("101,San,FirstDiv")
fw.write("\n")
fw.write("102,Tan,FirstDiv")
fw.write("\n")
fw.write("103,Wan,SecondDiv")
fw.write("\n")
fw.write("104,Jan,ThirdDiv")
fw.write("\n")
fw.close()


fr=open(absolutePathToCsv,"r")
print("People having First Division")
for li in fr:
    print(li)
    te = li.rstrip("\n")
    record = te.split(",")
    #print("record", record)
   
    if "FirstDiv" in record:
        print(record[0], record[1])   
        
