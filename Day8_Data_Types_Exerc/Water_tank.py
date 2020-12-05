# •	On the first line, you will receive n – the number of lines, which will follow
# •	On the next n lines – you receive quantities of water, which you have to pour in the tank

n_lines=int(input())
total_liters=0


for n in range (0,n_lines):
    liter = int(input())
    total_liters += liter
    if total_liters > 255:
        print(f"Insufficient capacity!")
        total_liters -= liter
    continue
print(255-liter)