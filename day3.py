with open("day3input.txt", "r") as file:
    input_data = file.read()
input_data = input_data.splitlines()
height = len(input_data)
length = len(input_data[0])


def is_special(ch):
    return not ch.isdigit() and not ch == "."

def search(input_data,row,column):
    if row > 0:
        if is_special(input_data[row-1][column]):
            return True
    if row > 0 and column > 0:
        if is_special(input_data[row-1][column-1]):
            return True
    if column > 0:
        if is_special(input_data[row][column-1]):
            return True
    if row > 0 and column < length - 1:
        if is_special(input_data[row-1][column+1]):
            return True
    if column < length - 1:
        if is_special(input_data[row][column+1]):
            return True
    if row < height - 1 and column < length - 1:
        if is_special(input_data[row+1][column+1]):
            return True
    if row < height - 1:
        if is_special(input_data[row+1][column]):
            return True
    if row < height - 1 and column > 0:
        if is_special(input_data[row+1][column-1]):
            return True
        
    if column < length - 1:
        if input_data[row][column+1].isdigit():
            return search(input_data,row,column+1)
        
    return False

def get_num_from_left(input_data,row,column):
    num = int(input_data[row][column])
    column += 1
    while (column < length and input_data[row][column].isdigit()):
        num *= 10
        num += int(input_data[row][column])
        column+=1
    return num

def check_three(input_data,row,column):
    if input_data[row][column].isdigit() and input_data[row][column+2].isdigit() and not input_data[row][column+1].isdigit():
        return 2
    elif input_data[row][column].isdigit() or input_data[row][column+2].isdigit() or input_data[row][column+1].isdigit():
        return 1
    return 0

def get_num(input_data,i,j):
    if not input_data[i][j-1].isdigit():
        return get_num_from_left(input_data,i,j)
    return get_num(input_data,i,j-1)

def get_gear_ratios(input_data,i,j):
    temp = set()
    for c in range(3):
        if input_data[i-1][j-1+c].isdigit():
            temp.add(get_num(input_data,i-1,j-1+c))
    if input_data[i][j-1].isdigit():
        temp.add(get_num(input_data,i,j-1))
    if input_data[i][j+1].isdigit():
        temp.add(get_num(input_data,i,j+1))
    for c in range(3):
        if input_data[i+1][j-1+c].isdigit():
            temp.add(get_num(input_data,i+1,j-1+c))
    
    print(temp)
    
    if len(temp) == 1:
        for key in temp:
            return key * key
    
    ret = 1
    for key in temp:
        ret *= key
    return ret

def adj_check(input_data,row,column):
    count = 0

    if input_data[row][column-1].isdigit():
        count += 1

    if input_data[row][column+1].isdigit():
        count += 1

    count += check_three(input_data,row-1,column-1)
    count += check_three(input_data,row+1,column-1)
    return count == 2
    
    # gave up on edgecases
    # if row > 0 and column < length - 1:
    #     if input_data[row-1][column+1].isdigit():
    #         count += 1
    
    # if row < height - 1 and column < length - 1:
    #     if input_data[row+1][column+1].isdigit():
    #         count += 1
    # if row < height - 1:
    #     if input_data[row+1][column].isdigit():
    #         count += 1
    # if row < height - 1 and column > 0:
    #     if input_data[row+1][column-1].isdigit():
    #         count += 1
    # return count == 2

gear_ratios = 0
total_sum = 0
connected = False
print(input_data)
for i,line in enumerate(input_data):
    for j,ch in enumerate(line):
        if ch.isdigit() and not connected:
            connected = True
            num = get_num_from_left(input_data,i,j)
            if (search(input_data,i,j)):
                total_sum += num
        elif ch.isdigit() and connected:
            continue
        elif ch == "*":
            if adj_check(input_data,i,j):
                gear_ratios += get_gear_ratios(input_data,i,j)
        else:
            connected = False

print("\nTotal Sum:", total_sum)
print("Sum of Gear Ratios:", gear_ratios)

