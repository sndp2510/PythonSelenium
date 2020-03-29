#Enter the string and replace all vowel with Z

sen = str(input("Enter the sentence"))

print('the length is ',len(sen))

sen1=sen.replace("a","Z").replace("e","Z").replace("i","Z").replace("o","Z").replace("u","Z")
sen1.replace("A","Z").replace("E","Z").replace("I","Z").replace("O","Z").replace("U","Z")
print("Replaced vowel with Z : ",sen1)
