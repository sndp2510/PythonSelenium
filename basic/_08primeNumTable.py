flag=False

sRange = 3
eRange = 10

#Find Whether Number is prime or Not
for i in range(sRange,eRange):
    for j in range(2,i):
        if(i%j ==0):
            flag=True
            break
    
    if(flag==True):
        pass
    else:
        print(">>>",i)
        for k in range(1,11):
            print ("%d" %i, end = ' '),
            print (" x " , end = ' '),
            print ("%d=" %k, end = ' '),
            print(i*k)
    flag=False
    
    
    