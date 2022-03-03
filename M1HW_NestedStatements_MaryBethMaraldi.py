"""
Created on Thu Jan 27 17:27:35 2022

@author: MBMaraldi
"""
#   Determine the Largest Values
#   Jan 27, 2022
#   CSC-121 M1HW2-Nested Statements
#   Mary Beth Maraldi

#   Calculate and display 2 largest numbers and display results
#   
#   If largest number store as value
#   elif second largest number store value
    
#   Display Results

#   set variables max1 = largest, max2 = second largest to zero

#   create for loop gathering input of numbers
#       evaluate values of numbers, with if/elif 
#       display results

# Initialize variables
max1 = 0
max2 = 0
# n is the input number
# x is a place holder in case max1 is replaced by n. It would still need to be evaluated against max2.

# Process 10 numbers
for i in range (10):
    # Prompt to enter number
    n = int(input("Enter number:"))
    
    if n > max1:
        x = max1 # This is in case the old max1 is greater than the current max2
        max1 = n
    elif n > max2: # This allows the new number to become max2 if it was less than max1
        max2 = n
    elif x > max2: # This allows the old max1 to become max2 if it is greater
           max2 = x


# Display results
print(f'The largest valur is {max1}, the second largest value is {max2}.')
