from functions import *
import os

def clr():

    os.system('cls' if os.name == 'nt' else 'clear')

player_cache=dict()
match_cache=list()
match_details_cache=dict()


def main():

    clr()
    checksApiKey()  
        
    while(True):
        
        # Menu'

        print("\n--------------------")
        print("0 - Exit")
        print("1 - Search Player")
        print("--------------------\n")

        user_input = input("Choose : ")

        clr()
        
        # Stops the execution
        if user_input == "0":

            break

        # Searches for a player details
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
                games_details=list()
                
                for game in games:
                    if game not in match_cache:
                        match_cache.append(game)

                print(match_cache)
                games_details=matchesInfo(games,player)
                for game_details in games_details:
                    match_details_cache.update({game:game_details})
                    print(game)

            else:
                print("Player not found")

        elif user_input == "2":
            print(player_cache)
        
        elif user_input == "3":
            print(match_cache)

        elif user_input == "4":
            print(match_details_cache)

        else:
            continue

if __name__ == "__main__":

    main()
