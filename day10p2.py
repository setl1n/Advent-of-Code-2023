import re
import sys
sys.setrecursionlimit(100000)

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

def get_st_piece(map,x_coord,y_coord):
    up_valid = False
    down_valid = False
    left_valid = False
    right_valid = False
    no_of_valid = 0
    
    if x_coord >= 0 and check_valid(map, x_coord - 1, y_coord,'L'):
        no_of_valid += 1
        left_valid = True
    if y_coord >= 0 and check_valid(map, x_coord,y_coord - 1, 'U'):
        no_of_valid += 1
        up_valid = True
    if x_coord < len(map[y_coord]) - 1 and check_valid(map, x_coord + 1,y_coord, 'R'):
        no_of_valid += 1
        right_valid = True
    if y_coord < len(map) - 1 and check_valid(map, x_coord,y_coord + 1, 'D'):
        no_of_valid += 1
        down_valid = True
    
    if not no_of_valid == 2:
        print("ERROR: More than 2 valid pieces beside start")
        return
    
    if left_valid and right_valid:
        return '-'
    elif left_valid and up_valid:
        return 'J'
    elif left_valid and down_valid:
        return '7'
    elif right_valid and up_valid:
        return 'L'
    elif up_valid and down_valid:
        return '|'
    elif right_valid and down_valid:
        return 'F'
    else:
        print("Error, unable to find valid starting piece")
        return

def get_st_dir(piece):
    if piece in "|JL":
        return 'U'
    elif piece in "-7":
        return 'L'
    elif piece == 'F':
        return 'R'

def draw_loop(map,main_loop_map,x_coord,y_coord,prev_dir):
    curr_piece = map[y_coord][x_coord]
    if main_loop_map[y_coord][x_coord] == 1:
        return
    main_loop_map[y_coord][x_coord] = 1
    # | - L J 7 F
    # Recursive call to next one
    if prev_dir == 'U':
        if curr_piece == '|':
            draw_loop(map,main_loop_map,x_coord,y_coord + 1,'U')
        elif curr_piece == 'L':
            draw_loop(map,main_loop_map,x_coord + 1,y_coord,'L')
        elif curr_piece == 'J':
            draw_loop(map,main_loop_map,x_coord - 1,y_coord,'R')
    elif prev_dir == 'R':
        if curr_piece == '-':
            draw_loop(map,main_loop_map,x_coord - 1,y_coord,'R')
        elif curr_piece == 'F':
            draw_loop(map,main_loop_map,x_coord,y_coord + 1,'U')
        elif curr_piece == 'L':
            draw_loop(map,main_loop_map,x_coord,y_coord - 1,'D')
    elif prev_dir == 'D':
        if curr_piece == '|':
            draw_loop(map,main_loop_map,x_coord,y_coord - 1,'D')
        elif curr_piece == '7':
            draw_loop(map,main_loop_map,x_coord - 1,y_coord,'R')
        elif curr_piece == 'F':
            draw_loop(map,main_loop_map,x_coord + 1,y_coord,'L')
    elif prev_dir == 'L':
        if curr_piece == '-':
            draw_loop(map,main_loop_map,x_coord + 1,y_coord,'L')
        elif curr_piece == 'J':
            draw_loop(map,main_loop_map,x_coord,y_coord - 1,'D')
        elif curr_piece == '7':
            draw_loop(map,main_loop_map,x_coord,y_coord + 1,'U')
 

def main():
    with open("./day10input.txt","r") as file:
        map = file.read()
    
    map = map.splitlines()
    st_x,st_y = get_st_idx(map)
    main_loop_map = [
        [0] * len(line) for line in map
    ]
    st_piece = get_st_piece(map,st_x,st_y)
    st_dir = get_st_dir(st_piece)
    map[st_y] = map[st_y].replace('S',st_piece)
    draw_loop(map,main_loop_map,st_x,st_y,st_dir)
    
    count = 0
    for y,row in enumerate(main_loop_map):
        row = main_loop_map[y]
        is_inside = False
        for x,pos in enumerate(row):
            if pos == 1:
                if map[y][x] in "|F7": #if s L J or |
                    is_inside = not is_inside
            elif pos == 0 and is_inside:
                count += 1
                
        
    print("ANSWER ==",count)

main()