# Author : Sanjeev Sapre
# A program to find percentage of marks.


print("Starting the programm.")

# for demo purpose we are not handling value error in first block. 
try:
    marks = int(input( "Enter Marks Obtained: "))
    total = int(input( "Enter Total Marks: "))
    
    percent = marks / total * 100
    print( f"You got {percent}% marks.")

finally:
    # you can use just finally , except is not needed by synaxt. 
    # what is the use case for this? 
    print("This finally is there and will run everytime even if the code inside the try fails  ..")

