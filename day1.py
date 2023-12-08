MAPPINGS = {
    "one" : "o1e",
    "two" : "t2o",
    "three" : "t3e",
    "four" : "f4r",
    "five" : "f5e",
    "six" : "s6x",
    "seven" : "s7n",
    "eight" : "e8t",
    "nine" : "n9e"
}

def decrypt(data):
    for i in range(len(data)):
        for key,value in MAPPINGS.items():
            data[i] = data[i].replace(key,value)

with open("day1input.txt", "r") as file:
    input_data = file.read()
input_data = input_data.splitlines()
input_len = len(input_data)
res =[]

decrypt(input_data)
for line in input_data:
    first_digit = None
    last_digit = None
    for char in line:
        if char.isdigit():
            if (first_digit == None):
                first_digit = int(char)
                last_digit = int(char)
            else :
                last_digit = int(char)
    res.append(first_digit * 10 + last_digit)

print(sum(res))