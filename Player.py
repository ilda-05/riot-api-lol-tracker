from Account import Account
class Player:

    __account:Account
    __kills:int
    __deaths:int
    __assists:int
    __champion:str
    __role:str

    def __init__(self,account:Account,kills:int,deaths:int,assists:int,champion:str,role:str) -> None:
        self.__account = account
        self.__kills = kills
        self.__deaths = deaths
        self.__assists = assists
        self.__champion = champion
        self.__role = role

    def get_account(self) -> Account:
        return self.__account

    def get_kills(self) -> int:
        return self.__kills

    def get_deaths(self) -> int:
        return self.__deaths

    def get_assists(self) -> int:
        return self.__assists

    def get_champion(self) -> str:
        return self.__champion

    def get_role(self) -> str:
        return self.__role

    def __str__(self) -> str:
        return (
            f"Player(account={self.__account}, "
            f"kills={self.__kills}, deaths={self.__deaths}, "
            f"assists={self.__assists}, champion='{self.__champion}', "
            f"role='{self.__role}')"
        )
