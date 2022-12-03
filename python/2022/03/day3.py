def convert(car):
    if car.islower():
        return ord(car) - 96
    else:
        return ord(car) - 38


with open('input.txt') as f:
    point = 0

    for line in f:
        rucksack = line.rstrip()
        comp1 = rucksack[:int(len(rucksack) / 2)]
        comp2 = rucksack[int(len(rucksack) / 2):len(rucksack)]

        prio1 = {}
        prio2 = {}

        # for c1 in comp1:
        #     # if c in comp2:
        #     for c2 in comp2:
        #         if c1 == c2:

        for c in comp1:
            prio1[c] = convert(c)
        for c in comp2:
            prio2[c] = convert(c)
        # print(prio1)
        # print(prio2)
        # print('----------------')
        for key, value in prio1.items():
            if key in prio2:
                point += value
    print(point)
