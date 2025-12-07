import re

def parse_direction(direction: str) -> tuple[str, int]:
    pattern = r'([A-Za-z])(\d+)'
    matches = re.match(pattern, direction)
    if not matches:
        raise ValueError(f"Invalid direction format: {direction}")
    direction_letter = matches.group(1)
    amount = int(matches.group(2))
    return direction_letter, amount
    

def spin_dial(dial_position, direction, amount) -> int:
    # return the new position
    # preprocessing
    actual_turn_amount = amount % 100

    # spin left conditions
    if direction.lower() == 'l':
        current_dial_position = dial_position - actual_turn_amount
        if current_dial_position < 0:
            current_dial_position = 100 - abs(current_dial_position)
        return current_dial_position

    # spin right conditions
    if direction.lower() == 'r':
        current_dial_position = dial_position + actual_turn_amount
        return current_dial_position % 100
        
    return 0

def read_directions(path: str) -> list[tuple[str, int]]:
    directions = []
    with open(path, 'r') as file:
        for line in file:
            if line.strip(): 
                directions.append(line)
    return directions

def main():
    dial_position = 50
    count = 0
    directions = read_directions("file.txt")
    
    for line in directions:
        direction, amount = parse_direction(line)

        dial_position = spin_dial(dial_position, direction, amount)
        print(dial_position)
        if dial_position == 0:
            count += 1
    
    print(f"Times dial hit 0: {count}")


main()