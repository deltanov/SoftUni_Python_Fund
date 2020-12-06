# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00

def calculate_order(item,quantity):
    total_amount=""
    if item=="coffee":
        total_amount=quantity*1.5
    elif item=="coke":
        total_amount=quantity*1.4
    elif item=="water":
        total_amount=quantity*1
    elif item=="snacks":
        total_amount=quantity*2.0
    return total_amount

product=input()
quantity=int(input())
total_price=calculate_order(product,quantity)

print(f"{total_price:.2f}")

