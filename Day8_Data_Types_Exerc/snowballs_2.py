import sys

n = int(input())

total_balls = 0

max_ball = -sys.maxsize

max_snow = 0

max_time = 0

max_quality = 0

while n > total_balls:

    total_balls += 1

    ball_snow = int(input())

    ball_time = int(input())

    ball_quality = int(input())

    ball_v = (ball_snow / ball_time)

    ball_value = pow(ball_v, ball_quality)  # (** ) ball_value = (ball_snow / ball_time) ** ball_quality

    if ball_value > max_ball:
        max_ball = ball_value

        max_snow = ball_snow

        max_time = ball_time

        max_quality = ball_quality

print(f"{max_snow} : {max_time} = {round(max_ball)} ({max_quality})")