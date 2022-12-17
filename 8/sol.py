import pprint
file = open("p1.in")
input = file.read()
lines = input.split("\n")

num_rows = 0
num_cols = 0
grid = []
vis_grid = []
scenic_grid = []
for line in lines:
    row = []
    for char in line:
        row.append(int(char))
    grid.append(row)
    num_cols = len(row)
num_rows = len(grid)

pprint.pprint(grid)

def check_vis(row,col):
    temp_vis = [True, True, True, True]
    scenic_score = [col,len(grid[row])-col-1,row,len(grid)-row-1]
    height = grid[row][col]
    vis = True
    for _col in range(col): # look left
        tree = grid[row][_col]
        if(tree >= height):
            temp_vis[0] = False
            scenic_score[0] = col - _col
    for _col in range(len(grid[row])-1,col, -1): # look right
        tree = grid[row][_col]
        if(tree >= height):
            temp_vis[1] = False
            scenic_score[1] = _col - col
    for _row in range(row): # look up
        tree = grid[_row][col]
        if(tree >= height):
            temp_vis[2] = False
            scenic_score[2] = row - _row
    for _row in range(len(grid)-1,row,-1): # look down
        tree = grid[_row][col]
        if(tree >= height):
            temp_vis[3] = False
            scenic_score[3] = _row - row
    scenic_grid[row][col] = (scenic_score[0] * scenic_score[1] *  scenic_score[2] * scenic_score[3])
    return (temp_vis[0] or temp_vis[1] or temp_vis[2] or temp_vis[3])

for row in range(num_rows):
    vis_grid.append([])
    scenic_grid.append([])
    for col in range(num_cols):
        vis_grid[row].append(False)
        scenic_grid[row].append(0)

num_vis = 0
for row in range(num_rows):
    for col in range(num_cols):
        result = vis_grid[row][col] = check_vis(row,col)
        if(result):
            num_vis = num_vis + 1


#pprint.pprint(vis_grid)
print(num_vis)
pprint.pprint(scenic_grid)

max_vis = 0
for row in scenic_grid:
    for col in row:
        if(col > max_vis):
           max_vis = col
print(max_vis)
