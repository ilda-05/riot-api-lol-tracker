from functions import *
import os

def clr():

    os.system('cls' if os.name == 'nt' else 'clear')

player_cache=dict()

def main():

    clr()
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
            print("Loading...")
            
            if playerName+"#"+playerTag in player_cache:

                player = player_cache[playerName+"#"+playerTag]

            else:

                player = searchPlayer(playerName,playerTag)
                player_cache.update({playerName+"#"+playerTag:player})
                print(player)

            if player != None:

                games = searchPlayerMatches(player.getPuuid())

                matchesInfo(games,player)

            else:

                print("Player not found")

        elif user_input == "2":

            print(player_cache)

        else:

            continue

if __name__ == "__main__":

    main()
