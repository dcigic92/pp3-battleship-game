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
    
    @staticmethod
    def print_battlefield(battlefield):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        space = " "
        i = 1
        print(space, end=" ")
        for letter in range(len(battlefield[0])):
            print(letters[letter], end=" ")
        print()
        for row in battlefield:
            print(i, end=" ")
            for cell in row:
                print(cell, end=" ")     
            i += 1           
            print()