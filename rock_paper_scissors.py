import random
def play_game():
    user_score=0#user score
    comp_score=0#computer score
    ch = ['rock', 'paper', 'scissors']
    
    user_ch = input("Choose rock, paper, or scissors: ").lower() #user choice
    comp_ch = random.choice(ch) #computer choice
    
    print("You chose:", user_ch)
    print("Computer chose:", comp_ch)
    if user_ch == comp_ch:
        print("It's a tie!")    
    elif (user_ch == 'rock' and comp_ch == 'scissors') or (user_ch== 'paper' and comp_ch == 'rock') or (user_ch == 'scissors' and comp_ch == 'paper'):
        print("You win!")
        user_score=user_score+1
    else:
        print("Computer wins!")
        comp_score=comp_score+1
    print("user score:",user_score,"computer score:",comp_score)
    play_again=input("do you want to paly game:(yes/no)").lower()
    if(play_again=="yes"):
        play_game()
    else:
        while False:
          print("thanks for playing")
          break
play_game()   
