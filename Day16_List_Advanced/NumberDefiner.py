number_test=float(input())

if number_test==0:
    print("zero")

elif number_test>0:
    if number_test<1:
        print("small positive")
    elif number_test> 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if abs(number_test)<1:
        print("small negative")

    elif number_test > 1000000:
        print("large negative")
    else:
        print("negative")

