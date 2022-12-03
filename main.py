# Day 1 solution

with open("Input_Day1.txt") as f:
    inp = sorted(sum(int(y) for y in x.split("\n")) for x in f.read().split("\n\n"))
    #Using regex will help with dealing with the blank lines in the input file (\n\n to separate by each blank line and ignore it).

    Part1 = inp[-1]
    print("Day 1_part 1:", Part1)
    
    Part2 = sum(inp[-3:])
    print("Day 1_part 2:", Part2)

# Day 2 solution

combinations_part1 = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
print("Day 2_part 1:", sum(combinations_part1[x] for x in [x.strip() for x in open("Input_Day2.txt").readlines()]))

combinations_part2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
print("Day 2_part 2:", sum(combinations_part2[x] for x in [x.strip() for x in open("Input_Day2.txt").readlines()]))

# Day 3 solution

with open("Input_Day3.txt") as f:
    ruscksacks = [i.strip() for i in f.readlines()]

sum_priorities = 0
for i in ruscksacks:
    first_compartment = i[:int(len(i) / 2)]
    second_compartment = i[int(len(i) / 2):]
    both_compartments = (list(set(first_compartment).intersection(set(second_compartment)))[0])
    if both_compartments.isupper():
        sum_priorities += (ord(both_compartments) - 38) #Code unicode for "A" is 39
    elif both_compartments.islower():
        sum_priorities += (ord(both_compartments) - 96) #Code unicode for "a" is 97
        
print("Day 3_part 1:",sum_priorities)

sum_priorities = 0
for i in range(0, len(ruscksacks), 3):
    a, b, c = [set(items) for items in ruscksacks[i:i+3]]
    character = list(a & b & c)[0]
    if character.isupper():
        sum_priorities += (ord(character) - 38)
    elif character.islower():
        sum_priorities += (ord(character) - 96)

print("Day 3_part 2:",sum_priorities)