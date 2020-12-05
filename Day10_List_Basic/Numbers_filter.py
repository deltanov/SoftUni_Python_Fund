n=int(input())
even_num=[]
odd_num=[]
positive_num=[]
negative_num=[]


for i in range(n):
    current_number=int(input())
    if current_number>=0:
        positive_num.append(current_number)
    if current_number<0:
        negative_num.append(current_number)
    if current_number%2==0:
        even_num.append(current_number)
    if current_number%2 !=0:
        odd_num.append(current_number)

command=input()

if command == "even":
    print(even_num)
elif command=="odd":
    print(odd_num)
elif command=="positive":
    print(positive_num)
elif command=="negative":
    print(negative_num)



