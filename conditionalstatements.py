temperature = 56

if temperature > 37:
    print("It is too hot")
else:
    print("It is cold")

# Python program that returns the largest number among three numbers
num1 = 45
num2 = 34
num3 = 67
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# Assignment
# Write a program that checks whether a year is a leap year or not
# Python program that checks whether an alphabet is a vowel or consonant

year = 2023

if year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Assignment 2

letter = input("enter a letter")
if letter.lower() in ("a", "e", "i", "o", "u"):
    print("vowel")
elif letter.upper() in ("A", "E", "I", "O", "U"):
    print("vowel")
else:
    print("consonant")