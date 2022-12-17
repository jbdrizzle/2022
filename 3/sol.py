file = open("p1.in")
input = file.read()
lines = input.split("\n")

duplicates = []
for line in lines:
    sack1 = line[:int(len(line)/2)]
    sack2 = line[int(len(line)/2):len(line)]
    dict1 = {}
    dict2 = {}
    for item in sack1:
        dict1[item] = "present"
    for item in sack2:
        dict2[item] = "present"
    #print (dict1.keys())
    #print (dict2.keys())
    for key in dict1.keys():
        for key2 in dict2.keys():
            #print(key2)
            if key == key2:
#                print("Found duplicate: ", key)
                duplicates.append(key)
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#print(duplicates)
sum = 0
for num in duplicates:
    val = alphabet.find(num) + 1
    sum = sum + val
    #print(val)
print(sum)
    #print(line)
    #print(sack1)
    #print(sack2)


file = open("p1.in")
input = file.read()
lines = input.split("\n")

duplicates = []
for i in range(int(len(lines)/3)):
    sack1 = lines[int(i*3)]
    sack2 = lines[int(i*3+1)]
    sack3 = lines[int(i*3+2)]

    dict1 = {}
    dict2 = {}
    dict3 = {}
    for item in sack1:
        dict1[item] = "present"
    for item in sack2:
        dict2[item] = "present"
    for item in sack3:
        dict3[item] = "present"

    print(dict1.keys())
    print(dict2.keys())
    print(dict3.keys())

    for key in dict1.keys():
        for key2 in dict2.keys():
            for key3 in dict3.keys():
            #print(key2)
                if (key == key2 and key2 == key3):
#                print("Found duplicate: ", key)
                    duplicates.append(key)
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(duplicates)
sum = 0
for num in duplicates:
    val = alphabet.find(num) + 1
    sum = sum + val
    #print(val)
print(sum)
    #print(line)
    #print(sack1)
    #print(sack2)