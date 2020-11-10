# Author : Sanjeev Sapre
# A program using exception to only copy numberic values to other list.
# NOTE: this may not be the best way to implement this requirement! the best way would be list comprehension
# list2 = [ i for i in list1 if type(i)== 'int']  
# A one liner!

list1 = [12, 34, 's' , 45, 78 , 'ww' , 34, 56 , 67]
list2 = []

for i in list1 :
    try:
        n = i + 0
    except: 
        # for demo purpose we are not HANDLING value error in first block rather just pass this section.
        pass
    else:
        list2.append(i)        

print(list2)