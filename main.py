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
    while(True):
        print("0 - Exit")
        print("1 - Search Player")
        user_input = input("Choose : ")
        if user_input == "0":
            break
        elif user_input == "1":
            playerName=input("Player Name : ")
            playerTag=input("Player Tag : ")
            player = searchPlayer(playerName,playerTag)
            print(player)
            games = searchPlayerMatches(player.getPuuid())
            matchesInfo(games,player)
        else:
            continue

if __name__ == "__main__":
    main()
