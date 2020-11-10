# Author : Sanjeev Sapre
# A program to find percentage of marks.

# This is same as previously seen, parenthesized version but you can provide seperate statemets for each type 
# of excpetion in this format. 

marks_list = {"Student1": 25,  "Student1": 17, "Student1": 18, "Student1": 21, "Student1": 16, "Student1": 9, "Student1": 23 }

for key, value in marks_dict:
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
