import random

def rolldice():
    min_num=1
    max_num=6
    rolldice=random.randint(min_num,max_num)
    return rolldice

print("                                             WELCOME TO THE SPICE DICE GAME!                              ")
print("Rules of the game:\n#Keep rolling till you reach the max score of 50\n#On a 1 your turn gets over\n\n##HAVE FUN & BEST OF LUCK!##")

while True:
    players=input("\nEnter the number of players(2 - 5): ")
    if players.isdigit():
        players=int(players)
        if 2 <= players <=5:
            break
        else:
            print("Should be between 2 - 5 players!")
    else:
        print("Invalid,please try again!")

max_score=50
score=[0 for i in range(players)]

while max(score) < max_score:

    for index in range(players):
        print("\nPlayer",index + 1,"begins the game!")
        print("\nYOUR TOTAL SCORE IS : ",score[index],"\n")
        current_score = 0

        while True:

            roll=input("WOULD YOU LIKE TO ROLL THE DICE (y/n)?")
            if roll.lower() !="y":
                break 
            else:
                value = rolldice()
                if value==1:
                    print("\nOOPS!!!!!\nYOU ROLLED A 1\nTURN OVER!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print("\nYOU ROLLED A : ",value)

                print("\nYOUR SCORE IS : ",current_score)

        score[index] += current_score
        print("\nYOUR TOTAL SCORE IS : ",score[index])
        
max_score = max(score)
win_index = score.index(max_score)

print("CONGRATULATIONS!\nPLAYER NUMBER ",win_index + 1,"IS THE WINNER WITH A SCORE : ",max_score)















        
