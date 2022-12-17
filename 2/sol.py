file = open("p1.in")
input = file.read()
lines = input.split("\n")

total_score = 0
for line in lines:
    p1, p2 = line.split(' ')

    if p2 == 'X':
        total_score = total_score + 1
        if(p1 == 'A'):
            total_score = total_score + 3
        elif(p1 == 'C'):
            total_score = total_score + 6
    elif p2 == 'Y':
        total_score = total_score + 2
        if(p1 == 'A'):
            total_score = total_score + 6
        elif(p1 == 'B'):
            total_score = total_score + 3
    elif p2 == 'Z':
        total_score = total_score + 3
        if(p1 == 'B'):
            total_score = total_score + 6
        elif(p1 == 'C'):
            total_score = total_score + 3

print(total_score)

total_score = 0
for line in lines:
    p1, p2 = line.split(' ')

    if p1 == 'A':
        if(p2 == 'X'):
            total_score = total_score + 3
        elif(p2 == 'Y'):
            total_score = total_score + 4
        else:
            total_score = total_score + 8
    elif p1 == 'B':
        if(p2 == 'X'):
            total_score = total_score + 1
        elif(p2 == 'Y'):
            total_score = total_score + 5
        else:
            total_score = total_score + 9
    elif p1 == 'C':
        if(p2 == 'X'):
            total_score = total_score + 2
        elif(p2 == 'Y'):
            total_score = total_score + 6
        else:
            total_score = total_score + 7

print(total_score)