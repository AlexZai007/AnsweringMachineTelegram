from dataclasses import dataclass


@dataclass
class Config():

    '''
    api_id - your api id you can find it on the site - https://my.telegram.org/auth?to=apps
    api_hash - your api id you can find it on the site - https://my.telegram.org/auth?to=app
    db_name - the path to the database in which to enter all the id who wrote the account. This is necessary so as not to spam a person
    session_location - path to the telegram session from the account

    EXAMPLE

    api_id: int =  71023987
    api_hash: str = "sdfjhsdlfkjh:sdoufhhk" 
    db_name: str = 'src/users.db' 
    session_location: str = 'src/session/anon.session' 

    '''


    api_id: int =  
    api_hash: str = "" 
    db_name: str = 'src/users.db' 
    session_location: str = 'src/session/anon.session' 




