sRange=int(input("Enter the start range: "))

eRange=int(input("Enter the end range: "))


print("Using While loops")
i=sRange
while(i<eRange):
    if((i%7)==0):
        print("Number ",i," divisible by 7")
    i=i+1;
    
    
print("Using For loops")
i=sRange
for i in range(sRange,eRange):
    if((i%7)==0):
        print("Number ",i," divisible by 7")
    i=i+1;
    

