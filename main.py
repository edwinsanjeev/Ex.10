# Programmer: Edwin Sanjeev
# Date: 01/8/2022
# Description: Exercise 10
from math import *
from sys import *

# Ask the user what interval to count by
count_by = int(input("What should I count by? "))
print()

if count_by < 0:
    print("We must count by a positive number!", file=stderr)
# Ask the user for the start and end numbers

start = int(input("What number should I start on? "))
print()

end = int(input("What number should I end on? "))
print()


if end < start:
    print("The ending number can't be before the starting number!")
answer = start + count_by 

print(start)

# While loop
while (answer < end): 
  print(answer) 
  answer= answer + count_by




    


