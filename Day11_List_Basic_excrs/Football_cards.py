cards = input ().split ()
set_1 = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11}
set_2 = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11}

team_a_counter = 11
team_b_counter = 11
is_terminated = False

for card in cards:
    tokens = card.split ( "-" )
    team = tokens[ 0 ]
    number = int ( tokens[ 1 ] )

    if team == "A":
        if number in set_1:
            set_1.remove ( number )
            team_a_counter -= 1
    else:
        if number in set_2:
            set_2.remove ( number )
            team_b_counter -= 1
    if team_b_counter < 7 or team_a_counter < 7:
        is_terminated = True
        break

print ( f"Team A - {team_a_counter}; Team B - {team_b_counter}" )
if is_terminated:
    print ( f"Game was terminated" )