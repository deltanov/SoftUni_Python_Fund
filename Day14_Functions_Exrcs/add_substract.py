def substract(num1,num2):
    res=num1-num2
    return res

def add (num1,num2):
    res=num1+num2
    return res

def add_substr(num1,num2,num3):

    add_res=add(num1,num2)
    res=substract(add_res,num3)
    return res


num1=int(input())
num2=int(input())
num3=int(input())
print(add_substr(num1,num2,num3))