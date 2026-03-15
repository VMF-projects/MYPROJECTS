#
# ██╗   ██╗███╗   ███╗███████╗
# ██║   ██║████╗ ████║██╔════╝
# ██║   ██║██╔████╔██║█████╗
# ╚██╗ ██╔╝██║╚██╔╝██║██╔══╝
#  ╚████╔╝ ██║ ╚═╝ ██║██║
#   ╚═══╝  ╚═╝     ╚═╝╚═╝   
#
# PYGUESS GAME v1.1

game_lives=0
attempt=0
max_digit=0
gmode="0"
rndm=0
import random
def guesser(anti_guess):
    if rndm==1:
        print(f"Maybe go lower\nlives left: {game_lives}\n")
        return anti_guess
    else:
        return False
while True:
    mode_ask=input("Choose your gamemode: Hardcore / Average / Babymode\n:").lower()
    if mode_ask=="hardcore" or "1":
        game_lives=10
        max_digit=10000
        gmode="Hardcore mode"
        break
    elif mode_ask=="average" or "2":
        game_lives=15
        max_digit=1000
        gmode="Average mode"
        break
    elif mode_ask=="babymode" or "3":
        game_lives=75
        max_digit=10
        gmode="Babymode"
        break
    else: 
        print("Not a valid option!\n")
num=random.randint(1,max_digit)
print(f"\nYou choose {gmode} \nyou have {game_lives} lives\n")
while True:
    rndm=random.randint(1,4)
    try:
        guess=int(input("Choose your guess: "))
    except:
        print("Enter a valid number!\n")
        continue
    if guess==num:
        attempt+=1
        print(f"You won!\n{attempt} attempts\n{game_lives} lives left")
        break
    elif guess>num:
        if guesser(1):
            game_lives-=1
            attempt+=1
            continue
        print(f"Maybe go lower\nlives left: {game_lives}\n")
        game_lives-=1
        attempt+=1
    elif guess<num:
        if guesser(1):
            game_lives-=1
            attempt+=1
            continue
        print(f"Maybe go higher\nlives left: {game_lives}\n")
        game_lives-=1
        attempt+=1
    if game_lives==0:
        print(f"\nYou lose!\nThe number was {num}\n")
        break