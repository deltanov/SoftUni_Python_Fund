# •	On the first line you will receive the needed experience amount –  a real number in the range [0.0….400000.0]
# •	On the second line you will receive the count of battles – an integer number in the range
# [0….500]
# •	On the next lines you will receive the experience earned per battle – a real number in the range
# [0.0….5000.0]


amount_of_experience=float(input())
count_of_battles=int(input())
experience_total=0
battle_Count=0

while count_of_battles>0:
    battle_Count+=1
    experience_earned_per_battle=float(input())
    experience_total+=experience_earned_per_battle

    if experience_total>=amount_of_experience:
        break



    if count_of_battles%3==0:
        experience_total=experience_total*1.15
    if count_of_battles%5==0:
        experience_total=experience_total*0.9
    if count_of_battles%15==0:
        experience_total=experience_total*1.05

    count_of_battles-=1


if experience_total>amount_of_experience:
    print(f"Player successfully collected his needed experience for {battle_Count} battles.")
else:
    needed_experience=amount_of_experience-float(experience_total)
    print(f"Player was not able to collect the needed experience, {neededExperience:.2f} more needed.")

