import random


def Roll():
    min_val = 1
    max_val = 6
    Roll= random.randint(min_val,max_val)
    return Roll


while True :
    Players=input("Please enter number of player (2-4) : ")
    if Players.isdigit():
        Players=int(Players)
        if 2<= Players <= 4:
            break
        else :
            print("The player min is 2 max is 4 !!!")
            continue
    else :
        print( " invalid , try again ") 


max_score=50
player_scores=[0 for _ in range (Players)]

while True:

    if max(player_scores) >= max_score:
        break  


    for player_idx in range(Players):
         
        current_score=0
        print("\nPlayer ",player_idx+1," turn just started! \n")
        print 
        while True:
            if player_scores[player_idx] >= max_score:
                break
            
            chosee=input ("Do you want to roll (y/n) : ")
            if chosee.lower()!='y':
                break
            else :
                value=Roll()

            if value == 1:
                print ("You roll 1 ! Turn Done !!!")
                player_scores[player_idx]=0
            else :
                print("You roll ",value)
                player_scores[player_idx]+=value
            print("Your total score is ",player_scores[player_idx])
            
    
        if player_scores[player_idx] >= max_score:
             break
    
winner_idx = player_scores.index(max(player_scores))
print("\nPlayer", winner_idx + 1, "wins with a score of", player_scores[winner_idx], "!")


     