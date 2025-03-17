# arthametic operator
# assignment operator
# compound assignment operator
# comparision operators
# logical operators
# membership operator
# output formatting strings

# arthametic operator
#additon(+)

# number_1 = 2050
# number_2 = 3050
# result = number_1 + number_2
# print(result)

#subraction(-)
# number_1 = 3050
# number_2 = 2050
# result = number_1 - number_2
# print(result)


#multiplication(*)

# number_1 = 2050
# number_2 = 3050
# result = number_1 * number_2
# print(result)

#division(quotent reply)(/)

# number_1 = 3090
# number_2 = 50
# result = number_1 / number_2
# print(result)

# #floor division(//)(quotent but not exact)

# number_1 = 3090
# number_2 = 50
# result = number_1 // number_2
# print(result)

#modulus(reminder)(%)(int)

# number_1 = 3090
# number_2 = 50
# result = number_1 % number_2
# print(result)

#exponetiation(**)

# number_1 = 20
# number_2 = 3
# result = number_1 ** number_2
# print(result)

# mixed arthamatic operation

# number_1 = 10
# number_2 = 10
# number_3 = 10
# result = number_1 + number_2 - number_3 * number_1 / number_2 // number_3 % number_1 ** number_2
# print(result)

# PEMDAS

# P - Parentheses ()
# E - Exponentiation **
# MD - Multiplication * and Division /, Floor Division //, Modulus % (from left to right)
# AS - Addition + and Subtraction - (from left to right)


#assignmnet operator

# num_1 = 5 
# num_1 += 5
# print(num_1)

# num_1 = 5 
# num_1 -= 5
# print(num_1)

# num_1 = 5 
# num_1 *= 5
# print(num_1)

# num_1 = 5 
# num_1 /= 5
# print(num_1)

# num_1 = 5 
# num_1 //= 5
# print(num_1)

# num_1 = 5 
# num_1 %= 5
# print(num_1)

# num_1 = 5 
# num_1 **= 5
# print(num_1)

# num_1 = 5 
# num_1 &= 5
# print(num_1)

# num_1 = 5
# num_1 |= 5
# print(num_1)

# num_1 = 5 
# num_1 ^= 5
# print(num_1)

# num_1 = 5 
# num_1 <<= 5
# print(num_1)

# num_1 = 5 
# num_1 >>= 5
# print(num_1)

# comparision operators

# num_1 = 5 
# num_2 = 10
# print(num_1 == num_2)

# num_1 = 5 
# num_2 = 10
# print(num_1 < num_2)

# num_1 = 5 
# num_2 = 10
# print(num_1 <= num_2)

# num_1 = 5 
# num_2 = 10
# print(num_1 > num_2)

# num_1 = 5 
# num_2 = 10
# print(num_1 >= num_2)

# num_1 = 5 
# num_2 = 10
# print(num_1 != num_2)

# name_1 = "santosh"
# name_2 = "ashok"
# print(name_1 >= name_2)


#logical operator
# num_1 = 5 
# num_2 = 10
# num_3 = 20
# print(num_1 < num_2 and num_2 > num_3)

# num_1 = 5 
# num_2 = 10
# num_3 = 20
# print(num_1 < num_2 and num_2 > num_3)

# num_1 = 5 
# num_2 = 10
# num_3 = 20
# print(num_1 < num_2 and num_2 < num_3)

# num_1 = 5 
# num_2 = 10
# num_3 = 20
# print(num_1 > num_2 and num_2 < num_3 or num_3 < num_2)

# num_1 = 5 
# num_2 = 10
# num_3 = 20
# print(not((num_1 > num_2 and num_2 < num_3 or num_3 < num_2)))

#Identity operators

# num_1 = [1,2,3]
# num_2 = num_1
# print(num_1 is num_2)
# print(id(num_1))
# print(id(num_2))

# num_1 = [1,2,3]
# num_2 = [1,2,3]
# print(num_1 is num_2)
# print(id(num_1))
# print(id(num_2))

# num_1 = [1,2,3]
# num_2 = [1,2,3]
# print(num_1 is not num_2)
# print(id(num_1))
# print(id(num_2))


#membership operators

# list_1 = ["santosh","ashok","nagaprasad","swathi","chinna"]
# print("santosh" in list_1)
# print("santosh" not in list_1)

#f_strings

# name = "santosh age is :"
# age = "25"
# santosh_age = name + age
# print(santosh_age)
# print(f"name is {name} and age is {age} totally ,santossh age is {santosh_age}")



#____________________tasks________________

 #Question: What do identity operators ( is and is not ) check in Python?
# memory address identity
 #Question: Which of the following statements is correct for the identity
#ans: x is y is True if x and y refer to the same object

#whatt do membership operators ( in and not in ) check in Python?
#ans:  Sequence membership
#witch membership operator is used to check if a value is not
#ans: is not

# create a program that takes user input for their name and age. Use
# formatted strings (f-strings) to print a message welcoming the user and
# stating their age

# name = input("enter your name please :")
# age = input("enter your age :")
# print(f"welcome to mexico mr {name} and your age is {age} ")

# write a Python script that defines a dictionary with information
# about a product (e.g., name, price, quantity). Use formatted strings to display
# the information in a readable format.


# dictionary_1 = {"name" : "samsung tv",
# "price" : 25000,
# "quantity" : 1}
# print(f"product name : {dictionary_1['name']}")
# print(f"product price : {dictionary_1['price']}")
# print(f"product quantity:{dictionary_1['quantity']}")

# create a list called numbers that contains integers from 1 to 10.
# Check if the number 5 is in the list.
# Check if the number 15 is not in the list.

# list = [1,2,3,4,5,6,7,8,9,10]
# print(5 in list)
# print(15 not in list)

# Write a Python program to calculate the area of a rectangle using the given
# formula: area = length * width . Take the values of length and width as inputs from
# the user

# length = float(input("enter the lenght of site :"))
# width = float(input("enter the width of the site :"))
# area = length * width
# print(area)




#Write a Python program to demonstrate incrementing and decrementing a variable

# number = 10
# number +=1
# print(f"after incrementing number : {number}")
# number -=1
# print(f"after decrementing number : {number}")

# Write a Python program to convert temperature from Celsius to Fahrenheit. The
# formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as
# input from the user.

# temperature = float(input("enter temperature in celsus :"))
# farenheat = (temperature * 9/5) + 32
# print(farenheat)



# Write a Python program to concatenate two strings and display the result. The
# strings should be taken as input from the user.




# name_1 = input("enter name one :")
# name_2 = input("enter name two :")
# cancat = name_1 + name_2
# print(cancat)

# Write a Python program to calculate the simple interest given the principal
# amount, rate, and time (in years).

# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the annual interest rate (in %): "))
# time = float(input("Enter the time period (in years): "))
# simple_interest = (principal * rate * time)/100
# print(simple_interest)

# kilometers = float(input("Enter the distance in kilometers: "))
# miles = kilometers * 0.621371
# print(miles)