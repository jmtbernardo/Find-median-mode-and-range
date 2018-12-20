# The Program calculates the following; mean, median, mode, and range.


# User input values
print("This program is only designed to handle and work with values.")
print("To find the arithmetic mean answer following questions: ")
var1 = input("Enter first number: \n")
var2 = input("Enter Second number: \n")
var3 = input("Enter third number: \n")
var4 = input("Enter fourth number: \n")

# Equation for the mean
# Add all numbers, then divide by the total values, in this case there are total of 4 values
adding_numbers=int(var1)+int(var2)+int(var3)+int(var4)
mean=int(adding_numbers)/5

# Answer for  the mean
print("The mean number is "+ str(mean))


# User input values
print("To find the median answer following questions:")
var5 = input("Enter first number: \n")
var6 = input("Enter Second number: \n")
var7 = input("Enter third number: \n")
var8 = input("Enter fourth number: \n")

# The equation for mean will not answer right mean, if user inputs wrong ascending/descending order.
# This equation needs to be changed, because user might insert wrong order.
#list=[int(var5),+int(var6),+int(var7),+int(var8)]
#list.sort()
#how to add two integers inside of the list in python?
# Equation for median, median is found using numbers in the middle of the list
median=int(var6)+int(var7)

# Answer for the median
print("The median number is "+ str(median))

# User input values
print("To find the mode answer following questions:")
a = input("Enter first number: \n")
b = input("Enter Second number: \n")
c = input("Enter third number: \n")
d = input("Enter fourth number: \n")

# Equation and answer for the mode
# Comparison Statement being used to find the most repetitive number
if a == b or c:
    print("Your mode number is "+ str(a))
elif b==c or d:
    print("Your mode number is "+ str(b))
elif c==d or a:
    print("Your mode number is "+ str(c))
else:
    print("Your list does not have a mode")

# User input values
print("To find the range answer following questions: ")
print("To find the range provide the following:")
r1 = input("Enter first number: \n")
r2 = input("Enter Second number: \n")
r3 = input("Enter third number: \n")
r4 = input("Enter fourth number: \n")

# List of answers
list = [int(r1),+int(r2),+int(r3),+int(r4)]

# Function to find the highest number
highest= max(list)

# Function to find lowest number
lowest=min(list)

# Equation
range= highest - lowest

# Answer of range
print("The range number is "+ str(range))
