#Practical Example 4: Print this pattern using nested for loop: 
"""   
* 
** 
*** 
**** 
*****
"""

for r in range(1,6):
    for c in range(1,r+1):
        print('*',end="")
    print()
