def find_same(first, second):
    for letter in first:
        if letter in second:
            return letter
    return None


def find_same(first, second, third):
    for letter in first:
        if letter in second and letter in third:
            return letter
    return None


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_letter_value(letter):
    return alphabet.index(letter) + 1


def do_prob_3():
    total = 0
    with open("prob3Inputs.txt", "r") as file:
        for line in file.readlines():
            total += get_letter_value(find_same(line[0: len(line) // 2], line[len(line) // 2: len(line)]))
    return total


def do_prob_3_2():
    total = 0
    with open("prob3Inputs.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            same = find_same(lines[i], lines[i+1], lines[i+2])
            total += get_letter_value(same)
    return total


print(do_prob_3_2())
