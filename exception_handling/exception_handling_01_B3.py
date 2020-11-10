# Author : Sanjeev Sapre
# A program to find percentage of marks.
# introducitng else

try:
    marks = int(input( "Enter Marks Obtained: "))
    total = int(input( "Enter Total Marks: "))
    
    percent = marks / total * 100
    

except Exception as e: 
    print(f"Exception occurred -- ")
    print(f"\tText :{format(e)}")
    print(f"\tText: {type(e)}")
    print(f"\tText: {type(e).__name__}")
# else runs only if any exception was not raised. 
# else is for except, meaning if you do not add except then you can not add else.
else :
    print( f"You got {percent}% marks.")

print('Continuing with the rest of the program..')
