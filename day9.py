def get_extrapolated_data(data_set):
    if all(x == 0 for x in data_set):
        return 0
    next_data_set = []
    for i,data in enumerate(data_set):
        if i == len(data_set) - 1:
            continue
        next_data_set.append(data_set[i+1] - data_set[i])
    return next_data_set[-1] + get_extrapolated_data(next_data_set)

def main():
    with open("./day9input.txt","r") as file:
        input_data = file.read()
    input_data = input_data.splitlines()
    sum1 = 0
    sum2 = 0
    for line in input_data:
        data_set = [int(data) for data in line.split()]
        sum1 += data_set[-1] + get_extrapolated_data(data_set)
        sum2 += data_set[0] + get_extrapolated_data(data_set[::-1])
    print("\nANSWER1 ==",sum1)
    print("ANSWER2 ==",sum2)

main()