import constants as c
from battleship_game import BattleshipGame


def take_user_input(input_type, min_value, max_value):
    """
    Runs a while loop to collect a valid integer from the user via the
    terminal, which must be one number.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        try:
            user_input = int(input(
                c.GRAY + c.BOLD +
                f"Enter the number of {input_type} (between {min_value}"
                f" and {max_value}): \n"
                + c.RESET))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                raise ValueError(
                    f"number of {input_type} must be between {min_value}"
                    f" and {max_value}, you entered number {user_input}")
        except ValueError as e:
            print(c.RED + f"\nInvalid input: {e}. Please enter a"
                        + f" valid number.\n"
                        + c.RESET)


def play_again():
    """
    Runs a while loop to collect a valid string from the user via the
    terminal, which must be one character y or n.
    The loop will repeatedly request data, until it is valid. If answer is y
    it will clear terminal and call main function which will start game again.
    """
    while True:
        try:
            user_input = (input(
                c.GRAY + c.BOLD +
                "Do you want to play again? (y or n): \n"
                + c.RESET)).lower()
            if user_input == c.YES:
                print(c.CLEAR)
                main()
            elif user_input == c.NO:
                print(c.BOLD + "\nThank you for playing. Goodbye." + c.RESET)
                break
            else:
                raise ValueError(
                    f"you must enter y or n, you entered {user_input}")
        except ValueError as e:
            print(c.RED + f"\nInvalid input: {e}. Please try again.\n"
                        + c.RESET)


def main():
    """
    Main function which prints title, gets user inputs and starts the game.
    This function also calls play again function after game is finished.
    """
    print(c.CYAN + c.TITLE + c.RESET)

    rows = take_user_input("rows", 5, 8)
    cols = take_user_input("columns", 5, 8)
    num_ships = take_user_input("ships", 4, 6)

    game = BattleshipGame(rows, cols, num_ships)
    game.play()
    play_again()


main()
