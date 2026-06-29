class Team:
    
    __teamId=int
    __players=list()
    __win=bool()

    def __init__(self,players:list,teamId:int) -> None:
        self.__players=players
        self.__teamId=teamId

    def getPlayers(self) -> list:
        return self.__players
    
    def getTeamId(self) -> int:
        return self.__teamId
    
    def isWin(self) -> bool:
        return self.__win
    
    def __str__(self) -> str:
        return f"Team(players={self.__players})"