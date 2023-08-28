from battleship_game import BattleshipGame


def main():

    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    ships = int(input("Enter the number of ships: "))
    game = BattleshipGame(rows, cols, ships)


print("Welcome to Battleship Game")
main()