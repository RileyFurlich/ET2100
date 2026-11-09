from colorama import Fore

class MapManager:
    def __init__(self):
        # Map 1: Town & Wilds (Non-square layout with walls '#')
        self.map_town = [
            "##########",
            "#P..N....#",
            "#...##...#",
            "#..S...M.#",
            "#####....#",
            "    #..M.#",
            "    ######"
        ]

        # Map 2: Dark Dungeon (Non-square layout with walls '#')
        self.map_dungeon = [
            "  ####### ",
            " ##.....##",
            "#...M...N#",
            "#..####..#",
            "#...B....#",
            "##########"
        ]

    def get_layout(self, map_name):
        if map_name == "Town Square":
            return self.map_town
        else:
            return self.map_dungeon

    def draw_map(self, map_name, player_x, player_y):
        layout = self.get_layout(map_name)
        print(Fore.CYAN + f"\n--- Map: {map_name} ---")
        for r_idx, row in enumerate(layout):
            line = ""
            for c_idx, char in enumerate(row):
                if r_idx == player_y and c_idx == player_x:
                    line += Fore.GREEN + "P "
                elif char == "#":
                    line += Fore.WHITE + "# "
                elif char == "N":
                    line += Fore.MAGENTA + "N "
                elif char == "S":
                    line += Fore.YELLOW + "S "
                elif char == "M":
                    line += Fore.RED + "M "
                elif char == "B":
                    line += Fore.RED + "B "
                else:
                    line += Fore.GRAY + ". " if hasattr(Fore, 'GRAY') else ". "
            print(line)
        print(Fore.YELLOW + "Legend: P=Player, #=Wall, N=NPC, S=Shop, M=Monster Spawn, B=Boss")

    def is_valid_move(self, map_name, x, y):
        layout = self.get_layout(map_name)
        if y < 0 or y >= len(layout):
            return False
        if x < 0 or x >= len(layout[y]):
            return False
        return layout[y][x] != "#" and layout[y][x] != " "