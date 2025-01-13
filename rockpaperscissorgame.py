import random
choices=["rock","paper","scissors"]
user_score=0
computer_score=0
rounds=int(input("enter the no of rounds you want to play:"))
for i in range(rounds):
    user_choice=input("\n enter 'rock','paper',or,'scissors':").lower()
    if user_choice not in choices:
        print("invalid choice! please enter 'rock','paper',or'scissors':")
        continue
    computer_choice=random.choice(choices)
    print(f"computer's choice:{computer_choice}")
    print(f"your choice:{user_choice}")
    if user_choice==computer_choice:
     print("it's a tie")
    elif(user_choice=='rock' and computer_choice=='scissors')or\
     (user_choice=='paper' and computer_choice=='rock')or\
     (user_choice=='scissors'and computer_choice=='paper'):
        print("you win this round!")
        user_score+=1
    else:
        print("computer wins this round!")
        computer_score+=1
    #display current scores
    print(f"current scores = you:{user_score},computer: {computer_score}")
print("\nGame Over!")
print(f"final scores = you :{user_score},Computer :{computer_score}")

if user_score>computer_score:
    print("congrats,you are the overall winner!")
elif user_score<computer_score:
    print("Computer is the overall winner!,better luck next time")
else:
    print("it's an overall tie")
    
