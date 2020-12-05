# •	On the first line, you will receive n – the number of lines, which will follow
# •	On the next n lines – you will receive letters from the Latin alphabet

number_of_lines=int(input())
total_sum=0
for n in range (0,number_of_lines):
    char=input()
    total_sum+=ord(char)
print(f"The sum equals: {total_sum}")