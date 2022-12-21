def read_crate_line(line):
    print(len(line))
    crates = ['' for i in range(len(line) // 4)]
    for i in range(0, len(line), 4):
        if line[i] == '[':
            crates[i//4] = line[i+1]
    return crates


def create_columns(crates_list):
    columns = [[] for i in range(9)]
    crates_list.reverse()
    for list in crates_list:
        for i in range(len(list)):
            if list[i] != "":
                columns[i].append(list[i])
    return columns


def move(crates, amount, column_from, column_to):
    for i in range(amount):
        if len(crates[column_from]) > 0:
            crates[column_to].append(crates[column_from].pop())


def move_2(crates, amount, column_from, column_to):
    moved = []
    for i in range(amount):
        if len(crates[column_from]) > 0:
            moved.append(crates[column_from].pop())
    moved.reverse()
    for crate in moved:
        crates[column_to].append(crate)


def do_prob_5():
    with open("prob5Test.txt", "r") as file:
        part1 = True
        crates_list = []
        crates_column = []
        for line in file.readlines():
            if line == "\n":
                part1 = False
                crates_column = create_columns(crates_list)
                print(crates_column)
            else:
                if part1 and ("[" in line):
                    crates_list.append(read_crate_line(line))
                elif not part1:
                    words = line.split(" ")
                    amount = int(words[1])
                    column_from = int(words[3]) - 1
                    column_to = int(words[5]) - 1
                    move(crates_column, amount, column_from, column_to)
        ret = ""
        for column in crates_column:
            if len(column) > 0:
                ret += column.pop()
        print(ret)


def do_prob_5_2():
    with open("prob5Inputs.txt", "r") as file:
        part1 = True
        crates_list = []
        crates_column = []
        for line in file.readlines():
            if line == "\n":
                part1 = False
                crates_column = create_columns(crates_list)
                print(crates_column)
            else:
                if part1 and ("[" in line):
                    crates_list.append(read_crate_line(line))
                elif not part1:
                    words = line.split(" ")
                    amount = int(words[1])
                    column_from = int(words[3]) - 1
                    column_to = int(words[5]) - 1
                    move_2(crates_column, amount, column_from, column_to)
        ret = ""
        for column in crates_column:
            if len(column) > 0:
                ret += column.pop()
        print(ret)


do_prob_5_2()
