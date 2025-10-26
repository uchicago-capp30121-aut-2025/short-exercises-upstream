"""
Short Exercises #4
Implement simplified version of battleship board
"""

import random

SIZE = 10

SHIP_SIZES = {
    "Carrier": 5,
    "Battleship": 4,
    "Destroyer": 3,
    "Submarine": 3,
    "Patrol Boat": 2}

class Board:
    """
    Class for representing the state of the game board

    Attributes
    ----------
    board: (list of lists of strings) the current state of the board
    num_ships: (int) the number of ships that have yet to be sunk

    Methods
    -------
    deploy_fleet(fleet_locations):
        add the ships to the board
    is_game_over(): 
        are there any ships (or parts of ships) left on the board
    play_move(loc):
        update the board to reflect a shot at the specified location (loc), 
        returns Miss, Hit, or the type of ship sunk depending on the
        outcome of the shot
    """

    def __init__(self):
        """
        Construct an instance of the Board class
        """

        # REPLACE pass with appropriate code.
        pass

    
    def deploy_fleet(self, fleet_locations):
        """
        Add ships to the board.

        Args:
            locations: a dictionary that speficies a starting
              location for ships in the fleet.  The number of
              ships in a fleet can vary.
        """
        # REPLACE pass with appropriate code.
        pass


    def play_move(self, loc):
        """
        Play a move in the game
        
        Args:
            loc: (int, int) a location in the board

        Returns: (string) "Miss" if the location contained water, "Hit" if the
            location contained a piece of a ship, but not the last piece in
            the ship.  The ship type if the location contained the last piece
            of a given ship.
        """

        row, col = loc
        assert 0 <= row < SIZE
        assert 0 <= col < SIZE

        # YOUR CODE HERE
        # Replace None with an appropriate return value
        return None

    def is_game_over(self):
        """Have all the ships been sunk?"""

        # YOUR CODE HERE
        # Replace None with an appropriate return value
        return None

    def __str__(self):
        """ Generate a string representation of the board"""

        # YOUR CODE HERE
        # Replace "" with an appropriate return value
        return ""        
        
    
class Game:
    """
    Represent the game

    Attributes
    ----------
    board: (Board) the game board

    Methods
    -------
    play(): play the game
    """

    def __init__(self, ships):
        self.board = Board()
        self.board.deploy_fleet(ships)
        
    def __convert_input(self, keyboard):
        """
        Convert the input into a (int, int) tuple
        if possible.  Check in range(0, SIZE).

        Args:
            keyboard: (string) the user's input

        Returns: (int, int) or None
        """

        split = keyboard.split()
        if len(split) != 2:
            return None
        try:
            r = int(split[0])
            c = int(split[1])
        except (ValueError, IndexError):
            return None

        if 0 <= r < SIZE and 0 <= c < SIZE:
            return r, c
        return None

    def __get_input(self):
        """
        Keep asking for input until user enters: show, concede,
        cheat, or move as a pair of integers.

        Returns (action, location or None)
        """
        while True:
            keyboard = input("Enter your move: ")
            if keyboard.lower() in ("concede", "cheat"):
                return (keyboard.lower(), None)
            result = self.__convert_input(keyboard)
            if result:
                return ("move", result)
            print("Please enter a valid board location or command...")

    def play(self):
        """
        Play the game.
        """

        print("Ready to play?")

        num_shots = 0
        while not self.board.is_game_over():
            (action, loc) = self.__get_input()
            if action == "move":
                print(self.board.play_move(loc))
                num_shots = num_shots + 1
            elif action == "concede":
                print(f"You conceded after {num_shots} shots")
                return
            elif action == "cheat":
                print(self.board)
            else:
                assert False, "should never get here"

        print(f"You took {num_shots} shots to win")


def generate_random_game():
    """
    Generate a game randomly:
       Choose how many and which ships to include (zero to five)
       Choose where to place them on the board.

    Returns: (Game) a randomly generated game
    """

    # Choose how many and which ships to include
    num_ships = random.randint(1, len(SHIP_SIZES))
    ships = list(SHIP_SIZES.keys())
    random.shuffle(ships)
    ships = ships[:num_ships]

    # Choose which rows will hold ships
    row_nums = list(range(SIZE))
    random.shuffle(row_nums)
    rows_to_use = row_nums[:num_ships]

    config = {}
    for i, r in enumerate(rows_to_use):
        ship = ships[i]
        c = random.randint(0, SIZE-SHIP_SIZES[ship])
        config[ship] = (r, c)
        
    return Game(config)

if __name__ == "__main__":
    g = generate_random_game()
    g.play()

