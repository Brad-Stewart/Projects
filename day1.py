#Declaring Variables
name = "Edward Im"
age = 30
lists = [] #same as an array in javascript, operates the same way
float = 2.2
check = True
check1= False #boolean, True/False capitalized
dict = {
    "a" : 1 #keys for dictionaries must be in quotes
}
person = {
    "full_name" : "Edward Im" #colon is a seperater of key and value
}

#Loops
for i in range(0, 21, 2): #Third value is the increment (0-20 buy 2's) (increment -X will count down)
    print(i) #range function is exclusive of upper limit (21
print("FOR LOOP FINISHED")

#Conditions
for i in range(21, -1, -1):
    if i % 2 == 0:
        print("i is divisible by 2")
    elif i %2 == 1:  # elif cannot exist without an if statement
        print("i is not divisible by 2")
    else:
        print("something")
print("FOR LOOP FINISHED")

# F-Strings
first_name = "Edward"
last_name = "Im"
age = 30
print(f"Hello my name is {first_name} {last_name} I'm {age} years old")
#"Hello my name is Edward Im I'm 30"


#Functions

# DEFINE
# 1. FUNCTION NAME addTwoThings (lowerCamelCase) # First word lower case, all other words upper case
# 2. PARAMETERS - (a.b)
def addTwoThings(a, b):  #function followed by function name then ():
    c = a + b
    return c #takes input info and returns output
    #Return replaces the instance of the function

# CALL
print(addTwoThings(42, 56)) # Arguments - 42, 56
print(addTwoThings(1, 2))
print(addTwoThings(4,8))
print(addTwoThings("hello ","world"))
print(addTwoThings([1,2,3],"Hello")) #doesn't work

#PARAMETERS AND ARGUMENTS

# Return vs Print()

