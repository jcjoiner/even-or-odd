# Problem Set 4
# Even or Odd

'''
    Write a Python program that determines whether a given number is even or odd.
'''

# Ask user for a number
# Check if number is even or odd
# print() result to user

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even!")
else:
    print(f"{number} is odd!")
