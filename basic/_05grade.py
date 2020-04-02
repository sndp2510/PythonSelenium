marks=int(input("Enter a marks: "))

if((marks<=100)&(marks>80)):
    print("Grade A")
elif((marks<=80)&(marks>60)):
    print("Grade B")
elif((marks<=60)&(marks>40)):
    print("Grade C")
elif((marks<=40)&(marks>0)):
    print("Grade C")
else:
    print("Invalid marks")