from battlefield_generator import BattlefieldGenerator


class BattleshipGame:
    def __init__(self, rows, cols, num_ships):
        self.rows = rows
        self.cols = cols
        self.user_ships = num_ships
        self.computer_ships = num_ships

        self.user_battlefield = BattlefieldGenerator.generate_battlefield(rows, cols)
        self.computer_battlefield = BattlefieldGenerator.generate_battlefield(rows, cols)

    def user_place_ships(self):
        for _ in range(self.user_ships):
            print(f"\nPlace your ship ({self.user_ships - _} left)")
            row, col = 1, 4
            BattlefieldGenerator.place_ship(self.user_battlefield, row, col)

    def computer_place_ships(self):
        pass

    def get_valid_coordinates(self):
        pass

    def user_attack(self):
        pass

    def computer_attack(self):
        pass

    def play(self):
        self.user_place_ships()
        print(self.user_battlefield)