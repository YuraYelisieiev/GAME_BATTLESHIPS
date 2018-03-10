from string import ascii_uppercase
from random import randint


def read_data(file_name):
    with open(file_name, 'r') as file:
        re_lst = [list(line.strip('\n')) for line in file.readlines()]
    return re_lst


def has_ship(lst, coord, empty_peace):
    # abc = ascii_uppercase
    # I made this exception for my own further use
    if type(coord[0]) == str:
        x = ascii_uppercase.index(coord[0])
    else:
        x = coord[0] - 1
    if lst[coord[1] - 1][x] != empty_peace:
        return True
    else:
        return False


def ship_size(lst, coord, empty_peace):
    """
    Count the size of a ship by coordinates of 1 peace, and check if by given
    coordinates exist ship
    :param lst: Your field for the game
    :param coord: coordinates of a ship
    :return: size of a ship
    """
    if has_ship(lst, coord, empty_peace):
        # I made this exception for my own further use
        if type(coord[0]) == str:
            first_index = ascii_uppercase.index(coord[0])
        else:
            first_index = coord[0] - 1
        second_index = coord[1] - 1
        x, y, count, space, ret_count = first_index, second_index, 1, empty_peace, (
            1, 1)
        if 0 <= x + 1 <= 9 and lst[y][x + 1] == '*':
            while 0 <= x + 1 <= 9 and lst[y][x + 1] != space:
                x += 1
                count += 1
        x, y = first_index, second_index
        if 0 <= x - 1 <= 9 and lst[y][x - 1] == '*':
            while 0 <= x - 1 <= 9 and lst[y][x - 1] != space:
                x -= 1
                count += 1
        x, y = first_index, second_index
        if count > 1:
            ret_count = (count, 1)
            count = 1
        if 0 <= y - 1 <= 9 and lst[y - 1][x] == '*':
            while 0 <= y - 1 <= 9 and lst[y - 1][x] != space:
                y -= 1
                count += 1
        x, y = first_index, second_index
        if 0 <= y + 1 <= 9 and lst[y + 1][x] == '*':
            while 0 <= y + 1 <= 9 and lst[y + 1][x] != space:
                y += 1
                count += 1
        if count > 1:
            ret_count = (1, count)
        return ret_count
    else:
        return (0, 0)


def is_valid(lst):
    """
    Validate your field
    :param lst: Your filed
    :return: boolean Or this field if good for use
    """
    ships = [ship_size(lst, (i, j)) for i in range(1, 11) for j in
             range(1, 11)]
    return len(list(filter(lambda x: x[0] > 0, ships))) == 20 and sum(
        map(lambda x: x[0] * x[1], ships)) == 50


def placement_check(lst, ship_type, x, y, orientation, empty_peace):
    if not has_ship(lst, (x, y), empty_peace):
        if orientation == 'horiz' and x + ship_type >= 10:
            return False
        elif orientation == 'vert' and y + ship_type >= 10:
            return False
        else:
            if orientation == 'horiz':
                for i in range(ship_type):
                    if i == 0:
                        try:
                            if lst[x - 1][y] != empty_peace or lst[x][
                                        y - 1] != empty_peace or \
                                            lst[x][y + 1] != empty_peace or \
                                            lst[x - 1][
                                                        y - 1] != empty_peace or \
                                            lst[x - 1][
                                                        y + 1] != empty_peace:
                                return False
                        except IndexError:
                            if lst[x - 1][y] != empty_peace or lst[x][
                                        y - 1] != empty_peace or \
                                            lst[x - 1][
                                                        y - 1] != empty_peace:
                                return False
                    if 0 < i <= ship_type - 2:
                        try:
                            if lst[x + i][y + 1] != empty_peace or lst[x + i][
                                        y - 1] != empty_peace:
                                return False
                        except IndexError:
                            if lst[x + i][y - 1] != empty_peace:
                                return False
                    if i == ship_type - 1:
                        try:
                            if lst[x + i + 1][y - 1] != empty_peace or \
                                            lst[x + i + 1][
                                                        y + 1] != empty_peace or \
                                            lst[x + i][
                                                        y + 1] != empty_peace or \
                                            lst[x + i][
                                                        y - 1] != empty_peace or \
                                            lst[x + i + 1][
                                                y] != empty_peace:
                                return False
                        except IndexError:
                            if lst[x + i + 1][y - 1] != empty_peace or \
                                            lst[x + i][
                                                        y - 1] != empty_peace or \
                                            lst[x + i + 1][
                                                y] != empty_peace:
                                return False
                    if lst[x + i][y] != empty_peace:
                        return False
            elif orientation == 'vert':
                for i in range(ship_type):
                    if i == 0:
                        try:
                            if lst[x][y - 1] != empty_peace or lst[x - 1][
                                y] != empty_peace or \
                                            lst[x + 1][y] != empty_peace or \
                                            lst[x - 1][
                                                        y - 1] != empty_peace or \
                                            lst[x + 1][
                                                        y - 1] != empty_peace:
                                return False
                        except IndexError:
                            if lst[x][y - 1] != empty_peace or lst[x - 1][
                                y] != empty_peace or \
                                            lst[x - 1][
                                                        y - 1] != empty_peace:
                                return False
                    if 0 < i <= ship_type - 2:
                        try:
                            if lst[x + 1][y + i] != empty_peace or lst[x - 1][
                                        y + i] != empty_peace:
                                return False
                        except IndexError:
                            if lst[x - 1][y + i] != empty_peace:
                                return False
                    if i == ship_type - 1:
                        try:
                            if lst[x - 1][y + i + 1] != empty_peace or \
                                            lst[x + 1][
                                                                y + 1 + i] != empty_peace or \
                                            lst[x + 1][
                                                        y + i] != empty_peace or \
                                            lst[x - 1][
                                                        y + i] != empty_peace or \
                                            lst[x][y + i + 1] != empty_peace:
                                return False
                        except IndexError:
                            if lst[x - 1][y + i + 1] != empty_peace or \
                                            lst[x - 1][
                                                        y + i] != empty_peace or \
                                            lst[x][
                                                                y + i + 1] != empty_peace:
                                return False
                    if lst[x][y + i] != empty_peace:
                        return False
        return True
    else:
        return False


