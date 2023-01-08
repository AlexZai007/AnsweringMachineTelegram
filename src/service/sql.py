import sqlite3


class DataBase():

    #specific initialization (for ease of scaling)
    def __init__(self, db_file):
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()

    #Adding a user to the database
    async def UserAdd(self, user_id: int):
        with self.connect:
            return self.cursor.execute(f"""INSERT INTO id (ID) VALUES (?)""", [user_id])

    #Search for a user by id in the database
    async def UserFind(self, user_id: int):
        with self.connect:
            return self.cursor.execute("""SELECT ID FROM id WHERE id = (?)""", [user_id]).fetchall()