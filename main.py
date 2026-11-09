from database import DatabaseManager
from auth import AuthSystem
from player import Player
from game import GameEngine

def main():
    db_manager = DatabaseManager()
    auth_system = AuthSystem(db_manager)

    username = auth_system.run()
    if not username:
        return

    # Load save data or initialize new player
    saved_data = db_manager.load_game(username)
    player = Player(username)

    game_engine = GameEngine(player, db_manager, username)
    if saved_data:
        game_engine.load_saved_state(saved_data)

    game_engine.play()

if __name__ == "__main__":
    main()