# Author : Sanjeev Sapre
# A program to find percentage of marks.

# NOTE: This shows Python’s default exception-handling behavior, that is it stops the program and prints an 
# error message on the screen. we also call it as Traceback
# if you dont want this to happen then use try... except.

marks = int(input( "Enter Marks Obtained: "))
total = int(input( "Enter Total Marks: "))

percent = marks / total * 100
print(f"You got {percent}% marks.")









