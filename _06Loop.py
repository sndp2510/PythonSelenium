sRange=10
eRange=20

print("Using For loops with range")
for i in range(sRange,eRange):
    print(i)

print("Using For loops with increment 2")
for i in range(sRange,eRange,2):
    print(i)
    
    
print("Using For loops with decrement -2")
for i in range(eRange,sRange,-2):
    print(i)

print("Using While loops with range")
i=sRange
while(i<eRange):
    print(i)
    i=i+1