# To make standart board you need to change ship objects in this function to '*'
def ship_placement(lst, ship_type, x, y, orientation):
    if orientation == 'horiz':
        for i in range(ship_type):
            lst[x + i][y] = Ship((ship_type, 1), (x, y), type='ship')
    elif orientation == 'vert':
        for i in range(ship_type):
            lst[x][y + i] = Ship((1, ship_type), (x, y), type='ship')
    return lst


def generate_field(empty_peace):
    ships = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    my_field = [[empty_peace for j in range(10)] for i in range(10)]
    for ship in ships.values():
        loop_amount = 5 - ship
        while loop_amount != 0:
            x = randint(0, 9)
            y = randint(0, 9)
            h_v = randint(0, 1)
            if h_v == 0:
                orientation = 'horiz'
            else:
                orientation = 'vert'
            if placement_check(my_field, ship, x, y, orientation, empty_peace):
                ship_placement(my_field, ship, x, y, orientation)
                loop_amount -= 1

    return my_field


def field_to_str(lst):
    """
    :param lst: Our field
    :return: write field to file
    """
    with open('ships.txt', 'w') as file:
        for line in lst:
            file.write(''.join(line) + "\n")
    return 1


class Ship():
    def __init__(self, length=(1, 1), bow=(0, 0), type=None):
        self.type = type
        self.bow = bow
        # I transformed this attribute because there is more need to use it like tuple
        self.__length = length[0] * length[1]
        if length[0] >= 1:
            self.horizontal = True
            self.__coord_list = [(bow[0] + i, bow[1]) for i in
                                 range(self.__length) if
                                 bow[0] + i in range(10)]
        elif length[1] >= 1:
            self.horizontal = False
            self.__coord_list = [(bow[0], bow[1] + i) for i in
                                 range(self.__length) if
                                 bow[1] + i in range(10)]
        self.__hit = [True for i in range(self.__length)]

    def shoot_at(self, coord):
        if coord in self.__coord_list:
            self.__hit[self.__coord_list.index(coord)] = not self.__hit[
                self.__coord_list.index(coord)]

    def __repr__(self):
        return "'*'"

    # 1@property
    def show_booleans(self):
        return self.__hit


class Field:
    def __init__(self):
        self.__ships = generate_field(' ')
        self.__empty_field = [[' ' for i in range(10)] for j in range(10)]

    def shoot_at(self, coord):
        print('aaaaaaaaa')
        if has_ship(self.__ships, coord, ' '):
            self.__ships[coord[1]][coord[0]].shoot_at(
                (coord[1], coord[0]))
            self.__ships[coord[1]][coord[0]], \
            self.__empty_field[coord[1]][coord[0]] = 'X', 'X'
        else:
            self.__ships[coord[1]][coord[0]], \
            self.__empty_field[coord[1]][coord[0]] = 'O', 'O'

    def ret_field(self):
        return self.__ships

    def field_with_ships(self):
        return '\n'.join(list(map(str, self.__ships)))

    def field_without_ships(self):
        return '\n'.join(list(map(str, self.__empty_field)))


class Player:
    def __init__(self, name):
        self.__name = name

    def read_position(self):
        coord = input()
        x, y = ascii_uppercase.index(coord[0].upper()), int(coord[1:]) - 1
        assert x in range(10) and y in range(10), "Wrong params"
        return x, y


class Game:
    def __init__(self, fields=[], players=[], current_player=0):
        self.__fields = fields[:]
        self.__players = players[:]
        self.__current_player = current_player

    def read_position(self, index):
        return self.__players[index].read_position()

    def field_without_ships(self, index):
        return self.__fields[index].field_without_ships()

    def field_with_ships(self, index):
        return self.__fields[index].field_with_ships()

    def ret_field(self):
        return self.__fields

    @staticmethod
    def end_of_the_game(field):
        ships = [ship_size(field, (i, j), ' ') for i in range(1, 11) for j in
                 range(1, 11)]
        if sum(map(lambda x: x[0] * x[1], ships)) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print('-----GAME_BATTlESHIPS-----')
    name_1 = input('Player 1, enter your name: ')
    name_2 = input('Player 2, enter your name: ')
    game = Game([Field(), Field()], [Player(name_1), Player(name_2)])
    while True:
        player = 1
        print('This is your Field')
        print(game.field_with_ships(0))
        print('Player {}, enter move: '.format(player))
        try:
            x, y = game.read_position(player - 1)
            game.ret_field()[0].shoot_at((x, y))
            print(game.field_without_ships(0))
            if game.end_of_the_game(game.ret_field()[0].ret_field()):
                print('Player 2 WON!!! UHUUUUUU')
        except AssertionError as err:
            # print('You entered wrong parameters!!!\n' + ' You will miss your turn')
            print(err)
        player = 2
        print('This is your Field')
        print(game.field_with_ships(1))
        print('Player {}, enter move: '.format(player))
        try:
            x, y = game.read_position(player - 1)
            game.ret_field()[1].shoot_at((x, y))
            print(game.field_without_ships(1))
        except AssertionError as err:
            print(err)
            # print('You entered wrong parameters!!!\n' + ' You will miss your turn')
        if game.end_of_the_game(game.ret_field()[1].ret_field()):
            print('Player 2 WON!!! UHUUUUUU')
