# QUESTION 1: convert 45.67 into a float and int
# Question 2: Calculate the square and cube of a number entered by the user
# Question 3: Reverse the string "Python" without using reversed()
from tkinter import Variable

#Type Conversion
#num="45.67"
#print(float(num))

#num=45.67
#print(int(num))

# Square a number
#num=float(input("Enter a number "))
#print(num**2)
# Cube a number
#num=float(input("Enter a number "))
#print(num**3)


# Reverse String
#word="Python"
#print(word[::-1])


#List's in python
#Storage_Configuration=["128","256","512","1TB"]
#print(type(Storage_Configuration))       #Proof that the above is a list

#ANDROID=[True,int,float,str]    #Lists can hold any types
#print(type(ANDROID))

#for item in ANDROID:    # We use for in loop through each element in a sequence like a list, string, or range
#    print(True)         # This is an example of a list



#for I in range(len(ANDROID)): # use range to count and show each item; 'I' can be any name
#    print(I, ANDROID[2])

#Variable=[True,False,23,12.3]         # Another example of range
#for i in range(len(Variable)):
#    print(Variable[i], 111)



# Tuple is a collection which is ordered and unchangeable used to group together related data
#student = ("Bro",21,"male")

#print(student.count("Bro")) # .count function in this case checks how many times "Bro" appears inside the tuple
#print(student.index("male")) # .index tells you the position of that value inside the tuple (or list)

#for x in student:
    # go through each item in the tuple and print it
 #   print(x)

#if "Bro" in student:
    # check if "Bro" is inside the tuple, then print message if true
 #   print("Bro is here!")



#Practice Tuples:

#Body_Metrics=("70",178,"Male")
#print(Body_Metrics.count(178))
#print(Body_Metrics.index("70"))
#if 178 in Body_Metrics:
    #print("Welcome to the height club!")


#Phones=("APPLE","SAMSUNG","ONEPLUS")
#print(Phones.count("ONEPLUS"))
#print(Phones.index("SAMSUNG"))
#if "SAMSUNG" in (Phones):
#    print("Officially the best most innovative phone brand to exist!")


#set is a collection which is unordered, unindexed. No duplicate values

#utensils = {"fork","spoon","knife"}
#dishes = {"bowl","plate","cup","knife"}
#for x in utensils:
#    print(x)

# Practice set

#american_muscle={"Mustang GTD","Camaro ZL1","Challenger Hellcat Redeye"}
#german_sportscars={"BMW M8","SL63SE AMG","911 GT3RS"}
#for x in german_sportscars:
#    print("911 GT3RS")
#for x in american_muscle:
#    print("Mustang GTD")



# dict create a dictionary of a student
#student = {
#    "name": "Pramith",
#    "age": 20,
#    "major": "Computer Science",
 #   "GPA": 3.7
#}

#print(student["name"]) #Square brackets is a strict way of saying give me this value, and if it doesn't exist, crash the program
#print(student.get("GPA")) # .get means Get value; if missing, give None. .get only works for dict.


# Practice using dict

#Car_Terminology= {
 #  "horsepower": "How much power the car makes",
 #   "Torque": "Higher number lets the car accelerate quicker",
 #   "Weight": "If a car is heavier than its competitor by a few hundred pounds even while having similar horsepower still affects performance"
#}

#print(Car_Terminology.get("Weight"))
# print(Car_Terminology["horsepower"])







