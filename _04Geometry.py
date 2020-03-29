sideCount=int(input("Enter Number of side: "))

if(sideCount==1):
    print("Its square")
    side=int(input("Enter length of side : "))
    print("Area of the square is : " , (side*side))
elif(sideCount==2):
    print("Its Rectangle")
    length = int(input("Enter length of side : "))
    breadth =int(input("Enter length of side : "))
    print("Area of the square is : " , (length*breadth))
else:
    print("Invalid Entry")
    