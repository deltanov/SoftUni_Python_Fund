num1=int(input())
num2=int(input())
result=None

def calc_facturiel(n):
    res=1 # we start with 1 because in factoriel strting with 0 will always retunr 0
    for num in range(2,n+1):
        res *=num

    return res

if num1==0 and num2!=0:
    result=0
elif num1!=0 and num2!=0:
    factorial_number_1=calc_facturiel(num1)
    factorial_number_2=calc_facturiel(num2)
    result = factorial_number_1/factorial_number_2
elif num1 !=0 and num2==0:
    result=None
print(f"{result:0.2f}")
