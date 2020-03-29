import re

userInput = input("Enter a MobileNumber or VehicleNumber")
regexMobSrc = "\d{10}"
regexVehSrc = "^[a-z]{2}\d{2}[a-z]{2}"


if(re.search(regexMobSrc, userInput, re.M|re.I)):
    print("Input is mobile Number")
elif(re.search(regexVehSrc, userInput, re.M|re.I)):
    print("Input is vehicle Number")
else:
    print("Invalid entry")