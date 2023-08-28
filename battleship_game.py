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
        pass

    def computer_place_ships(self):
        pass

    def get_valid_coordinates(self):
        pass

    def user_attack(self):
        pass

    def computer_attack(self):
        pass

    def play(self):
        print(self.user_battlefield)
        print(self.computer_battlefield)