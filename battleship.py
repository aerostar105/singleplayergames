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
        self.remaining_guess_list = []
        self.remaining_ship_list = []
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
                #create list of all coords for guesses
                self.remaining_guess_list.append([i,j])
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
        coord_list=[]
        coord_list.append(self.translate_from_dict.get(rows)-1)
        coord_list.append(columns-1)
        return coord_list
            


class Ship:
    movement_dict={'N':[-1, 0], 'S': [1, 0], 'E': [0, 1], 'W':[0, -1]}

    def __init__(self, ship_name, ship_size, Grid, icon):
        self.ship_name = ship_name
        self.ship_size = ship_size
        self.hp = ship_size
        self.is_placed = False
        self.abbreviation = icon

    def __repr__(self):
        return str(self.ship_name)
        
    def is_valid_placement(self, player, coords,  direction):
        # if invalid location, i.e. if any positions along the length of the ship are not
        # locations in the grid or not empty, return False
        # print("Starting is_valid_placement coords")
        # print(coords)
        coordy=coords.copy()
        # print(coordy)
        direction_vector = self.movement_dict[direction]
        # print(direction_vector)
        for i in range(self.ship_size):
            if coordy[0] < 0 or coordy[1] < 0 or coordy[0] > len(player.griddy)-1 or coordy[1] > len(player.griddy[0])-1:
                # note, len(player.griddy[0]) column length check assumes all columns of the list are the same length
                # as the first column to avoid an index out of range error
                return False
            if player.griddy[coordy[0]][coordy[1]] != ['  ']:
                return False
            coordy[0] += direction_vector[0]
            coordy[1] += direction_vector[1]
        #     print(coordy)
        #     print(direction_vector)
        # print("Ending is_valid_placement coords")
        # print(coords)
        # print(coordy)
        return True
     

    def place_ship(self, player, coord_list, direction):
        # place ship in grid
        # print("place_ships coordinates")
        # print(coord_list)
        # print(direction)

        if direction == "N":
            for length in range(self.ship_size):
                copy_list=coord_list.copy()
                player.griddy[copy_list[0]][copy_list[1]] = [self.abbreviation]
                player.remaining_ship_list.append(copy_list)
                coord_list[0] -= 1
        elif direction == "S":
            for length in range(self.ship_size):
                copy_list=coord_list.copy()
                player.griddy[copy_list[0]][copy_list[1]] = [self.abbreviation]
                player.remaining_ship_list.append(copy_list)
                coord_list[0] += 1
        elif direction == "E":
            for length in range(self.ship_size):
                copy_list=coord_list.copy()
                player.griddy[copy_list[0]][copy_list[1]] = [self.abbreviation]
                player.remaining_ship_list.append(copy_list)
                coord_list[1] += 1
        elif direction == "W":
            for length in range(self.ship_size):
                copy_list=coord_list.copy()
                player.griddy[copy_list[0]][copy_list[1]] = [self.abbreviation]
                player.remaining_ship_list.append(copy_list)
                coord_list[1] -= 1
        self.is_placed = True


def guess(enemy_board, personal_guess_board, coords):
    # checks a grid location for a ship, marks hit or miss in that location on guess board and board
    # print("guess initializing")
    coord_list = coords.copy()
    # print(coords)
    # print(" ^coords passed to function")
    # print(coord_list)
    # print("^ copy of coords passed to function")
    # print(coord_list in personal_guess_board.remaining_guess_list)
    # print("^coord_list in personal_guess_board.remaining_guess_list ")
    if (not(coord_list[0] < 0 or coord_list[1] < 0 or coord_list[0] > len(enemy_board.griddy)-1 or coord_list[1] > len(enemy_board.griddy[0])-1) and coord_list in personal_guess_board.remaining_guess_list):
        # note, len(player.griddy[0]) column length check assumes all columns of the list are the same length
        # as the first column to avoid an index out of range error
        if enemy_board.griddy[coord_list[0]][coord_list[1]] != ['  ']:
            print("{ship} was hit!".format(ship = enemy_board.griddy[coord_list[0]][coord_list[1]]))
            enemy_board.griddy[coord_list[0]][coord_list[1]] = ['><']
            enemy_board.remaining_ship_list.remove(coord_list)
            personal_guess_board.griddy[coord_list[0]][coord_list[1]] = ['><']
            personal_guess_board.remaining_guess_list.remove(coord_list)
        else:
            print("Miss")
            personal_guess_board.griddy[coord_list[0]][coord_list[1]] = ['()']
            enemy_board.griddy[coord_list[0]][coord_list[1]] = ['()']
            personal_guess_board.remaining_guess_list.remove(coord_list)


