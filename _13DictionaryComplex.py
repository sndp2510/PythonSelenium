#Dictionary
dictEmp = {'E101':['San','CEO',32],'E102':['Seb','CTO',37],'E103':['Sar','CFO',52]}

a = input("enter the employee id: ")

# for  employee id Deatils are below
detList=dictEmp.get(a,"Not Found")

for i in range (0,len(detList)):
    print(detList[i])

for i in range (0,detList):
    print(detList[i])


#print("employee name is ",dictEmp.get(a,"Not Found"))
#print("Again employee name is ",dictEmp[a])