from tinydb import TinyDB, Query

class DatabaseManager:
    def __init__(self, db_filename="game_db.json"):
        self.db = TinyDB(db_filename)
        self.users_table = self.db.table("users")
        self.saves_table = self.db.table("saves")

    def register_user(self, username, password):
        User = Query()
        if self.users_table.search(User.username == username):
            return False, "Username already exists."
        self.users_table.insert({"username": username, "password": password})
        return True, "Registration successful!"

    def authenticate_user(self, username, password):
        User = Query()
        result = self.users_table.search((User.username == username) & (User.password == password))
        if result:
            return True, "Login successful!"
        return False, "Invalid username or password."

    def save_game(self, username, game_data):
        Save = Query()
        self.saves_table.upsert({"username": username, "data": game_data}, Save.username == username)

    def load_game(self, username):
        Save = Query()
        result = self.saves_table.search(Save.username == username)
        if result:
            return result[0]["data"]
        return None