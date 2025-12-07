import re


def parse_instruction(s: str) -> tuple[str, int]:
    match = re.match(r"([A-Za-z]+)(\d+)", s)
    if match:
        direction = match.group(1)
        number = int(match.group(2))
    return direction, number


def spin(dial_num, dir, num):
    dir = dir.capitalize()
    if dir == "L":
        # spin left = subtract
        # make sure if it goes over check over by how much and subtract accordingly
        # if num > dial_num:
        #     excess_amount = abs(dial_num - num)
        #     return 100 - excess_amount
        # return dial_num - num
        subtract_num = num % 100
    else:
        # spin right = add
        if num + dial_num == 100:
            return 0
        elif num + dial_num > 100:
            excess_amount = num + dial_num
            return excess_amount - 100
        return dial_num + num



def main():
    list_instructions = "L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"
    dial_num = 50
    count = 0

    with open("file.txt", "r") as f:
        for line in f:
            direction, num = parse_instruction(line.strip())
            dial_num = spin(dial_num, direction, num)
            if dial_num == 0:
                count += 1
            print(dial_num)
    
    
    # for instruction in list_instructions:
    #     direction, num = parse_instruction(instruction)
    #     dial_num = spin(dial_num, direction, num)
    #     if dial_num == 0:
    #         count += 1
    #     print(dial_num)
    

main()