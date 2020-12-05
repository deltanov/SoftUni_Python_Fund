
comapnions=int(input())
days=int(input())
coins=0
for n_day in range (1,days+1):

    if n_day%10==0:
        comapnions -=2
    if n_day%15==0:
        comapnions +=5

    coins +=50
    coins -=comapnions*2

    if n_day%3==0:
        coins -=comapnions*3

    if n_day%5==0:
        coins += comapnions*20
        if n_day % 3 == 0:
            coins -= comapnions * 2

conins_per_person = int(coins/comapnions)

print(f"{comapnions} companions received {conins_per_person} coins each.")