file = open("p1.in")
input = file.read()
lines = input.split("\n")

for line in lines:
    symbol_list = []
    unique_set = set()
    for i in range(len(line)):
        if(i < 4):
            symbol_list.append(line[i])
            unique_set.add(line[i])
        elif(len(unique_set) == 4):
            print("Found unique symbol at: ", i)
            break
        else:
            symbol_list.pop(0)
            symbol_list.append(line[i])
            unique_set = set(symbol_list)
        #print(symbol_list)
        #print(unique_set)

for line in lines:
    symbol_list = []
    unique_set = set()
    for i in range(len(line)):
        if(i < 14):
            symbol_list.append(line[i])
            unique_set.add(line[i])
        elif(len(unique_set) == 14):
            print("Found unique symbol at: ", i)
            break
        else:
            symbol_list.pop(0)
            symbol_list.append(line[i])
            unique_set = set(symbol_list)
        #print(symbol_list)
        #print(unique_set)
            
