# From Question 2b:

courseCode = input("Please enter course code: ") # request user to enter course code input

if (courseCode == "CSC1006"):
    print("Mathematics 2")
elif (courseCode == "CSC1007"):
    print("Operating Systems")
elif (courseCode == "CSC1008"):
    print("Data Structures and Algorithms")
elif (courseCode == "CSC1009"):
    print("Object-Oriented Programming")
elif (courseCode == "CSC1010"):
    print("Computer Networks")
else:
    print("Unknown Module entered.") #if unable to match course code, throw unknown module

print("Odd numbers from 102 to 65:")

for i in range(102, 65, -1): # creates iterable from 102 to 66
    if (i % 2 == 1): # checks if i is an odd number
         print(f"Odd number: {i}")