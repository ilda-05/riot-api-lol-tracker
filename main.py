from functions import *


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
        
        if user_input == "0":
            break
        elif user_input == "1":
            playerName=input("Player Name : ")
            playerTag=input("Player Tag : ")
            print("Loading...")
            player = searchPlayer(playerName,playerTag)
            games = searchPlayerMatches(player.getPuuid())
            matchesInfo(games,player)
        else:
            continue

if __name__ == "__main__":
    main()
