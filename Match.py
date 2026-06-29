import Account

class Match:

    __matchId: str
    __participants: list
    __teams: list
    __winnerTeam: int

    def __init__(self, matchId: str, participants: list, teams: list, winnerTeam: int) -> None:
        self.__matchId = matchId
        self.__participants = participants
        self.__teams = teams
        self.__winnerTeam = winnerTeam

    def getMatchId(self) -> str:
        return self.__matchId
    
    def getParticipants(self) -> list:
        return self.__participants
    
    def getTeams(self) -> list:
        return self.__teams
    
    def getWinnerTeam(self) -> int:
        return self.__winnerTeam
    
    def __str__(self) -> str:
        return (
            f"Match(matchId={self.__matchId}, participants={self.__participants}, "
            f"teams={self.__teams}, winnerTeam={self.__winnerTeam})"
        )