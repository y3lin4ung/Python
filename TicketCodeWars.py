#!/usr/bin/python
import sys

money = []
print ("Enter Customers' Bill : \n\t\t\t25 25 25\n\n\n")
money = [int(x) for x in raw_input("> ").split()]
chkmoney = 0
i = 0
for i in range(len(money)):
    if(money[i] == 25):
        chkmoney += money[i]
    elif(money[i] == 50):
        if(chkmoney != 0 and (chkmoney % 50)!=0):
            chkmoney += 25
        else:
            print("No! The change is out of the Clerk!")
            sys.exit(0)
    elif(money[i] == 100):
        if(chkmoney > 50 and (chkmoney%100)!=0):
            chkmoney += 25
        else:
            print("No! The change is out of the Clerk!")
            sys.exit(0)
    else:
        print("Wrong Input! \n \t Try Again!!")
        sys.exit(0)
print ("Yes! It's Succeed!")


#4ung
