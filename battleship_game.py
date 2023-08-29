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
            while True:
                try:
                    row, col = self.get_valid_coordinates()
                    if self.user_battlefield[row][col] == "-":
                        BattlefieldGenerator.place_ship(self.user_battlefield, row, col)
                        break
                    else:
                        raise ValueError("you already placed ship there")
                except ValueError as e:
                    print(f"\nInvalid input: {e}. Please enter a valid coordinates.")

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
                row = int(input(f"Enter row (1 to {self.rows}): "))
                col = (input(f"Enter column (A to {dict_key_num[self.cols-1]}): ")).upper()
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
                print(f"Invalid input: {e}. Please enter a valid coordinates.")

    def user_attack(self):
        print("\nYour Turn to Attack!")
        row, col = self.get_valid_coordinates()
        if self.computer_battlefield[row][col] == "S":
            print("\nYou hit a computer's ship!")
            self.computer_battlefield[row][col] = "+"
            self.computer_ships -= 1
        elif self.computer_battlefield[row][col] == "+" or self.computer_battlefield[row][col] == "x":
            print("\nYou already attacked on that coordinates! Please choose again.")
            self.user_attack()
        else:
            print("\nYou missed!")
            self.computer_battlefield[row][col] = "x"

    def computer_attack(self):
        print("\nComputer's Turn to Attack!")
        row, col = BattlefieldGenerator.random_coordinates(self.rows, self.cols)
        if self.user_battlefield[row][col] == "S":
            print("\nComputer hit your ship!")
            self.user_battlefield[row][col] = "+"
            self.user_ships -= 1
        elif self.user_battlefield[row][col] == "+" or self.user_battlefield[row][col] == "x":
            self.computer_attack()
        else:
            print("\nComputer missed!")
            self.user_battlefield[row][col] = "x"

    def play(self):
        self.user_place_ships()
        self.computer_place_ships()

        while self.user_ships > 0 and self.computer_ships > 0:
            print("\nYour Battlefield:\n")
            BattlefieldGenerator.print_battlefield(self.user_battlefield)

            print(f"\nComputer's ships remaining: {self.computer_ships}")
            print(f"\nYour ships remaining: {self.user_ships}")

            print("\nComputer's Battlefield:\n")
            BattlefieldGenerator.print_battlefield(self.computer_battlefield)

            self.user_attack()
            if self.computer_ships == 0:
                print("\nCongratulations! You sunk all the computer's ships! You won!")
                break

            self.computer_attack()
            if self.user_ships == 0:
                print("\nOh no! All your ships are sunk! You lost!")
                break