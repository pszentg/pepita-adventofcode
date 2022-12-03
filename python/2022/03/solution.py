# https://adventofcode.com/2022/day/3

# a little help:
# https://docs.python.org/3/library/functions.html?highlight=ord#ord
# https://en.wikipedia.org/wiki/List_of_Unicode_characters

# part 1

def convert_to_prio(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


with open('input.txt') as f:
    prio_sum = 0
    for line in f:
        rucksack = line.rstrip()
        items_in_rucksack = len(rucksack)
        comp1 = rucksack[:int(items_in_rucksack/2)]
        comp2 = rucksack[int(items_in_rucksack/2):items_in_rucksack]

        # print(comp1)
        # print(comp2)
        # print('-------')

        prio1 = {}
        prio2 = {}

        for c in comp1:
            prio1[c] = convert_to_prio(c)

        for c in comp2:
            prio2[c] = convert_to_prio(c)

        # print(prio1)
        # print(prio2)
        # print('----------')

        for k, v in prio1.items():
            if k in prio2:
                prio_sum += v

    print(prio_sum)

# part 2

with open('input.txt') as f:
    lines = []
    sum_prios = 0

    for line in f:
        lines.append(line.rstrip())

    composite_lines = [lines[x:x+3] for x in range(0, len(lines), 3)]

    # print(composite_lines)

    prios = {}

    for index, group in enumerate(composite_lines):
        prios[index] = []
        for rucksack in group:
            rucksack_prios = {}
            for c in rucksack:
                rucksack_prios[c] = convert_to_prio(c)
            prios[index].append(rucksack_prios)

    for item in prios.values():
        for k, v in item[0].items():
            if k in item[1] and k in item[2]:
                sum_prios += v

    print(sum_prios)
