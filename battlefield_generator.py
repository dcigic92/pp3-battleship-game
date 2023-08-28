import random


class BattlefieldGenerator:
    @staticmethod
    def generate_battlefield(rows, cols):
        return [["-" for _ in range(cols)] for _ in range(rows)]
    
    @staticmethod
    def place_ship(battlefield, row, col):
        battlefield[row][col] = "S"

    @staticmethod
    def random_coordinates(rows, cols):
        return random.randint(0, rows - 1), random.randint(0, cols - 1)