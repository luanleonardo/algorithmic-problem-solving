# https://www.hackerrank.com/challenges/crossword-puzzle
# https://programs.programmingoneonone.com/2021/03/hackerrank-crossword-puzzle-solution.html

from copy import deepcopy


def fill_board(board, words):
    if len(words) == 0:
        for a in board:
            for b in a:
                print(b, end="")
            print("")
    first_open_space = open_space_finder(board)
    result = word_placer(first_open_space, board, words)
    if not result:
        return False


def open_space_finder(board):
    for a in range(len(board)):
        for b in range(len(board[a])):
            if board[a][b] == "-":
                return word_finder([a, b], board)


def word_finder(open_space, board):
    word_place = []
    x = open_space[0]
    y = open_space[1]
    if x in range(1, len(board) - 1):
        if look_up(x, y, board):
            word_place.append([x - 1, y])
            word_place.append(open_space)
            return fill_down(word_place, board)
        if look_down(x, y, board):
            word_place.append(open_space)
            word_place.append([x + 1, y])
            return fill_down(word_place, board)
    elif x == 0:
        if look_down(x, y, board):
            word_place.append(open_space)
            word_place.append([x + 1, y])
            return fill_down(word_place, board)

    if y in range(1, len(board[y]) - 1):
        if look_left(x, y, board):
            word_place.append([x, y - 1])
            word_place.append(open_space)
            return fill_across(word_place, board)
        if look_right(x, y, board):
            word_place.append(open_space)
            word_place.append([x, y + 1])
            return fill_across(word_place, board)
    elif y == 0:
        if look_right(x, y, board):
            word_place.append(open_space)
            word_place.append([x, y + 1])
            return fill_across(word_place, board)


def look_up(x, y, board):
    return board[x - 1][y] != "+"


def look_down(x, y, board):
    return board[x + 1][y] != "+"


def look_left(x, y, board):
    return board[x][y - 1] != "+"


def look_right(x, y, board):
    return board[x][y + 1] != "+"


def fill_down(place_list, board):
    where_to_start = place_list[len(place_list) - 1]
    x = where_to_start[0] + 1
    y = where_to_start[1]
    while x < len(board):
        if board[x][y] != "+":
            place_list.append([x, y])
            x += 1
        else:
            x = len(board)
    return place_list


def fill_across(place_list, board):
    where_to_start = place_list[len(place_list) - 1]
    x = where_to_start[0]
    y = where_to_start[1] + 1
    while y < len(board[x]):
        if board[x][y] != "+":
            place_list.append([x, y])
            y += 1
        else:
            y = len(board[x])
    return place_list


def word_placer(place_list, board, words):
    words_that_fit = [X for X in words if len(X) == len(place_list)]

    for a in words_that_fit:
        board1 = deepcopy(board)
        words1 = deepcopy(words)
        for index in range(len(a)):
            x = place_list[index][0]
            y = place_list[index][1]
            if board[x][y] == "-":
                board1[x][y] = a[index]
            else:
                if board[x][y] != a[index]:
                    break
            if index == len(a) - 1:
                words1.remove(a)
                buzz = fill_board(board1, words1)
                break
    return False


first_board = []
for x in range(10):
    string = input()
    string_list = list(string)
    first_board.insert(x, string_list)
words = input().split(";")
fill_board(first_board, words)
