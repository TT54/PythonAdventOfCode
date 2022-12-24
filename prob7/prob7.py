def read_command(line):
    words = line.split(' ')
    words[1] = words[1].replace('\n', '')
    if len(words) > 2:
        words[2] = words[2].replace('\n', '')
    if words[1] == "cd":
        if words[2] == '/':
            return ['cd', '/']
        if words[2] == '..':
            return ['cd', '..']
        return ['cd', words[2]]
    return [words[1], '']


def update_place(last_command: list, place_in_files: str):
    if last_command[0] == 'cd':
        if last_command[1] == '/':
            return '/'
        if last_command[1] == '..':
            files = place_in_files.split('/')
            for f in files:
                if f == '':
                    files.remove(f)
            new_file = '/'
            for i in range(len(files) - 1):
                new_file += files[i] + '/'
            return new_file
        return place_in_files + last_command[1] + '/'


def read_file(place_in_files, tree, line):
    words = line.split(" ")
    words[0] = words[0].replace('\n', '')
    words[1] = words[1].replace('\n', '')
    if words[0] == 'dir':
        tree[place_in_files + words[1] + "/"] = 0
    else:
        size = int(words[0])
        dirs = place_in_files.split("/")
        dirs.pop()
        for i in range(len(dirs)):
            path = ''
            for j in range(i+1):
                path += dirs[j] + "/"
            print(path)
            if not path in tree:
                tree[path] = 0
            tree[path] += size
        #tree[words[1]] = size


def find_most_100k(tree):
    total = 0
    for key in tree:
        if tree[key] <= 100000:
            total += tree[key]
    return total


def do_prob_7():
    with open("prob7Inputs.txt", 'r') as file:
        tree = {}
        last_command = ['', '']
        place_in_files = ''
        for line in file.readlines():
            if line[0] == '$':
                last_command = read_command(line)
                if last_command[0] == 'cd':
                    place_in_files = update_place(last_command, place_in_files)
            else:
                if last_command[0] == 'ls':
                    read_file(place_in_files, tree, line)
        print(tree)
        print("result :", find_most_100k(tree))


#do_prob_7()


def find_best_to_delete(space_required, tree):
    best_to_delete = tree['/']
    for key in tree:
        if tree[key] >= space_required and tree[key] < best_to_delete:
            best_to_delete = tree[key]
    return best_to_delete


def do_prob_7_2():
    with open("prob7Inputs.txt", 'r') as file:
        tree = {}
        last_command = ['', '']
        place_in_files = ''
        for line in file.readlines():
            if line[0] == '$':
                last_command = read_command(line)
                if last_command[0] == 'cd':
                    place_in_files = update_place(last_command, place_in_files)
            else:
                if last_command[0] == 'ls':
                    read_file(place_in_files, tree, line)
        print(tree)
        total_space_used = tree['/']
        space_required = 30000000 - (70000000 - total_space_used)
        print(find_best_to_delete(space_required, tree))


do_prob_7_2()
