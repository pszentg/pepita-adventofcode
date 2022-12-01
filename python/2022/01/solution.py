# https://adventofcode.com/2022/day/1

with open('input.txt') as f:
    calories = 0
    inventory = []
    for line in f:
        if line != "\n":
            calories += int(line.rstrip())
        if line == "\n":
            inventory.append(calories)
            calories = 0

# part 1
max_calories = max(inventory)
print(max_calories)

# part 2
inventory.sort(reverse=True)
total = sum(inventory[0:2])
print(sum(inventory[0:3]))  # equivalent of inventory[0] + inventory[1] + inventory[2]