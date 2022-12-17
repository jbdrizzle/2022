packet_pairs = [pair.split("\n") for pair in (open("p1.in").read().split("\n\n"))]

def check_pair(p0, p1):
    i=0
    while(i < min(len(p0),len(p1))):
        if(type(p0[i]) == int and type(p1[i]) == int):
            if(p0[i] < p1[i]):
                return -1
            elif(p0[i] > p1[i]):
                return 1
            i = i + 1
        elif(type(p0[i]) == list and type(p1[i]) == list):
            check = check_pair(p0[i], p1[i])
            if(check != 0):
                return check
            i = i + 1
        elif((type(p0[i]) == int and type(p1[i]) == list) or (type(p0[i]) == list and type(p1[i]) == int)):
            new_list = []
            check = 0
            if(type(p0[i]) == int):
                new_list.append(p0[i])
                check = check_pair(new_list, p1[i])
            else:
                new_list.append(p1[i])
                check = check_pair(p0[i], new_list)
            if(check != 0):
                return check
            i = i + 1
    if(len(p0) < len(p1)):
        return -1
    elif(len(p0) > len(p1)):
        return 1
    return 0

def make_list(stuff):
    my_list = []
    stuff = stuff[1:-1] #strip []
    arr = stuff.split(',')
    i = 0
    while(i < len(arr) and arr[0] != ''):
        if(arr[i].isdigit()):
            my_list.append(int(arr[i]))
            i = i + 1
        elif(arr[i].find('[') != -1):
            begin = arr[i].find('[')
            end = arr[i].rfind(']')
            if(end != -1 and arr[i].count('[') - arr[i].count(']') == 0):
                my_list.append(make_list(''.join(arr[i][begin:end+1])))
                i = i + 1
            else:
                num_opens = 0
                for j in range(i, len(arr)):
                    num_opens = num_opens + arr[j].count('[') - arr[j].count(']')
                    if(arr[j].find(']')!=-1 and num_opens == 0):
                        end = arr[j].find(']')
                        my_list.append(make_list(','.join(arr[i:j+1])))
                        i = j + 1
                        break
                        
    return my_list            

i = 1
sum = 0
packets = []
packets.append(make_list("[[2]]"))
packets.append(make_list("[[6]]"))
for pair in packet_pairs:
    p0 = pair[0]
    p1 = pair[1]
    temp_p0 = make_list(p0)
    temp_p1 = make_list(p1)
    inserted = False
    for j in range(len(packets)):
        if(check_pair(temp_p0, packets[j]) < 0):
            packets.insert(j, temp_p0)
            inserted = True
            break
    if not inserted:
        packets.append(temp_p0)
    inserted = False
    for j in range(len(packets)):
        if(check_pair(temp_p1, packets[j]) < 0):
            packets.insert(j, temp_p1)
            inserted = True
            break
    if not inserted:
        packets.append(temp_p1)
    result  = check_pair(make_list(p0), make_list(p1))
    if(result == -1):
        sum = sum + i
    i = i + 1

print(sum)

for i in range(len(packets)):
    if(packets[i] == [[2]]):
        print("Found [[2]] at", i+1)
    elif(packets[i] == [[6]]):
        print("Found [[6]] at", i+1)