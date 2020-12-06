
num1=int(input())
num2=int(input())
num3=int(input())

def find_smallest_from_3 (num1,nume2,num3):
    min_num = num1
    for i in range(num2,num3+1,1):
        if num2<min_num:
            min_num=num2
        elif num3<min_num:
            min_num=num3
    return min_num

print(find_smallest_from_3(num1,num2,num3))