file = open("ex.in")
input = file.read()
lines = input.split("\n")

num_dup = 0
num_overlap = 0
for line in lines:
    elf1,elf2 = line.split(',')
    elf_set1 = set()
    elf_set2 = set()
    begin,end = elf1.split("-")
    for item in range(int(begin),int(end)+1):
        elf_set1.add(item)
    begin,end = elf2.split("-")
    for item in range(int(begin),int(end)+1):
        elf_set2.add(item)
    if(elf_set1.issubset(elf_set2) or elf_set2.issubset(elf_set1)):
        #print("Found duplicate with ", elf_set1, elf_set2)
        num_dup = num_dup + 1
    if(elf_set1.intersection(elf_set2) != set()):
        num_overlap = num_overlap + 1
    #print(elf_set1, elf_set2)
print(num_dup)
print(num_overlap)