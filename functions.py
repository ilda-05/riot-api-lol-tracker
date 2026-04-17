import requests
from api_key import API_KEY
from Player import Player
from Match import Match

def checksApiKey():
    if(API_KEY==None):
        print("Api key missing")
        exit()

# Checks if the player exists
# then return the Object Player
# Return type : Player
def searchPlayer(playerName, playerTag):
    req = requests.get("https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}?api_key={api}".format(name=playerName,tag=playerTag,api=API_KEY))
    if(req.status_code==200):
        content = req.json()
        puuid=content["puuid"]
        name=content["gameName"]
        tag=content["tagLine"]
        return Player(puuid,name,tag)
    elif(req.status_code==404):
        print("Player not found")


# Returns the id of last 10 games of the player
# Return type : list
def searchPlayerMatches(puuid:Player):
    
    req = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{playerPuuid}/ids?start=0&count=10&api_key={api}".format(playerPuuid=puuid,api=API_KEY))
    idMatches:list = req.json()
    print(type(idMatches))
    return idMatches

# Return the details of the game
# Return type : list
def matchesInfo(list_matchId:list):

    stat_games = []
    matchId = str()

    for game in list_matchId:
        req = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/{idGame}?api_key={api}".format(idGame=game,api=API_KEY))
        content = req.json()

        metadata=content["metadata"]

        matchId=metadata["matchId"]

        info_game=content["info"]
        info_participants = info_game["participants"]

        for participant in info_participants:
            if participant["puuid"] == player.getPuuid():
                stat_games.append("Stats : {champ} {kills}/{deaths}/{assists}".format(kills=participant["kills"],deaths=participant["deaths"],assists=participant["assists"], champ=participant["championName"]))
                break

    return stat_games
    
            




    
    
    
