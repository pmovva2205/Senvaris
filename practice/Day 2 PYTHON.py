#NOTES
from xmlrpc.client import APPLICATION_ERROR

# .upper() makes everything uppercase. "hello".upper() prints "HELLO"
# .lower() makes everything lowercase. "HELLO".lower() prints "hello"

# .strip() removes spaces (or special characters) from the beginning and end.
#   Example of .strip() : "   hi   ".strip() prints "hi"

# .replace("a", "b") swaps characters
#    Example of .replace() : "banana".replace("a","o") prints "bonono"

# .split(",") breaks a string into a list based on a separator.
#     Example of .split(",") : "a,b,c".split(",") prints ["a", "b", "c"]

# .join(list) combines items from a list into one string.
#     Example of .join() : " ".join(["I", "love", "Python"]) prints I love Python


#Execution
# .upper() practice
#Mustang= "only real car guy's buy mustangs with v8's"
#print(Mustang.upper())

#muscle_cars= "who on planet earth would buy a muscle car without a v8?"
#print(muscle_cars.upper())

# .lower() practice

#German_cars= "german cars are great but overrated ash and too many components affecting reliability"
#print(German_cars.lower())

#JDM_CARS= "Often sound hilarious due to crappy driver mods but with proper upgrades they sound crisp and perform great"
#print(JDM_CARS.lower())

# .replace(",") practice

#Elec_build="APPLE"
#print(Elec_build.replace("A","O"))

#ios_opperating_sys="10"
#print(ios_opperating_sys.replace("1","2"))

#.split(",")

#top_phone_brands="Apple,Samsung,Google,Oneplus"
#print(top_phone_brands.split(","))

#beverages="Monster,RedBull,BANG,Celsius"
#print(beverages.split(","))

#.join()

#HP=["Mustang","Camaro","Dodge"]
#print(",".join(HP))
#print("𓃗".join(HP))
#print("😈".join(HP))
#print("🇨🇦".join(HP))

#fruit="Apple,Banana,Strawberry"
#print(" ".join(fruit))


#GPT EXAMPLE:

#joy="happiness"
#print(joy.upper().strip())

#ANOTHER EXAMPLE:

#content=["joy" , "happiness"]
#print((",").join(content))


# Daily Practice
# Q1: Take a string and count how many vowels it has
# Q2: Replace all spaces with underscores in "I love Python" (Use.replace(" ", ", "_"))
# Q3: Check if "racecar" is a palindrome (same forward and backward). (Compare the string with string[::-1])

#Q1: Counts how many vowels are in a string
#text = input("Text: ")

#count = 0  #Starts counter at 0

#for character in text: #goes through each character in the input
#    if (character in "aAeEiIoOuU"): #checks if the character is a vowel
#        count += 1 #adds 1 if it is a vowel
#print("count:", count)    #prints the total number of vowels


# Q1 cont another example:

# #text = input("Enter Your Name: " )

#count =  0

#for character in "Enter Your Name ":
#    if (character in "JOE"):
#        count += 1

#print("count:", count)


#Q1 continued another example:

#superhero=input("Enter your favorite superhero ")

#count=0

#for character in superhero:
#    if character in "AaEeIiOoUu":
#        count += 1

#print("Count:",count)


# Q1 Last example

#Protein=input("I can't hit my protein")

#count = 0

#for i in Protein:
#    if i in "AaEeIiOoUu":
#        count += 1  # anytime you see any vowel what happens is 1 gets added so if we have 11 vowels its 11
#print("Count: ", count)  # this means show the word count and also the number stored in count



# Q2: Replace all spaces with underscores in "I love Python" (Use.replace(" ", ", "_"))

#intrests="I Love Python!"
#print(intrests.replace(" ","_"))

# Q2: Another Example

#Laptops="Macbook,Lenovo,Dell"
#print(Laptops.replace(","," "))


# Q3: Check if "racecar" is a palindrome (same forward and backward). (Compare the string with string[::-1])

#car="racecar"
#print(car[::-1])




