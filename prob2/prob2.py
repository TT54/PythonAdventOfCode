def get_move(input):
    if input == "A" or input == "X": return "R"
    if input == "B" or input == "Y": return "P"
    return "S"


def get_winner(move1, move2):
    """Renvoie 1 pour le joueur 1, 2 pour le joueur 2 et 3 en cas d'égalité"""
    if move1 == "R":
        if move2 == "P": return 2
        if move2 == "S": return 1
    elif move1 == "S":
        if move2 == "R": return 2
        if move2 == "P": return 1
    elif move1 == "P":
        if move2 == "S": return 2
        if move2 == "R": return 1
    return 0


def get_move_points(move):
    if move == "R": return 1
    if move == "P": return 2
    return 3


def get_points(adversary, player):
    move1 = get_move(adversary)
    move2 = get_move(player)
    points = get_move_points(move2)
    winner = get_winner(move1, move2)
    if winner == 0: points += 3
    if winner == 2: points += 6
    return points


def get_move_2(move1, result_needed):
    if result_needed == "X":
        if move1 == "R": return "S"
        if move1 == "P": return "R"
        return "P"
    if result_needed == "Y":
        return move1
    if result_needed == "Z":
        if move1 == "P": return "S"
        if move1 == "S": return "R"
        return "P"


def get_points_2(adversary, player):
    move1 = get_move(adversary)
    move2 = get_move_2(move1, player)
    points = get_move_points(move2)
    winner = get_winner(move1, move2)
    if winner == 0: points += 3
    if winner == 2: points += 6
    return points


def do_prob2():
    with open('prob2Inputs.txt', 'r') as file:
        total_points = 0
        for line in file.readlines():
            total_points += get_points(line[0], line[2])
        print(total_points)


def do_prob2_2():
    with open('prob2Inputs.txt', 'r') as file:
        total_points = 0
        for line in file.readlines():
            total_points += get_points_2(line[0], line[2])
        print(total_points)


do_prob2_2()
