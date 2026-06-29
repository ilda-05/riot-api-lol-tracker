import requests
from api_key import API_KEY
from Account import Account
from Match import Match
from Team import Team
from api_requests import *

# This is not ok, to define
# Checks only if the api key is not missing
# It needs to check if it's valid too
def checksApiKey():

    if(API_KEY==None):
        print("Api key missing")
        exit()

# Checks if the Account exists
# then return the Object Account
# Return type : Account
def searchAccount(accountName, accountTag) -> Account | None:

    req = accountByNameTag(accountName,accountTag)
    if(req.status_code==200):
        content = req.json()
        puuid=content["puuid"]
        name=content["gameName"]
        tag=content["tagLine"]
        return Account(puuid,name,tag)
    elif(req.status_code==404):
        print("Account not found")


# Returns the id of last 10 games of the Account
# Return type : list
def searchAccountMatches(puuid:Account) -> list:
    
    req = matchesIdByAccountPUUID(puuid)
    idMatches:list = req.json()
    print(type(idMatches))
    return idMatches

# Return the details of a list of games
# Return type : list (Match)
def matchesInfo(list_matchId:list) -> list:

    stat_games = []
    matchId = str()
    matchesInfo = list()

    for matchId in list_matchId:

        req = matchInfoByIdGame(matchId)
        content = req.json()
        metadata=content["metadata"]
        info=content["info"]

        account=metadata["participants"]
        matchId=metadata["matchId"]
        players=info["participants"]        

        winnerTeam = int()
        teams = list()

        playersTeam100 = list()
        playersTeam200 = list()
        
        for player in players:

            kills=player["kills"]
            deaths=player["deaths"]
            assists=player["assists"]
            role=player["role"]

            if player["teamId"]==100:
                playersTeam100.append(player)
            elif player["teamId"]==200:
                playersTeam200.append(player)

                
        teams.append(playersTeam100,playersTeam200)

        match=Match(matchId,players,teams,)

        matchesInfo.append(match)

    return stat_games
    
            




    
    
    
