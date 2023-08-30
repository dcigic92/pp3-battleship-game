import constants as c
import random


class BattlefieldGenerator:
    """
    Class to generate the battlefield, place ships, get random coordinates for the computer and print battlefield.
    This class is static, so it doesn't need to be instantiated.
    """
    @staticmethod
    def generate_battlefield(rows, cols):
        # Method to print list of lists
        return [[c.EMPTY_FIELD_SYMBOL for _ in range(cols)] for _ in range(rows)]
    
    @staticmethod
    def place_ship(battlefield, row, col):
        # Method to change the value inside the list
        battlefield[row][col] = c.SHIP_SYMBOL

    @staticmethod
    def random_coordinates(rows, cols):
        # Method to return random coordinates
        return random.randint(0, rows - 1), random.randint(0, cols - 1)
    
    @staticmethod
    def print_battlefield(battlefield, if_computer):
        # Method to print the battlefield with colors
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        i = 1
        print(" ", end=" ")
        for letter in range(len(battlefield[0])):
            print(letters[letter], end=" ") # Changing end parameter's value so it will end with space instead of the new line.
        print()
        for row in battlefield:
            print(i, end=" ")
            for cell in row:
                # Hides computer's ships
                if cell == c.SHIP_SYMBOL and if_computer == c.YES:
                    print(c.GRAY + c.EMPTY_FIELD_SYMBOL + c.RESET, end=" ")
                elif cell == c.SHIP_SYMBOL:
                    print(c.CYAN + cell + c.RESET, end=" ")
                elif cell == c.SHIP_HIT_SYMBOL:
                    print(c.RED + cell + c.RESET, end=" ")
                elif cell == c.SHIP_MISS_SYMBOL:
                    print(c.YELLOW + cell + c.RESET, end=" ")
                else:
                    print(c.GRAY + cell + c.RESET, end=" ")
            i += 1           
            print()