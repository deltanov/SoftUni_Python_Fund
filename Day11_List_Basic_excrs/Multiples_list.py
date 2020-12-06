factor=int(input())
count=int(input())
multiples=0
list_numbers=list()

for i in range (0,count):
    multiples+=factor
    list_numbers.append(multiples)


print(list_numbers)