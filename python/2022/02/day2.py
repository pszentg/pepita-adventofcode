with open('input.txt') as f:
    point = 0

    for line in f:
        game = line.rstrip().replace(' ', '')
        if game[1] == 'X':
            point += 1
            if game[0] == 'A':
                point += 3
            elif game[0] == 'B':
                pass
            elif game[0] == 'C':
                point += 6

        if game[1] == 'Y':
            point += 2
            if game[0] == 'A':
                point += 6
            elif game[0] == 'B':
                point += 3
            elif game[0] == 'C':
                pass

        if game[1] == 'Z':
            point += 3
            if game[0] == 'A':
                pass
            elif game[0] == 'B':
                point += 6
            elif game[0] == 'C':
                point += 3

    print(point)

with open('input.txt') as f:
    point = 0

    for line in f:
        game = line.rstrip().replace(' ', '')
        if game[1] == 'X':
            if game[0] == 'A':
                point += 3
            elif game[0] == 'B':
                point += 1
            elif game[0] == 'C':
                point += 2

        if game[1] == 'Y':
            point += 3
            if game[0] == 'A':
                point += 1
            elif game[0] == 'B':
                point += 2
            elif game[0] == 'C':
                point += 3

        if game[1] == 'Z':
            point += 6
            if game[0] == 'A':
                point += 2
            elif game[0] == 'B':
                point += 3
            elif game[0] == 'C':
                point += 1

    print(point)

