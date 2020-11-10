# Author : Sanjeev Sapre
# A program to find percentage of marks.

try:
    marks = int(input( "Enter Marks Obtained: "))
    total = int(input( "Enter Total Marks: "))
    
    percent = marks / total * 100
    print( f"You got {percent}% marks.")

except (ZeroDivisionError, ValueError):
    print("Either you entered non number or Zero as total!")

print('Continuing with the rest of the program..')
