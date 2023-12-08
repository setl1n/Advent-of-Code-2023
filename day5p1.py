import re

def get_mappings(input_data):
    pattern = re.compile(r"seed-to-soil map:\n(.*?)\n\n", re.DOTALL)
    seed_to_soil = pattern.findall(input_data)[0].split('\n')
    seed_to_soil = [matching.split() for matching in seed_to_soil]
    seed_to_soil = [[int(i) for i in matching] for matching in seed_to_soil]

    

    pattern = re.compile(r"soil-to-fertilizer map:\n(.*?)\n\n", re.DOTALL)
    soil_to_fertilizer = pattern.findall(input_data)[0].split('\n')
    soil_to_fertilizer = [matching.split() for matching in soil_to_fertilizer]
    soil_to_fertilizer = [[int(i) for i in matching] for matching in soil_to_fertilizer]

    pattern = re.compile(r"fertilizer-to-water map:\n(.*?)\n\n", re.DOTALL)
    fertilizer_to_water = pattern.findall(input_data)[0].split('\n')
    fertilizer_to_water = [matching.split() for matching in fertilizer_to_water]
    fertilizer_to_water = [[int(i) for i in matching] for matching in fertilizer_to_water]

    pattern = re.compile(r"water-to-light map:\n(.*?)\n\n", re.DOTALL)
    water_to_light = pattern.findall(input_data)[0].split('\n')
    water_to_light = [matching.split() for matching in water_to_light]
    water_to_light = [[int(i) for i in matching] for matching in water_to_light]

    pattern = re.compile(r"light-to-temperature map:\n(.*?)\n\n", re.DOTALL)
    light_to_temperature = pattern.findall(input_data)[0].split('\n')
    light_to_temperature = [matching.split() for matching in light_to_temperature]
    light_to_temperature = [[int(i) for i in matching] for matching in light_to_temperature]

    pattern = re.compile(r"temperature-to-humidity map:\n(.*?)\n\n", re.DOTALL)
    temperature_to_humidity = pattern.findall(input_data)[0].split('\n')
    temperature_to_humidity = [matching.split() for matching in temperature_to_humidity]
    temperature_to_humidity = [[int(i) for i in matching] for matching in temperature_to_humidity]

    pattern = re.compile(r"humidity-to-location map:\n(.*?)\n\n", re.DOTALL)
    humidity_to_location = pattern.findall(input_data)[0].split('\n')
    humidity_to_location = [matching.split() for matching in humidity_to_location]
    humidity_to_location = [[int(i) for i in matching] for matching in humidity_to_location]


    return [seed_to_soil, soil_to_fertilizer,fertilizer_to_water,water_to_light,light_to_temperature,temperature_to_humidity,humidity_to_location]

def get_seeds(input_data):
    seeds = re.findall(r'seeds: (.*)\n',input_data)[0].split()
    return [int(seed) for seed in seeds]

def get_next_loc(curr_val,mapping):
    for data in mapping:
        print(curr_val,data)
        if data[1] <= curr_val and data[1] + data[2] > curr_val:
            return  data[0] + curr_val - data[1]
    return curr_val
        

def get_location(seed,list_of_mappings):
    for mapping in list_of_mappings:
        seed = get_next_loc(seed,mapping)
    return seed

def main(input_data):
    seeds = get_seeds(input_data)
    list_of_mappings = get_mappings(input_data)
    min_loc = get_location(seeds[3],list_of_mappings)
    for seed in seeds:
        min_loc = min(min_loc,get_location(seed,list_of_mappings))
    print("min location:",min_loc)

    

with open("day5input.txt", "r") as file:
    input_data = file.read()

main(input_data)