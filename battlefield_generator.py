

class BattlefieldGenerator:
    @staticmethod
    def generate_battlefield(rows, cols):
        return [["-" for _ in range(cols)] for _ in range(rows)]