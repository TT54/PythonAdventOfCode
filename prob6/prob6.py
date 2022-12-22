def as_double_element(list):
    tempo = []
    for e in list:
        if e in tempo:
            return True
        tempo.append(e)
    return False


def find_first_marker(line):
    last_marker = [line[3 - i] for i in range(4)]
    for i in range(4, len(line)):
        last_marker[3] = last_marker[2]
        last_marker[2] = last_marker[1]
        last_marker[1] = last_marker[0]
        last_marker[0] = line[i]
        if not as_double_element(last_marker):
            print(last_marker)
            return i + 1


def do_prob_6():
    with open("prob6Inputs.txt", 'r') as file:
        for line in file.readlines():
            print(find_first_marker(line))


#do_prob_6()


def find_first_message_marker(line):
    last_marker = [line[13 - i] for i in range(14)]
    for i in range(14, len(line)):
        for j in range(13, 0, -1):
            last_marker[j] = last_marker[j - 1]
        last_marker[0] = line[i]
        if not as_double_element(last_marker):
            print(last_marker)
            return i + 1


def do_prob_6_2():
    with open("prob6Inputs.txt", 'r') as file:
        for line in file.readlines():
            print(find_first_message_marker(line))


do_prob_6_2()
