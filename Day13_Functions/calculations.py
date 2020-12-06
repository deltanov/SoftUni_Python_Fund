input_operator=input()
first_number=int(input())
second_number=int(input())

def claculator(a,b,operator):
    result=None

    if b==0:
        result='Error'

    elif operator=='multiply':
        result=a*b
    elif operator=='divide':
        result=a/b
    elif operator=='add':
        result=a+b
    elif operator=='subtract':
        result=a-b
    return result

print(int(claculator(first_number,second_number,input_operator)))
