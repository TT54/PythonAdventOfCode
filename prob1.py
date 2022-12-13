def find_max(file_lines):
    elf_max = 0
    elf = 0
    for line in file_lines:
        if line == '\n':
            if elf > elf_max:
                elf_max = elf
            elf = 0
        else:
            elf += int(line)
    if elf != 0 and elf > elf_max:
        elf_max = elf
    return elf_max


def find_max_for_3(file_lines):
    elf_max = [0, 0, 0]
    elf = 0
    for line in file_lines:
        if line == '\n':
            elf_max = edit_max(elf_max, elf)
            elf = 0
        else:
            elf += int(line)
    if elf != 0:
        elf_max = edit_max(elf_max, elf)
    return elf_max, elf_max[0] + elf_max[1] + elf_max[2]


def edit_max(max:list, value:int):
    '''Vérifie et associe, si nécessaire, la valeur de value aux 3 plus grandes valeurs de max'''
    if value > max[0]:
        max[2], max[1], max[0] = max[1], max[0], value
    elif value > max[1]:
        max[2], max[1] = max[1], value
    elif value > max[2]:
        max[2] = value
    return max


with open("prob1Inputs.txt", "r") as file:
    lines = file.readlines()
    print(find_max(lines))
    print(find_max_for_3(lines))
