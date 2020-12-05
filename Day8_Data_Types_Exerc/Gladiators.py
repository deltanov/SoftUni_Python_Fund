# •	On the first line you will receive the lost fights count – integer in the range [0, 1000].
# •	On the second line you will receive the helmet price - floating point number in range [0, 1000].
# •	On the third line you will receive the sword price - floating point number in range [0, 1000].
# •	On the fourth line you will receive the shield price - floating point number in range [0, 1000].
# •	On the fifth line you will receive the armor price - floating point number in range [0, 1000].

lost_fights=int(input())
price_helmet=float(input())
price_sword=float(input())
price_schield=float(input())
price_armor=float(input())

sum_for_repairs=0

counter_shield_brakes = 0

for n_fight in range (1,lost_fights+1):
    if n_fight%2==0:
        sum_for_repairs +=price_helmet

    if n_fight%3==0:
        sum_for_repairs += price_sword

    if n_fight%2==0 and n_fight%3==0:
        sum_for_repairs +=price_schield
        counter_shield_brakes +=1

        if counter_shield_brakes>0 and counter_shield_brakes%2==0:
            sum_for_repairs += price_armor


print(f"Gladiator expenses: {sum_for_repairs:.2f} aureus")

