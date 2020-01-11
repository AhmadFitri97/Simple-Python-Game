import random
print("Assalamualaikum")

name=input("What is your name:")

print("Welcome to Wan 2 Som Game")

print("Please choose below:")
user=eval(input("1-Rock 2-Water 3-Bird:"))

if user==1:
        print(name+" choose Rock")
elif user==2:
        print(name+" choose Water")
elif user==3:
        print(name+" choose Bird")


computer=(random.randint(1,3))
if computer==1:
        print("Computer choose Rock")
elif computer==2:
        print("Computer choose Water")
elif computer==3:
        print("Computer choose Bird")


if computer==user:
        print("Draw try again")
elif computer==1 and user==2:
        print(name+" You win!!")
elif computer==2 and user==3:
        print(name+" You win!!")
elif computer==3 and user==1:
       print(name+" You win!!")
else:    
       print(name+" You Lose!!")
