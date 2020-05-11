def isValidChessBoard(board_dict):
    # check for one black and one white king
    if "bking" not in board_dict.values() or "wking" not in board_dict.values():
        return False

    # check for a maximum of 16 pieces per player
    black_pieces = 0
    white_pieces = 0
    for colour in board_dict.values():
        if colour[0] == "b":
            black_pieces += 1
        elif colour[0] == "w":
            white_pieces += 1
    if black_pieces >= 16 or white_pieces > 16:
        return False

    # check for at most 8 pawns per player
    if sum(i == "bpawn" for i in board_dict.values()) > 8 or \
            sum(i == "wpawn" for i in board_dict.values()) > 8:
        return False

    # check for a valid location
    board_keys = list(board_dict)  # create list of dictionary keys. eg: ['1h', '6c', '2g', '5h', '3e']
    y = ["1", "2", "3", "4", "5", "6", "7", "8"]
    board_y = [s[:1] for s in board_keys]  # removes letters from list. eg: ['1', '6', '2', '5', '3']
    if not all(elem in y for elem in board_y):  # checks if all values from board_y are in the y-list
        return False

    x = ["a", "b", "c", "d", "e", "f", "g", "h"]
    board_x = [s[1:] for s in board_keys]  # removes numbers from list. eg: ['h', 'c', 'g', 'h', 'e']
    if not all(elem in x for elem in board_x):  # checks if all values from board_x are in the x-list
        return False

    # check if the name starts with a "w" or "b"
    for pieces in board_dict.values():
        if pieces[0] != "b" and pieces[0] != "w":
            return False

    # check if the piece name is valid
    piece_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    for names in board_dict.values():
        if names[1:] not in piece_names:
            return False
    return True


# testing boards
print(isValidChessBoard({"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}))