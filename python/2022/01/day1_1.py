
with open('list.txt') as f:
    cal = 0
    sum_cal = []

    for line in f:
        if line == '\n':
            sum_cal.append(cal)
            cal = 0
        else:
            cal += int(line)

    print(max(sum_cal))

    sum_cal.sort(reverse=True)

    print(sum(sum_cal[0:3]))

    # print(sum_cal)
    # print(sum_cal[0] + sum_cal[1] + sum_cal[2])

    # print(line)