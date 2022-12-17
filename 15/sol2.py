input = "p1.in"
pairs = [line.split(": ")[0:2] for line in open(input).read().split("\n")] 

closest_beacons = {}
for pair in pairs:
    sensor = pair[0].split(' ')[2:]
    sensor[0] = sensor[0][2:-1]
    sensor[1] = sensor[1][2:]
    beacon = pair[1].split(' ')[4:]
    beacon[0] = beacon[0][2:-1]
    beacon[1] = beacon[1][2:]
    closest_beacons[(int(sensor[0]), int(sensor[1]))] = (int(beacon[0]), int(beacon[1]))

if(input == "ex.in"):
    x_max = 20
    y_max = 20
else:
    x_max = 4000000
    y_max = 4000000

def calc_row(y):
    impossible_ranges = []
    l_bound = 0
    r_bound = x_max
    for sensor in closest_beacons.keys():
        beacon = closest_beacons[sensor]
        manhatten_dist = abs(beacon[0]-sensor[0]) + abs(beacon[1]-sensor[1])
        row_dist = abs(y-sensor[1])
        not_len = manhatten_dist - row_dist
        if(not_len > 0):
            impossible_ranges.append((sensor[0]-not_len,sensor[0]+not_len))
    for range in sorted(impossible_ranges):
        if(range[0] < 0 and range[1] >= l_bound):
            l_bound = range[1]+1
        else:
            if(range[0] > l_bound):
                print(sorted(impossible_ranges))
                print("Found l_bound=",l_bound,"and range=",range)
                return l_bound
            elif(range[1] >= l_bound):
                l_bound = range[1]+1

    return -1    


for y in range(y_max):
    spot = calc_row(y)
    if(y%250000 == 0):
        print("at row: ",y)

    if(spot > 0):
        print(y)
        print(spot)
        print(spot*x_max+y)
        break