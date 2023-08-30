import constants as c
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
            print(c.BOLD + f"\nPlace your ship ({self.user_ships - _} left)" + c.RESET)
            while True:
                try:
                    row, col = self.get_valid_coordinates()
                    if self.user_battlefield[row][col] == "-":
                        BattlefieldGenerator.place_ship(self.user_battlefield, row, col)
                        break
                    else:
                        raise ValueError("you already placed ship there")
                except ValueError as e:
                    print(c.RED + f"\nInvalid input: {e}. Please enter a valid coordinates.\n" + c.RESET)

    def computer_place_ships(self):
        computer_ships_placed = 0

        while computer_ships_placed < self.computer_ships:
            row, col = BattlefieldGenerator.random_coordinates(self.rows, self.cols)
            if self.computer_battlefield[row][col] == "-":
                BattlefieldGenerator.place_ship(self.computer_battlefield, row, col)
                computer_ships_placed += 1

    def get_valid_coordinates(self):
        dict_key_num = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H"}
        dict_key_letters = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
        while True:
            try:
                row = int(input(c.GRAY + f"\nEnter row (1 to {self.rows}): \n" + c.RESET))
                col = (input(c.GRAY + f"Enter column (A to {dict_key_num[self.cols-1]}): \n" + c.RESET)).upper()
                row -= 1
                if col in dict_key_letters:
                    col = dict_key_letters[col]
                    if 0 <= row < self.rows and 0 <= col < self.cols:
                        return row, col
                    else:
                        raise ValueError("you entered invalid coordinates")
                else:
                    raise ValueError("you entered invalid coordinates")
            except ValueError as e:
                print(c.RED + f"\nInvalid input: {e}. Please enter a valid coordinates.\n" + c.RESET)

    def user_attack(self):
        print(c.BOLD + "\nYour Turn to Attack!" + c.RESET)
        row, col = self.get_valid_coordinates()
        if self.computer_battlefield[row][col] == "S":
            print(c.GREEN + "\nYou hit a computer's ship!" + c.RESET)
            self.computer_battlefield[row][col] = "+"
            self.computer_ships -= 1
        elif self.computer_battlefield[row][col] == "+" or self.computer_battlefield[row][col] == "x":
            print(c.RED + "\nYou already attacked on that coordinates! Please choose again.\n" + c.RESET)
            self.user_attack()
        else:
            print(c.YELLOW + "\nYou missed!" + c.RESET)
            self.computer_battlefield[row][col] = "x"

    def computer_attack(self):
        print(c.BOLD + "\nComputer's Turn to Attack!" + c.RESET)
        while True:
            row, col = BattlefieldGenerator.random_coordinates(self.rows, self.cols)
            if self.user_battlefield[row][col] == "S":
                print(c.RED + "\nComputer hit your ship!" + c.RESET)
                self.user_battlefield[row][col] = "+"
                self.user_ships -= 1
                break
            elif self.user_battlefield[row][col] == "-":
                print(c.YELLOW + "\nComputer missed!" + c.RESET)
                self.user_battlefield[row][col] = "x"
                break

    def play(self):
        self.user_place_ships()
        self.computer_place_ships()

        while self.user_ships > 0 and self.computer_ships > 0:
            print(c.BOLD + "\nYour Battlefield:\n" + c.RESET)
            BattlefieldGenerator.print_battlefield(self.user_battlefield, "n")

            print(c.CYAN + f"\nYour ships remaining: {self.user_ships}")
            print(f"\nComputer's ships remaining: {self.computer_ships}" + c.RESET)

            print(c.BOLD + "\nComputer's Battlefield:\n" + c.RESET)
            BattlefieldGenerator.print_battlefield(self.computer_battlefield, "y")

            self.user_attack()
            if self.computer_ships == 0:
                print(c.GREEN + "\nCongratulations! You sunk all the computer's ships! You won!" + c.RESET)
                print(c.BOLD + "\nComputer's Battlefield:\n" + c.RESET)
                BattlefieldGenerator.print_battlefield(self.computer_battlefield, "y")
                break

            self.computer_attack()
            if self.user_ships == 0:
                print(c.RED + "\nOh no! All your ships are sunk! You lost!" + c.RESET)
                print(c.BOLD + "\nYour Battlefield:\n" + c.RESET)
                BattlefieldGenerator.print_battlefield(self.user_battlefield, "n")
                break