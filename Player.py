class Player:

    __puuid=str
    __name=str
    __tag=str

    def __init__(self,puuid,name,tag):
        self.__puuid=puuid
        self.__name=name
        self.__tag=tag

    def getPuuid(self):
        return self.__puuid
        
    def getName(self):
        return self.__name
    
    def getTag(self):
        return self.__tag
    
    def __str__(self):
        return "Player(puuid={}, name={}, tag={})".format(self.__puuid,self.__name,self.__tag)

