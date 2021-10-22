

class MySQL:
    Host: str
    User: str
    Password: str
    DBName: str
    Port: int
    def __init__(self,data) -> None:
        print(data)
        self.__dict__ = data

class Config: 
    mySQL:MySQL
    def __init__(self,data) -> None:
        self.__dict__ = data
        mySQL = MySQL(data.Mysql)