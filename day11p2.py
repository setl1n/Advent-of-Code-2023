import time

def get_sum(first_pt,second_pt,blank_rows,blank_cols):
    smaller_x = min(first_pt[0],second_pt[0])
    larger_x = max(first_pt[0],second_pt[0])
    
    smaller_y = min(first_pt[1],second_pt[1])
    larger_y = max(first_pt[1],second_pt[1])
    count = 0
    while smaller_x < larger_x:
        if blank_cols[smaller_x + 1]:
            count += 1000000
            smaller_x +=1
        else:
            count +=1
            smaller_x +=1

    while smaller_y < larger_y:
        if blank_rows[smaller_y + 1]:
            count += 1000000
            smaller_y +=1
        else:
            count +=1
            smaller_y +=1

    return count

def get_sums(gal_coords,blank_rows,blank_cols):
    sum = 0
    for i,coord in enumerate(gal_coords):
        counter = 0
        while i + counter < len(gal_coords):
            sum += get_sum(coord,gal_coords[i+counter],blank_rows,blank_cols)
            counter+=1
    return sum

def main():
    with open("./day11input.txt", "r") as file:
        input_data = file.read()
    input_data = input_data.splitlines()
    num_of_cols = len(input_data[0])
    num_of_rows = len(input_data)
    blank_cols = [True] * num_of_cols
    blank_rows = [True] * num_of_rows
    for i,row in enumerate(input_data):
        for j,col in enumerate(row):
            if col == "#":
                blank_cols[j] = False
                blank_rows[i] = False
    
    gal_coords = []
    for i,row in enumerate(input_data):
        for j,col in enumerate(row):
            if col == '#':
                gal_coords.append([j,i])
    
    sum_of_dists = get_sums(gal_coords,blank_rows,blank_cols)
    print("ANSWER ==", sum_of_dists)
    
st_time = time.time()
main()
print(f"-------Time Taken: {time.time() - st_time}--------")