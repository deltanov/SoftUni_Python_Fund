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

    if battle_Count%3==0:
        #experience_earned_per_battle=experience_earned_per_battle*1.15
        experience_earned_per_battle = experience_earned_per_battle + (experience_earned_per_battle* 15/100)

    if battle_Count%5==0:
        #experience_earned_per_battle=experience_earned_per_battle*0.9
        experience_earned_per_battle = experience_earned_per_battle - (experience_earned_per_battle * 10 / 100)
    if battle_Count%15==0:
        #experience_earned_per_battle=experience_earned_per_battle*1.05
        experience_earned_per_battle = experience_earned_per_battle + (experience_earned_per_battle * 5 / 100)
    experience_total+=experience_earned_per_battle

    if experience_total>=amount_of_experience:
        break


    count_of_battles-=1


if experience_total>amount_of_experience:
    print(f"Player successfully collected his needed experience for {battle_Count} battles.")
else:
    needed_experience=amount_of_experience-float(experience_total)
    print(f"Player was not able to collect the needed experience, {needed_experience:.2f} more needed.")


