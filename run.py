from battleship_game import BattleshipGame


def main():
    while True:
        try:
            rows = int(input("Enter the number of rows (between 5 and 8): "))
            if 5 <= rows <= 8:
                break
            else:
                raise ValueError(f"Number of rows must be between 5 and 8, you entered number {rows}")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

    while True:
        try:
            cols = int(input("Enter the number of columns (between 5 and 8): "))
            if 5 <= cols <= 8:
                break
            else:
                raise ValueError(f"Number of columns must be between 5 and 8, you entered number {cols}")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

    while True:
        try:
            num_ships = int(input("Enter the number of ships (4 or 5): "))
            if num_ships in [4, 5]:
                break
            else:
                raise ValueError(f"Number of ships must be either 4 or 5, you entered number {num_ships}")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

    game = BattleshipGame(rows, cols, num_ships)
    game.play()


print("Welcome to the Battleship Game")
main()