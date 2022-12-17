import networkx as nx
import matplotlib.pyplot as plt
import itertools
lines = open("p1.in").read().split("\n")

class Valve():
    def __init__(self, _name, _rate, _paths):
        self.name = _name
        self.rate = _rate
        self.paths = _paths
        self.open = False
        self.pressure_released = 0

    def open_valve(self):
        self.open = True

    def get_rate(self):
        if(self.open):
            return self.rate
        else:
            return 0

    def tick(self):
        self.pressure_released = self.pressure_released + self.get_rate()

    def __str__(self):
        if(self.open):
            return "Valve {}: currently open, releasing {} each tick, totaled {} units released so far.".format(self.name, self.rate, self.pressure_released)
        else:
            return "Valve {}: currently closed, can release {} each tick, totaled {} units released so far.".format(self.name, self.rate, self.pressure_released)



valves = {}
valve_maps = {}
for line in lines:
    tokens = line.split(" ")
    name = tokens[1]
    rate = int(tokens[4][5:-1])
    paths = ''.join(tokens[9:]).split(',')
    valves[name] = Valve(name,rate,paths)
    #valves[name].open_valve()

nx_map = nx.Graph()
for v in valves.values():
    for path in v.paths:
        nx_map.add_edge(v.name, path)
#        nx.set_node_attributes(nx_map, {v.name : {"has_flow": v.rate > 0}})
#for key in valves.keys():
#    print(nx_map.nodes[key])
#nx.draw_networkx(nx_map, pos=nx.spring_layout(nx_map))
#plt.show()

def get_length_of_path(path):
    length = nx.shortest_path_length(nx_map, 'AA', path[0])
    for i in range(len(path)-1):
        length = length + nx.shortest_path_length(nx_map, path[i], path[i+1])
    return length + len(path) # returning distance + num valves opened

#print(do_all_ticks_all(False))
#print(potential_returns('AA', 30))
#tick_all()
valves_with_flow = [valve for valve in valves.values() if valve.rate > 0]

all_paths_with_flow = []

prev_len = 0
new_len = -1
done_dict = {}
path_length_dict = {}

for valve in valves_with_flow:
    all_paths_with_flow.append([valve.name])
print(all_paths_with_flow)

for path in all_paths_with_flow:
    done_dict[''.join(path)] = False
    path_length_dict[''.join(path)] = get_length_of_path(path)


path_lut = {}
for valve1 in valves_with_flow:
    path_lut[valve1.name] = {}
    for valve2 in valves_with_flow:
        path_lut[valve1.name][valve2.name] = nx.shortest_path_length(nx_map, valve1.name, valve2.name)
print(path_lut) 

start_num_ticks = 30
while(prev_len != new_len):
    prev_len = len(all_paths_with_flow)

    #for path in all_paths_with_flow:
    for i in range(len(all_paths_with_flow)):
        path = all_paths_with_flow[i]
        path_str = ''.join(path)
        if(done_dict[path_str] == True):
            continue
        path_length = path_length_dict[path_str]
        found_new_path = False

        for valve2 in valves_with_flow:
            if(valve2.name not in path):
                #new_path_length = path_length + 1 + nx.shortest_path_length(nx_map, path[-1], valve2.name)
                new_path_length = path_length + 1 + path_lut[path[-1]][valve2.name]
                if(new_path_length < start_num_ticks):
                    found_new_path = True
                    new_path = path.copy()
                    new_path.append(valve2.name)
                    all_paths_with_flow.append(new_path)
                    done_dict[''.join(new_path)] = False
                    path_length_dict[''.join(new_path)] = new_path_length

        if(found_new_path):
            del all_paths_with_flow[i]
        else:
            done_dict[path_str] = True
    new_len = len(all_paths_with_flow)
    print(new_len)



#all_paths_with_flow = list(itertools.permutations(valves_with_flow))
#for valve in valves_with_flow:
#    construct_paths

max_flow = 0
max_path = []
for i in range(len(all_paths_with_flow)):
    total_flow = 0
    path = all_paths_with_flow[i]
    num_ticks = start_num_ticks - nx.shortest_path_length(nx_map, 'AA', path[0]) # initialize number of ticks = 30 - travel time from start to first valve
    for j in range(len(path)-1):
        num_ticks = num_ticks - 1 # one tick used to open valve
        total_flow = total_flow + (num_ticks)*valves[path[j]].rate # add all flow you'll get after opening the valve
        num_ticks = num_ticks - nx.shortest_path_length(nx_map, path[j], path[j+1]) # remove travel time to next valve
    total_flow = total_flow + (num_ticks-1)*valves[path[-1]].rate # add the flow from the final valve
    #print ([valve.name for valve in path], "total={}".format(total_flow))
    #print(path, "total={}".format(total_flow))
    if(total_flow > max_flow):
        max_flow = total_flow
        max_path = path

print(max_flow, max_path)
#for valve in valves_with_flow:
#    print (valve)
