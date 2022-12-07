# PART ONE ----------------------
with open('input.txt') as f:
    lines = f.readlines()
sum = 0
for line in lines:
    ranges = line.strip().split(',')
    elfOne = ranges[0].split('-')
    elfTwo = ranges[1].split('-')

    if(
        (int(elfOne[0]) >= int(elfTwo[0]) and int(elfOne[1]) <= int(elfTwo[1])) or 
        (int(elfTwo[0]) >= int(elfOne[0]) and int(elfTwo[1]) <= int(elfOne[1]))):
        sum += 1
print(sum)

# PART TWO ----------------------
with open('input.txt') as f:
    lines = f.readlines()
sum = 0
for line in lines:
    ranges = line.strip().split(',')
    elfOne = ranges[0].split('-')
    elfTwo = ranges[1].split('-')

    # print(elfOne[0] + " " + elfOne[1] + " " + elfTwo[0] + " " + elfTwo[1])
    if(
        (int(elfOne[0]) >= int(elfTwo[0]) and int(elfOne[0]) <= int(elfTwo[1])) or 
        (int(elfOne[1]) >= int(elfTwo[0]) and int(elfOne[1]) <= int(elfTwo[1])) or
        (int(elfTwo[0]) >= int(elfOne[0]) and int(elfTwo[0]) <= int(elfOne[1])) or 
        (int(elfTwo[1]) >= int(elfOne[0]) and int(elfTwo[1]) <= int(elfOne[1]))):
        sum += 1
print(sum)