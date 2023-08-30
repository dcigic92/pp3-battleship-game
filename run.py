import constants as c
from battleship_game import BattleshipGame


def take_user_input(input_type, min_value, max_value):
    while True:
        try:
            user_input = int(input(c.GRAY + f"Enter the number of {input_type} (between {min_value} and {max_value}): \n" 
                                   + c.RESET))
            if min_value <= user_input <= max_value:
                return user_input
            else:
              raise ValueError(
                  f"number of {input_type} must be between {min_value} and {max_value}, you entered number {user_input}"
                  )
        except ValueError as e:
            print(c.RED + f"\nInvalid input: {e}. Please enter a valid number.\n" + c.RESET)

def main():
    rows = take_user_input("rows", 5, 8)
    cols = take_user_input("columns", 5, 8)
    num_ships = take_user_input("ships", 4, 6)

    game = BattleshipGame(rows, cols, num_ships)
    game.play()


print(c.BOLD + "\n" + c.TITLE + "\n" + c.RESET)
main()