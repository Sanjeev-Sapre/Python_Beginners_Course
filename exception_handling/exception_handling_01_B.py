# Author : Sanjeev Sapre
# A program to find percentage of marks with catch all exceptions
# Remember - There is no direct way to go back to the place where the exception occurred
# 
import sys

try:
    marks = int(input( "Enter Marks Obtained: "))
    total = int(input( "Enter Total Marks: "))

    percent = marks / total * 100
    sys.exit("Exiting program using sys exit")
    print( f"You got {percent}% marks.")

except: # catch all exceptions as we are not specifying anyone so USE WITH CARE ! 
        # Drawback - you may have some unexpected errors going unnoticed. 
        # Dawback 2 - Even system exit calls and Ctrl-C key combinations in Python trigger exceptions, and 
        # you usually want these to pass.
        # Drawback 3 - It will also catch genuine programming mistakes which you probably want to see error.
    print("Something went wrong !")
    
print('Continuing with the rest of the program..')
