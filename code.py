
# GUESS_A_NUMBER_GAME                                

import random

targetvalue = random.randint(1,100)
count = 0
while True :
    choice = int(input("guess the target :"))
    count = count+1
    if(count==5):
        print("\n----^^^you loss game^^^----\n")
        print("----***TRY AGAIN LATER***----")
        break
    
    
    if choice==targetvalue :
        print("\nsuccess : correct guess !!\n")
        break
    elif (choice<targetvalue):
        print(("your number was to small , take a bigger guess...!!"))
    else:
        print(("your number was to big , take a smaller guess...!!"))


print("---***---GAME OVER---***---")
