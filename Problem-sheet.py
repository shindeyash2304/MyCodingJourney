# Problem 1:

# Write a Python program to store and print the details of a student (Name, Age, CGPA) using variables.

Name = "Yash"
Age = 21
CGPA = 6.5

print ("Student Details:")
print ("Name:",Name)
print ("Age:",Age)
print ("CGPA:",CGPA)

# Problem 2:

# Write a Python program to take two numbers as input and print their sum, difference, product, and quotient.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = (a+b)
print ("The addition of 'a' and 'b' is:", c)
d = (b-a)
print ("The difference between 'a' and 'b' is:", d)
e = (a*b)
print ("The product of 'a' and 'b' is:", e)
f = (a//b)
print ("The quotiont of 'a' and 'b' is:", f)

# Problem 3:

# Write a Python program that asks the user for their birth year and calculates their age in 2025.

ur_by = int(input("Enter your birth year: "))
ur_ag = 2025 - ur_by
print ("Your age is: ",ur_ag)

# Problem 4:

# Convert a temperature given in Celsius to Fahrenheit using the formula:
# Fahrenheit = (Celsius * 9/5) + 32
# Take Celsius as input from the user and display the result.

C = int(input("Enter Celcius in Degrees: "))
F = (C * 9/5) + 32
print (" Celcius to Fahrenheite is: ",F)

# Problem 5:

# Write a Python script that swaps two numbers without using a third variable.

a = (int(input("Enter 1st number: ")))
b = (int(input("Enter 2nd number: ")))

a, b = b, a
print (a)
print (b)

# #Write a program that asks the user for their name, age, and favorite color, then prints them

name = input("What is you name?")
dob = int(input("What is you Date Of Birth?"))
age = (2025 - dob)

print ("Hello!", name)
print ("Your age is: ", age)

#Write a program that asks the user for their name, age, and favorite color, then prints them.

age = int(input("Enter your age: "))
if age >= 18:
    print ("You are an adult")
else:
    print("You are minor")

#Take a number as input and check whether it is even or odd.

num = int(input("Enter the number: "))
if num % 2 == 0:
    print (num, "is an even number")
else:
    print (num , "is an odd number")

#Take marks as input and print "Pass" if marks >= 40, else print "Fail".
marks = int(input("Enter you marks: "))
if marks >= 40:
    print ("Congratulations!! you are passed <3")
else:
    print("paisa barbad")

# Practice Problems

# Problem 1:
# Write a Python program that takes 3 numbers as input and prints the largest among them.

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))

if a > b:
    print ("a is largest")
elif b > c:
    print ("b is largest")
else:
    print ("c is largest")


# Problem 2:
# Write a program that checks whether a given year is a leap year or not. (A year is a leap year if it is divisible by 4 but not divisible by 100, except if it is also divisible by 400.)

year = input("Enter the year: ")
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print (year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
            print(year, "is a leap year")
else:
            print(year, "is not a leap year")
            
year = int(input("Enter the year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a leap year")
            else:
                print(year, "is not a leap year")
        else:  # Divisible by 4 but not 100
            print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
            
# Problem 3:
# Write a program that takes an integer as input and checks if it is positive, negative, or zero.

num = int(input("Enter a number: "))
if num > 0:
    print (num, "is a positive")
elif num == 0:
    print ("zero")
else:
    print (num, "is a negative")

# Problem 4:
# Write a Python program that takes two numbers as input and performs division. If the second number is zero, print "Division by zero is not allowed."

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

if b == 0:
    print ("Zero is not allowed")
else:
    div = a / b
    print (div)


# Problem 5:
# Write a Python program that asks the user to enter a password and checks if it matches "Python123". If the password is correct, print "Access Granted", otherwise print "Access Denied".

Password = "Python123"
PW = input("Enter Password: ")

if PW == Password :
    print("Access Granted")
else:
    print("Acess Denied")
