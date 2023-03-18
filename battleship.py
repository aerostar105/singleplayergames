import random as rand


class Grid:

    translate_to_dict = {
        1: "A ",
        2: "B ",
        3: "C ",
        4: "D ",
        5: "E ",
        6: "F ",
        7: "G ",
        8: "H ",
        9: "I ",
        10: "J ",
        11: "K ",
        12: "L ",
        13: "M ",
        14: "N ",
        15: "O ",
        16: "P ",
        17: "Q ",
        18: "R ",
        19: "S ",
        20: "T ",
        21: "U ",
        22: "V ",
        23: "W ",
        24: "X ",
        25: "Y ",
        26: "Z ",
    }
    translate_from_dict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }

    def __init__(self, rows, columns):
        self.griddy = []
        self.rows = rows
        self.columns = columns
        self.row_legend = []
        self.column_legend = []
        # create legends
        for i in range(1, rows + 1):
            self.row_legend.append([Grid.translate_to_dict.get(i)])

        for j in range(1, columns + 1):
            if j < 10:
                self.column_legend.append(["" + str(j) + " "])
            else:
                self.column_legend.append(["" + str(j) + ""])

        # create board matrix
        for i in range(rows):
            temp_list = []
            for j in range(columns):
                temp_list.append(["  "])
            self.griddy.append(temp_list)

    # def __repr__(self):
    #     return self.griddy

    def print_grid(self):
        column_string = "['  ']"
        for i in range(len(self.column_legend)):
            column_string += str(self.column_legend[i])
        print(column_string)
        for i in range(self.rows):
            temp_string = ""
            secondary_counter = 0  # to display the row_header
            for j in range(self.columns):
                if secondary_counter == 0:
                    temp_string += str(self.row_legend[i])

                temp_string += str(self.griddy[i][j])
                secondary_counter += 1
            print(temp_string)

        def coord_conv(self, rows, columns):
            # takes alphanumeric grid coordinates true to Battleship Game Style
            # and converts to common zero-indexed list of row and column
            # indicies
            pass


class Ship:
    def __init__(self, ship_name, ship_size, Grid, icon):
        self.ship_name = ship_name
        self.ship_size = ship_size
        self.hp = ship_size
        self.is_placed = False
        self.abbreviation = icon

    def is_valid_placement(self, player, row, column, direction):
        # DOES NOT WORK CURRENTLY, ALSO NEEDS TO CHECK FOR NOT OVERWRITING
        # ANOTHER SHIP
        # if invalid location, i.e. if ending point or starting point are not
        # locations in the grid, or direction not N, E, S or W, return False
        if direction == "N":
            if (player.griddy[row - self.ship_size][column]) or (
                player.griddy[row][column]
            ) not in player.griddy:
                return False
        elif direction == "S":
            if (player.griddy[row + self.ship_size][column]) or (
                player.griddy[row][column]
            ) not in player.griddy:
                return False
        elif direction == "E":
            if (player.griddy[row][column + self.ship_size]) or (
                player.griddy[row][column]
            ) not in player.griddy:
                return False
        elif direction == "W":
            if (player.griddy[row][column - self.ship_size]) or (
                player.griddy[row][column]
            ) not in player.griddy:
                return False
        else:
            return False

    def place_ship(self, player, row, column, direction):
        # place ship in grid
        if direction == "N":
            for length in range(self.ship_size):
                player.griddy[row][column] = [self.abbreviation]
                row -= 1
        elif direction == "S":
            for length in range(self.ship_size):
                player.griddy[row][column] = [self.abbreviation]
                row += 1
        elif direction == "E":
            for length in range(self.ship_size):
                player.griddy[row][column] = [self.abbreviation]
                column += 1
        elif direction == "W":
            for length in range(self.ship_size):
                player.griddy[row][column] = [self.abbreviation]
                column -= 1
        self.is_placed = True


def guess(Grid, row, column):
    # checks a grid location for a ship, marks hit or miss in that location
    # could return type of ship hit
    #
    pass


# new_grid = Grid(4, 5)
# print(new_grid.griddy)
# print("/n/n/n")
# new_grid.print_grid()

# main gameplay loop
standard_board_size = [10, 10]

player1 = Grid(standard_board_size[0], standard_board_size[1])
player2 = Grid(standard_board_size[0], standard_board_size[1])

carrier = Ship("Carrier", 5, player1, "CV")
battleship = Ship("Battleship", 4, player1, "BB")
cruiser = Ship("Cruiser", 3, player1, "CR")
submarine = Ship("Submarine", 3, player1, "SF")
destroyer = Ship("Destroyer", 2, player1, "DD")

player1.griddy[2][1] = "['DD']"
player1.griddy[3][1] = "['DD']"
print(battleship.is_valid_placement(player2, 4, 5, "S"))
battleship.place_ship(player2, 4, 5, "S")
carrier.place_ship(player2, 2, 2, "E")
player1.print_grid()
print("")
player2.print_grid()


# left to do:    done --add A-J, 1-10 elements to display in print_grid.
# done --create list of ships in main method
# done --create ship placement logic function to grid class
# fix logic test for ship.is_valid_placement()
# create AI logic behavior for guessing
# initialize boards for player and AI
# create main gameplay loop
# use [()] to register a miss in our two character display format

# future options:
# create salvo alternate playstyle feature that is 'canon' (hah) in Battleship
# Rules
# create logic to narrow down AI player guesses based on available grid space
# aggregate various AI strategies into single game diffuculty settings
# to hide the ships left on the board


# ship abbreviations are from https://www.history.navy.mil
# /research/histories/ship-histories/abbreviations.html

# started with a weird formatting of a string inside a list but then realized
# it met the core functionality of displaying a grid pattern while still
# having room for 2 character string representing icons for empty space, ships,
# hits, and misses.

# got a cyclomatic complexity warning for function Ship.place_ship. Originally
# this function both checked for a valid placement and then placed the ship, to
# reduce the complexity a new function Ship.is_valid_placement() was created to
# split the complexity and remove the warning.

# game is initialized with a 10x10 board size but built with customizable size
# logically sound up to 26x26 as-is but not visually practical printed to the
# standard terminal past 22x12

# looks like coord_conv() is a Facade pattern
