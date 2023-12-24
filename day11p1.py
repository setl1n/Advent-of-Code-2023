import time

# Expand galaxies
# Find coords of each galaxy
# Sum distances

def expand_blanks(input_data):
    num_of_cols = len(input_data[0])
    num_of_rows = len(input_data)
    blank_cols = [True] * num_of_cols
    blank_rows = [True] * num_of_rows
    for i,row in enumerate(input_data):
        for j,col in enumerate(row):
            if col == "#":
                blank_cols[j] = False
                blank_rows[i] = False
    expanded_map = ['']* num_of_rows
    for i,row in enumerate(input_data):
        for j,col in enumerate(row):
            if col == '#':
                expanded_map[i] += '#'
            elif blank_cols[j]:
                expanded_map[i] += '..'
            else:
                expanded_map[i] += '.'
    buffer = 0
    for i,blank_row in enumerate(blank_rows):
        if blank_row:
            expanded_map.insert(buffer + i,'.' * len(expanded_map[0]))
            buffer += 1
    return expanded_map

def get_sum(first_pt,second_pt):
    return abs(second_pt[1] - first_pt[1]) + abs(second_pt[0] - first_pt[0])

def get_sums(map):
    gal_coords = []
    for i,row in enumerate(map):
        for j,col in enumerate(row):
            if col == '#':
                gal_coords.append([j,i])
    sum = 0
    for i,coord in enumerate(gal_coords):
        counter = 0
        while i + counter < len(gal_coords):
            sum += get_sum(coord,gal_coords[i+counter])
            counter+=1
    return sum

def main():
    with open("./day11input.txt", "r") as file:
        input_data = file.read()
    input = input_data.splitlines()
    expanded_map = expand_blanks(input)
    sum_of_dists = get_sums(expanded_map)
    print("ANSWER ==", sum_of_dists)
    
st_time = time.time()
main()
print(f"-------Time Taken: {time.time() - st_time}--------")