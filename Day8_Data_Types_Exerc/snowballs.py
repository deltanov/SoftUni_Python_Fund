from collections import defaultdict


def snowball_value(data_tuple: tuple):
    snowball_snow = data_tuple[0]
    snowball_time = data_tuple[1]
    snowball_quality = data_tuple[2]
    return int((snowball_snow / snowball_time) ** snowball_quality)


number_snowballs = int(input())
snowballs = defaultdict()

for _ in range(number_snowballs):
    data = (int(input()), int(input()), int(input()))
    snowballs[snowball_value(data)] = data

highest_snowball_value = max(snowballs.keys())
ball = snowballs[highest_snowball_value]

print(f"{ball[0]} : {ball[1]} = {highest_snowball_value} ({ball[2]})")