def rand_place_ships(board, ship_list):
    direction_list = ['N', 'S', 'E', 'W']
    while len(ship_list) > 0:
        x_rand = rand.randint(0,9)
        # print(x_rand)
        y_rand = rand.randint(0,9)
        # print(y_rand)
        dir_rand = rand.choice(direction_list)
        # print(dir_rand)
        coord = [x_rand, y_rand]
        # print(coord)
        if ship_list[0].is_valid_placement(board, coord, dir_rand):
            ship_list[0].place_ship(board, coord, dir_rand)
            ship_list.pop(0)
        # print(ship_list)
        # board.print_grid()

# new_grid = Grid(4, 5)
# print(new_grid.griddy)
# print("/n/n/n")
# new_grid.print_grid()

# player1.griddy[2][1] = "['DD']"
# player1.griddy[3][1] = "['DD']"
# carrier.place_ship(player2, player2.coord_conv('B',3), "E")
# print(battleship.is_valid_placement(player2, player2.coord_conv('B', 9), "N"))
# print(battleship.is_valid_placement(player2, player2.coord_conv('B', 9), "S"))
# print(battleship.is_valid_placement(player2, player2.coord_conv('B', 9), "E"))
# print(battleship.is_valid_placement(player2, player2.coord_conv('B', 9), "W"))
# battleship.place_ship(player2, player2.coord_conv("E", 4), "S")

# player1.print_grid()
# print("")
# player2.print_grid()

# main gameplay loop
standard_board_size = [10, 10]

player1 = Grid(standard_board_size[0], standard_board_size[1])
player2 = Grid(standard_board_size[0], standard_board_size[1])
player1_guesses = Grid(standard_board_size[0], standard_board_size[1])
player2_guesses = Grid(standard_board_size[0], standard_board_size[1])

carrier = Ship("Carrier", 5, player1, "CV")
battleship = Ship("Battleship", 4, player1, "BB")
cruiser = Ship("Cruiser", 3, player1, "CR")
submarine = Ship("Submarine", 3, player1, "SF")
destroyer = Ship("Destroyer", 2, player1, "DD")

ship_list_player1 = [carrier, battleship, cruiser, submarine, destroyer]

carrier = Ship("Carrier", 5, player2, "CV")
battleship = Ship("Battleship", 4, player2, "BB")
cruiser = Ship("Cruiser", 3, player2, "CR")
submarine = Ship("Submarine", 3, player2, "SF")
destroyer = Ship("Destroyer", 2, player2, "DD")

ship_list_player2 = [carrier, battleship, cruiser, submarine, destroyer]


# print(ship_list_player1)
rand_place_ships(player1, ship_list_player1)
rand_place_ships(player2, ship_list_player2)

print("Welcome to an electronic Battleship clone")
print("this is a non-commercial copy created as a python educational product")
# print("Place your ships:  1: Randomly, 2: Manually")
# while ships left to print > 0: do the following
# player1.print_grid()
# #print list of ships to place
# print("Please place your ships by entering the ship number, its starting location, and direction")
# print("in the form: 1, B, 7, S")
# # input_string = input()
# # check validity of ship placement, then place the ship
# # if not valid, print error message to user
# # create CPU ship placement

# at this point, both Grids have all ships placed
while (len(player1.remaining_ship_list) > 0) and (len(player2.remaining_ship_list) > 0):
    # player2.print_grid()
    # print("------")
    player1_guesses.print_grid()
    print("\n")
    player1.print_grid()
    print("Input the capital letter of your guess row: (or X for eXit)")
    guess_row = input()
    if guess_row == 'X':
        break
    print("Input the number of your guess column:")
    guess_column = int(input())
    guess(player2, player1_guesses, player1.coord_conv(guess_row, guess_column))
    # perform cpu player guess
    player2_guess_coord = rand.choice(player2_guesses.remaining_guess_list)
    guess(player1, player2_guesses, player2_guess_coord)

if len(player1.remaining_ship_list) == 0:
    print("player2 wins")
elif len(player2.remaining_ship_list) == 0:
    print("player1 wins")     
else:
    print("Error:no winner found")
print("Thanks for playing!")

# print("Here ")


# left to do:
#     
# done --add A-J, 1-10 elements to display in print_grid.
# done --create list of ships in main method
# done --create ship placement logic function to grid class
# done -- logic test for ship.is_valid_placement()
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

# several times I thought is_valid_placement() worked, once I got the rand_
# place_ships() function in place I have discovered several out of index errors
# and ship overwrites/incorrect placements. Using print() statements to track 
# location indexes throughout the two methods revealed that the location index 
# was modified during checks along the length of the proposed ship as specified
# but what was unknown was that this was performed on the location variable and
# not a copy of one. Tested individually, both functions worked fine but when
# combined, tried to place a ship one space away from the end of the checked 
# location instead of the start.  Changing is_valid_placement to work with a 
# copy of the location coordinates using b = a.copy() resolved the logic 
# errors.

# game is initialized with a 10x10 board size but built with customizable size
# logically sound up to 26x26 as-is but not visually practical printed to the
# standard terminal past 22x12

# looks like coord_conv() is a Facade pattern


