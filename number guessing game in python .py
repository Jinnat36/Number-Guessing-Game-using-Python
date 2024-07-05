import random
print('Computer Choose  Number Between "1-50"')
print("REMEMBER! YOU HAVE ONLY 5 CHANCE.")
random_number=random.randint(1,50)
t=1
while 5>=t:  
    user_input=int(input("ENTER YOUR GUSSE NUMBER : "))
    t+=1
    if user_input==random_number:
        print("YOU WIN")
        break
    elif user_input > random_number:
        print(f"{user_input} is too high.Try Again!")
    elif user_input<random_number:
        print(f"{user_input} is too low.Try Again!")
else:
    print(f"You Finished chances.")
print("THANK YOU FOR PLAY :)")
        
    
