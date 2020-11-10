# Author : Sanjeev Sapre
# A program to find percentage of marks.


try:
    marks = int(input( "Enter Marks Obtained: "))
    total = int(input( "Enter Total Marks: "))
    
    percent = marks / total * 100
    print( f"You got {percent}% marks.")

except ZeroDivisionError:
    print("The total can not be Zero!")

except ValueError:
    print("You have entered non numeric value.")

print('Continuing with the rest of the program..')