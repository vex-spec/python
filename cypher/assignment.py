# 1. A simple python program to
#check whether a year is a leap year or not
from traceback import print_tb

year = 2023
if year % 4 ==0 and year % 100 !=0 :
    print(year,"is a leap year")
else:
    print(year,"Not a leap year")


# 2. A python prom that check whether a letter is a vowel or a consonat
letter = "K"
if letter=="A" or letter=="E" or letter=="I"  or letter =="O"or letter=="a" or letter=="e" or letter=="i" or letter=="o":
    print(letter,"is a vowel")
else:
    print(letter,"is a consonant")
