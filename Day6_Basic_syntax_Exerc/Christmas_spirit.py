# The input will consist of exactly 2 lines:
# •	quantity – integer in range [1…100]
# •	days – integer in range [1…100]

quantity=int(input())
days=int(input())
total_money=0
spirit=0

# There are 4 types of decorations and each piece costs a price
# •	Ornament Set – 2$ a piece
# •	Tree Skirt – 5$ a piece
# •	Tree Garlands – 3$ a piece
# •	Tree Lights – 15$ a piece

for day in range (1,days+1):
    if day%11==0:
        quantity +=2
    if day%2==0:
        total_money +=quantity*2
        spirit +=5
    if day%3==0:
        total_money += (quantity*5 + quantity*3)
        spirit += 13
    if day%5==0:
        total_money += quantity*15
        spirit +=17
        if day%3==0:
            spirit +=30
    if day%10==0:
        spirit -=20
        total_money += 5+3+15
        if day==days:
            spirit -=30

# •	"Total cost: {budget}"
# •	"Total spirit: {totalSpirit}"

print(f"Total cost: {total_money}")
print(f"Total spirit: {spirit}")



