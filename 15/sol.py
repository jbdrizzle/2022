input = "ex.in"
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
else:
    x_max = 4000000

def calc_row(y):
    not_spots = set()
    for sensor in closest_beacons.keys():
        beacon = closest_beacons[sensor]
        manhatten_dist = abs(beacon[0]-sensor[0]) + abs(beacon[1]-sensor[1])
        row_dist = abs(y-sensor[1])
        not_len = manhatten_dist - row_dist
        for x in range(sensor[0]-not_len,sensor[0]+not_len+1):
            if(0 <= x <= x_max):
                not_spots.add(x)
    for beacon in closest_beacons.values():
        if(beacon[1] == y and beacon[0] in not_spots):
            not_spots.remove(beacon[0])
    return len(not_spots)


print(calc_row(10))