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
            row, col = self.get_valid_coordinates()
            BattlefieldGenerator.place_ship(self.user_battlefield, row, col)

    def computer_place_ships(self):
        pass

    def get_valid_coordinates(self):
        while True:
            try:
                row = int(input(f"Enter row (0 to {self.rows - 1}): "))
                col = int(input(f"Enter column (0 to {self.cols - 1}): "))
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    return row, col
                else:
                    raise ValueError("you entered invalid coordinates")
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid coordinates.")

    def user_attack(self):
        pass

    def computer_attack(self):
        pass

    def play(self):
        self.user_place_ships()
        print(self.user_battlefield)