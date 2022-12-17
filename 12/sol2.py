import networkx as nx
file = open("p1.in")
input = file.read()
lines = input.split("\n")

map = []

r_i = 0
start_pos = (0,0)
end_pos = (0,0)
for line in lines:
    row = []
    for i in range(len(line)):
        row.append(line[i])
        if(line[i] == 'S'):
            start_pos = (r_i, i)
            row[i] = '`'
        if(line[i] == 'E'):
            end_pos = (r_i,i)
            row[i] = '{'
    map.append(row)
    r_i = r_i + 1
r_max = len(map)-1
c_max = len(map[0])-1

nx_grid = nx.DiGraph()
for r in range(r_max+1):
    for c in range(c_max+1):
        for (x, y) in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_r = r+y
            new_c = c+x
            if(0 <= new_r <= r_max and 0 <= new_c <= c_max):
                if(ord(map[new_r][new_c]) - ord(map[r][c]) <= 1):
                    nx_grid.add_edge((r,c),(new_r,new_c))

path = nx.shortest_path(nx_grid, start_pos, end_pos)
print(len(path)-1)

path_lengths = {}
for r in range(r_max+1):
    for c in range(c_max+1):
        if(map[r][c] == 'a'):
            try:
                path_lengths[(r,c)] = len(nx.shortest_path(nx_grid, (r,c), end_pos))-1
            except:
                None

print(min(path_lengths.values()))
