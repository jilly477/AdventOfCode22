# PART ONE ---------------------------
with open('input.txt') as f:
    lines = f.readlines()
sum = 0
for line in lines:
    middle = int(len(line.strip())/2)
    common_letter = ''.join(
        set(line[:middle]).intersection(line[middle:])
    )
    value = ord(common_letter)
    if(value<97):
        sum += value - 38
    else:
        sum += value - 96
print(sum)

# PART TWO ---------------------------
with open('input.txt') as f:
    lines = f.readlines()
sum = 0
counter = 0
for line in lines:
    counter += 1
    if(counter == 1):
        firstElf = line.strip()
    elif(counter == 2):
        secondElf = line.strip()
    else:
        thirdElf = line.strip()
        counter = 0
        common_letter = ''.join(
            set(firstElf).intersection(secondElf).intersection(thirdElf)
        )
        value = ord(common_letter)
        if(value<97):
            sum += value - 38
        else:
            sum += value - 96
print(sum)
