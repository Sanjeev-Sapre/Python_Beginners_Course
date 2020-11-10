# Author : Sanjeev Sapre
# A program to find percentage of marks.


try:
    print("Starting the programm.")

    # for demo purpose we are not handling value error in first block.  
    # INFO:  - if the exception does not match in this try block, then the exception is propagated
    # to the next most recently entered try statement that matches the exception; if no such matching 
    # try statement can be found and the search reaches the top level of the process, Python kills 
    # the program and prints a default error message.
    try:
        marks = int(input( "Enter Marks Obtained: "))
        total = int(input( "Enter Total Marks: "))
        
        percent = marks / total * 100
        print( f"You got {percent}% marks.")

    except ZeroDivisionError:
        print("The total can not be Zero!")
    finally:
        # this is an example but the main purpose is to close the files or network corrections or db connection.
        # Remember the finally caluse runs always !
        # NOTE: The code in the finally-block will be run even if there is an error in 
        # - exception handler or 
        # - else-block and a new exception is raised.

        print("Catching the non numeric is not done at level 1, it will propagate to next level..")

except ValueError:
    print("You have entered non numeric value.")

print('Continuing with the rest of the program..')