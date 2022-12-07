# PART ONE ------------------------
# define the beginning stack
# stacks = [
#     ['B','V','S','N','T','C','H','Q'],
#     ['W','D','B','G'],
#     ['F','W','R','T','S','Q','B'],
#     ['L','G','W','S','Z','J','D','N'],
#     ['M','P','D','V','F'],
#     ['F','W','J'],
#     ['L','N','Q','B','J','V'],
#     ['G','T','R','C','J','Q','S','N'],
#     ['J','S','Q','C','W','D','M']
# ]

# # read instructions and perform them
# with open('input.txt') as f:
#     lines = f.readlines()
# for line in lines:
#     instr = line.strip().split(' ')
#     for x in range(int(instr[1])):
#         stacks[int(instr[5])-1].append(stacks[int(instr[3])-1].pop())

# # print all the crates at the top of each stack
# for stack in stacks:
#     print(stack[-1], end='')
# print('')


# PART TWO ------------------------
# define the beginning stack
stacks = [
    ['B','V','S','N','T','C','H','Q'],
    ['W','D','B','G'],
    ['F','W','R','T','S','Q','B'],
    ['L','G','W','S','Z','J','D','N'],
    ['M','P','D','V','F'],
    ['F','W','J'],
    ['L','N','Q','B','J','V'],
    ['G','T','R','C','J','Q','S','N'],
    ['J','S','Q','C','W','D','M']
]

# read instructions and perform them
with open('input.txt') as f:
    lines = f.readlines()
for line in lines:
    instr = line.strip().split(' ')
    stacks[int(instr[5])-1].extend(stacks[int(instr[3])-1][-int(instr[1]):])
    del stacks[int(instr[3])-1][-int(instr[1]):]

# print all the crates at the top of each stack
for stack in stacks:
    print(stack[-1], end='')
print('')
