# https://adventofcode.com/2022/day/2

with open('input.txt') as f:

    # part 1

    # +  A    B    C
    # X  4    1    7
    # Y  8    5    2
    # Z  3    9    6

    points = 0
    for line in f:
        game = line.rstrip().replace(" ", "")
        if game[1] == 'X':
            points += 1
            if game[0] == "A":
                points += 3
            if game[0] == "B":
                pass
            if game[0] == "C":
                points += 6

        if game[1] == 'Y':
            points += 2
            if game[0] == "A":
                points += 6
            if game[0] == "B":
                points += 3
            if game[0] == "C":
                pass

        if game[1] == 'Z':
            points += 3
            if game[0] == "A":
                pass
            if game[0] == "B":
                points += 6
            if game[0] == "C":
                points += 3

    print(points)

# part 2

# have to open again because previously the iterator went to the end of the file - need to move it to the beginning
with open('input.txt') as f:

    # +  A    B    C
    # X  3    1    2
    # Y  4    5    6
    # Z  8    9    7

    points = 0
    for line in f:
        game = line.rstrip().replace(" ", "")
        if game[1] == 'X':
            if game[0] == "A":
                points += 3
            if game[0] == "B":
                points += 1
            if game[0] == "C":
                points += 2

        if game[1] == 'Y':
            points += 3
            if game[0] == "A":
                points += 1
            if game[0] == "B":
                points += 2
            if game[0] == "C":
                points += 3

        if game[1] == 'Z':
            points += 6
            if game[0] == "A":
                points += 2
            if game[0] == "B":
                points += 3
            if game[0] == "C":
                points += 1

    print(points)

