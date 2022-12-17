monkeys = []

class Monkey():
    def __init__(self, _index, _items, _op, _test, _true_targ, _false_targ):
        _items = _items.split(": ")[1]
        self.items = []
        for thing in _items.split(", "):
            self.items.append(int(thing))
        
        _op = _op.split(": ")[1]
        self.op    = _op.split(" ")[3]
        self.arg   = _op.split(" ")[4]

        _test = _test.split(": ")[1]
        self.test  = int(_test.split(' ')[2])

        _true_targ = _true_targ.split(": ")[1]
        self.true_targ = int(_true_targ.split(" ")[3])

        _false_targ = _false_targ.split(": ")[1]
        self.false_targ = int(_false_targ.split(" ")[3])

        self.inspection_count = 0
        self.index = _index

    def __str__(self):
        print
        return "Monkey {}:\n  Items: {}\n  Operation: new = old {} {}\n  Test: divisible by {}\n    If true: throw to monkey {}\n    If false: throw to monkey {}\n  Inspection count:{}".format(self.index,self.items, self.op, self.arg, self.test, self.true_targ, self.false_targ, self.inspection_count)

    def update_worry(self):
        for i in range(len(self.items)):
            self.items[i] = self.calc_worry(self.items[i])

    def calc_worry(self, item):

        arg = self.arg

        if(arg == "old"):
            arg = int(item)
        else:
            arg = int(arg)
        if(self.op[0] == "+"):
            item = item + arg
        elif(self.op[0] == "*"):
            item = item * arg
        elif(self.op[0] == "/"):
            item = int(item / arg)
        else:
            item = item - arg
        return item
    
    def check_items(self):
        targets = []
        for i in range(len(self.items)):
            lcm = 1
            for monkey in monkeys:
                lcm = lcm * monkey.test
            self.items[i] = self.items[i] % lcm
            #self.items[i] = int(self.items[i]/3)
            self.inspection_count = self.inspection_count + 1

            if (self.items[i] % self.test == 0):
                targets.append(self.true_targ)
            else:
                targets.append(self.false_targ)
                #print("Throwing item: ", self.items[i])
        return targets

monkeys = []

file = open("p1.in")
input = file.read()
stuff = input.split("\n\n")

index = 0
for monk in stuff:
    lines = monk.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].lstrip()
    monkeys.append(Monkey(index, lines[1], lines[2], lines[3], lines[4], lines[5]))
    index = index + 1

def do_round():
    for monkey in monkeys:
        monkey.update_worry()
        thrown = monkey.check_items()
        for throw in thrown:
            (monkeys[throw]).items.append(monkey.items.pop(0))


for i in range(10000):
    print("On round",i)
    do_round()
for monk in monkeys:
    print(str(monk))

max1 = 0
max2 = 0
for monk in monkeys:
    if(monk.inspection_count >= max1):
        max2 = max1
        max1 = monk.inspection_count

print(max1*max2)