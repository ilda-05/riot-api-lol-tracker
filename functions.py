import requests
from api_key import API_KEY
from Player import Player

#Checks if the player exists and then return the Object Player
def searchPlayer(playerName, playerTag):
    req = requests.get("https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}?api_key={api}".format(name=playerName,tag=playerTag,api=API_KEY))
    print("https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}?api_key={api}".format(name=playerName,tag=playerTag,api=API_KEY))
    print("ok")
    print(req.status_code)
    if(req.status_code==200):
        content = req.json()
        puuid=content["puuid"]
        name=content["gameName"]
        tag=content["tagLine"]
        return Player(puuid,name,tag)
    elif(req.status_code==404):
        print("Player not found")



def searchPlayerMatches(puuid):
    
    req = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{playerPuuid}/ids?start=0&count=10&api_key={api}".format(playerPuuid=puuid,api=API_KEY))
    print("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{playerPuuid}/ids?start=0&count=10&api_key={api}".format(playerPuuid=puuid,api=API_KEY))
    idMatches = req.json()
    return idMatches

def matchesInfo(games,player):

    stat_games = []

    for game in games:
        req = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/{idGame}?api_key={api}".format(idGame=game,api=API_KEY))
        content = req.json()
        info_game=content["info"]
        info_participants = info_game["participants"]
        for participant in info_participants:
            if participant["puuid"] == player.getPuuid():
                stat_games.append("Stats : {champ} {kills}/{deaths}/{assists}".format(kills=participant["kills"],deaths=participant["deaths"],assists=participant["assists"], champ=participant["championName"]))
                break

    for game in stat_games :
        print(game)
    
            




    
    
    
