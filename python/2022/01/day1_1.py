filename = 'list.txt'

# import os
# path = f"{os.getcwd()}\\{filename}"
# file = open(path, 'r')
# list = file.read().splitlines()
# calories_list = []

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
    print(sum_cal)
    print(sum_cal[0] + sum_cal[1] + sum_cal[2])

    for index, value in enumerate(sum_cal):
        if value == 62093:
            print(index)

    

        # print(line)



# for i in list:
#     try:
#         e = int(i)
#         calories_list.append(e)
#     except:
#         calories_list.append(0)
#
# def valami():
#     cal = 0
#     max_cal = 0
#     elf = 0
#     max_elf = 0
#
#     for i in calories_list:
#         cal += i
#         if i == 0:
#             elf += 1
#             if cal > max_cal:
#                 max_cal = cal
#                 max_elf = elf
#             cal = 0
#
#     print(cal)
#     print(max_cal)
#     print(max_elf)
#
# valami()
