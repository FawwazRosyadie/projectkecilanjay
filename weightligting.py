import math

BAR = 20.0
plates = {1.25, 2.5, 5, 10, 15, 20}

# This funtion calculates the load percentage of an exercise relative to a PR
def calculate_load_percentage(pr, load):
    if pr == 0 or pr <= 0:
        return "Error: Your PR cannot be zero or negative."
    elif pr is None:
        exit()
    load_percentage = load / pr * 100.0
    
    return load_percentage

# This funtion calculates the total of snatch and clean & jerk
def calculate_total(sn, cj) -> float:
    
    if sn <= 0 or cj <= 0:
        return "Error: Your lift cannot be negative"
    
    return (sn + cj)

# This funtion calculates the sinclair total
def calculate_sinclair(body_weight, b=193.609, A=0.722762521):
    if body_weight <= calculate_total():
        X = math.log10(body_weight / b)
        SC = 10 ** (A * (X ** 2))
    else:
        SC = 1
    return SC

# This funtion informs the user what plates should be used for the lift
def plate_load(load, BAR):
    if load < BAR:
        return "Target weight must be greater than the bar weight."
    
    # Calculate the weight to be added on each side of the bar
    remaining_weight = (load - BAR) / 2
    
    # Sort plate options in descending order
    plate_options = sorted(plates, reverse=True)
    
    # Determine plates for one side
    plates_needed = {}
    for plate in plate_options:
        count = int(remaining_weight // plate)
        if count > 0:
            plates_needed[plate] = count
            remaining_weight -= count * plate
    
    return plates_needed

def print_plates(plates):
    for weight, count in plates.items():
        print(f"{weight} kg x {count * 2}")
    
