import re
from queue import Queue
        
class Coord:
    def __init__(self,x,y,dist_from_st):
        self.x = x
        self.y = y
        self.dist_from_st = dist_from_st

def get_st_idx(input_data):
    for i,line in enumerate(input_data):
        match = re.match(r".*(S)",line)
        if not match == None:
            return match.end()-match.start() - 1 , i

def check_valid(map, x_coord,y_coord,pos):
    if pos == 'L':
        return map[y_coord][x_coord] == '-' or map[y_coord][x_coord] == 'L' or map[y_coord][x_coord] == 'F'
    if pos == 'R':
        return map[y_coord][x_coord] == '-' or map[y_coord][x_coord] == 'J' or map[y_coord][x_coord] == '7'
    if pos == 'U':
        return map[y_coord][x_coord] == '|' or map[y_coord][x_coord] == '7' or map[y_coord][x_coord] == 'F'
    if pos == 'D':
        return map[y_coord][x_coord] == '|' or map[y_coord][x_coord] == 'L' or map[y_coord][x_coord] == 'J'

def update_dist_map(map,dist_map,x_coord,y_coord,dist_from_st,q):
    if dist_map[y_coord][x_coord] == 0:
        dist_map[y_coord][x_coord] = dist_from_st
        if x_coord >= 0:
            if check_valid(map, x_coord - 1, y_coord,'L'):
                q.put(Coord(x_coord - 1, y_coord, dist_from_st + 1))
        if y_coord >= 0:
            if check_valid(map, x_coord,y_coord - 1, 'U'):
                q.put(Coord(x_coord, y_coord - 1, dist_from_st + 1))
        if x_coord < len(map[y_coord]) - 1:
            if check_valid(map, x_coord + 1,y_coord, 'R'):
                q.put(Coord(x_coord + 1, y_coord, dist_from_st + 1))
        if y_coord < len(map) - 1:
            if check_valid(map, x_coord,y_coord + 1, 'D'):
                q.put(Coord(x_coord, y_coord + 1, dist_from_st + 1))

def main():
    with open("./day10input.txt","r") as file:
        map = file.read()
    
    map = map.splitlines()
    st_x,st_y = get_st_idx(map)
    st_coord = Coord(st_x,st_y,0)
    dist_map = [
        [0] * len(line) for line in map
    ]
    q = Queue(0)
    q.put(st_coord)
    while not q.empty():
        coord = q.get()
        update_dist_map(map,dist_map,coord.x,coord.y,coord.dist_from_st,q)
        
    for line in dist_map:
        print(line)
    highest_so_far = 0
    for line in dist_map:
        if max(line) > highest_so_far:
            highest_so_far = max(line)
    print("ANSWER ==",highest_so_far)

main()