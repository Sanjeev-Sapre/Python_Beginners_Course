# Author : Sanjeev Sapre
# A program to find percentage of marks with catch all exceptions but we are getting details of what was the exception.
# import sys

try:
    marks = int(input( "Enter Marks Obtained: "))
    total = int(input( "Enter Total Marks: "))
    # sys.exit("Exiting program using sys exit")
    percent = marks / total * 100

except Exception as e: 
    print(f"Exception occurred -- ")
    print(f"\tText :{format(e)}")
    print(f"\tText: {type(e)}")
    print(f"\tText: {type(e).__name__}")

print('Continuing with the rest of the program..')

