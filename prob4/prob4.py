def get_numbers_between(indexes:str):
    first, second = indexes.split("-")[0], indexes.split("-")[1]
    return range(int(first), int(second) + 1)


def do_prob_4():
    with open("prob4Inputs.txt", 'r') as file:
        count = 0
        for line in file.readlines():
            split = line.split(",")
            elf1 = get_numbers_between(split[0])
            elf2 = get_numbers_between(split[1])
            isIn = True
            for i in elf1:
                if not i in elf2:
                    isIn = False
                    break
            if not isIn:
                isIn = True
                for i in elf2:
                    if not i in elf1:
                        isIn = False
                        break
            if isIn:
                count += 1
        print(count)


#do_prob_4()


def do_prob_4_2():
    with open("prob4Inputs.txt", 'r') as file:
        count = 0
        for line in file.readlines():
            split = line.split(",")
            elf1 = get_numbers_between(split[0])
            elf2 = get_numbers_between(split[1])
            isIn = False
            for i in elf1:
                if i in elf2:
                    isIn = True
                    break
            if isIn:
                count += 1
        print(count)


do_prob_4_2()
