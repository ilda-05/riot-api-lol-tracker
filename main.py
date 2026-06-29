from functions import *
import os

def clr():

    os.system('cls' if os.name == 'nt' else 'clear')

# Cache Variables
account_cache=dict()
match_cache=list()
match_details_cache=dict()


def main():

    clr()
    checksApiKey()  
        
    while(True):
        
        # Menu'

        print("\n--------------------")
        print("0 - Exit")
        print("1 - Search account")
        print("--------------------\n")

        user_input = input("Choose : ")

        clr()
        
        # Stops the execution
        if user_input == "0":

            break

        # Searches for a account details
        elif user_input == "1":

            
            accountName=input("account Name : ")
            accountTag=input("account Tag : ")

            print("Loading...")
            
            if accountName+"#"+accountTag in account_cache:

                account = account_cache[accountName+"#"+accountTag]

            else:

                account = searchAccount(accountName,accountTag)

            if account != None:

                account_cache.update({accountName+"#"+accountTag:account})
                games = searchAccountMatches(account.getPuuid())
                games_details=list()
                
                for game in games:
                    if game not in match_cache:
                        match_cache.append(game)

                print(match_cache)
                games_details=matchesInfo(games)
                for game_details in games_details:
                    match_details_cache.update({game:game_details})
                    print(game)

            else:
                print("account not found")

        elif user_input == "2":
            print(account_cache)
        
        elif user_input == "3":
            print(match_cache)

        elif user_input == "4":
            print(match_details_cache)

        else:
            continue

if __name__ == "__main__":

    main()
