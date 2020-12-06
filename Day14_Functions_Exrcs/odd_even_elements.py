
number = input ()
digits = len ( number )


def sum_of_all_even_and_all_odd_digits(digit):
    odd_sum = 0
    even_sum = 0
    #res = list ( map ( int , str ( digit ) ) )
    res = [ int ( x ) for x in str ( digit ) ]
    for element in res:
        if element % 2 != 0:
            odd_sum += element
        else:
            even_sum += element

    print ( f'Odd sum = {odd_sum},' , end=' ' )
    print ( f'Even sum = {even_sum}' )


sum_of_all_even_and_all_odd_digits ( number )
