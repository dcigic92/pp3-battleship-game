
class BattleshipGame:
    def __init__(self, rows, cols, ships):
        self.rows = rows
        self.cols = cols
        self.user_ships = ships
        self.computer_ships = ships