from functions import *
import os

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

###
# 
# 0 Exit
#
# 1 Search Player
#
# 2 Champions Rotation
#  
###

def main():

    checksApiKey()  
    
    while(True):


        
        # Menu'

        print("0 - Exit")
        print("1 - Search Player")
        user_input = input("Choose : ")

        clr()
        
        if user_input == "0":
            break
        elif user_input == "1":
            playerName=input("Player Name : ")
            playerTag=input("Player Tag : ")
            clr()
            print("Loading...")
            player = searchPlayer(playerName,playerTag)
            games = searchPlayerMatches(player.getPuuid())
            clr()
            matchesInfo(games,player)
        else:
            continue

if __name__ == "__main__":
    main()
