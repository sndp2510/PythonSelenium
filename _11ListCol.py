list1=['pys','chem', 1987, 2011]


list2=[1,2,3,4,55,6,7,8,9]
print("list1" , list1)
print("list1[0]" , list1[0])
print(list2)
print("list2[1:5]" , list2[1:5]) #inclusive 1 and exclusive 5 index

del list2[3]
print("del list2[3]" ,list2)

list2.remove(6)
print("list2.remove(6)" ,list2)

for i in list2:
    print(i*2)
    
#List Functions
print("Length of list2:", len(list2))

print("max element  of list2:", max(list2))

print("min element of list2:", min(list2))

print("position of element in list:", list2.index(55))

list2.reverse()
print("Reverse of list2:", list2)