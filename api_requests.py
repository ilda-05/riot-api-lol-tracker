import requests
from api_key import API_KEY

def accountByNameTag(name:str,tag:str) -> requests.Response:
    return requests.get("https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}?api_key={api}".format(name=name,tag=tag,api=API_KEY))
    
def matchesIdByAccountPUUID(puuid:str):
    return requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{AccountPuuid}/ids?start=0&count=10&api_key={api}".format(AccountPuuid=puuid,api=API_KEY))

def matchInfoByIdGame(matchId:list) -> requests.Response:
    return requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/{matchId}?api_key={api}".format(matchId=matchId,api=API_KEY))