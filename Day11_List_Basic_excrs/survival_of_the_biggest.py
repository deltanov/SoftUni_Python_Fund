#split by space and convert into int
# based on the output examples it looks like we should not alternate the order in the original string
# I am using beside the original string/list, one list for ordering in DESC and removing the n numbers at the end
# and one list for keeping what was removed in order to match it against the origonal and remove it from there
#order the list descending list.sort -> list.reverse and remove the smallest with for using pop

list_of_numbers=input().split(" ")
n=int(input())

order_list_of_numbers=list() # ordering in DESC and removing the n numbers at the en
to_remove=list() #keeping what was removed in order to match it against the original

for i in range(0, len(list_of_numbers)):
    list_of_numbers[i] = int(list_of_numbers[i])



order_list_of_numbers=list_of_numbers.copy()

order_list_of_numbers.sort(reverse=True)



if n==0:
    print ( list_of_numbers )
else:
    for i in range(len(order_list_of_numbers)-1, len(order_list_of_numbers)-1- n, -1): #how to reference index backwards in python

        to_remove.append(order_list_of_numbers[i])
        order_list_of_numbers.pop(i)

    #udpated_list=list(set(list_of_numbers)-set(to_remove))
    #difference between two lists python
    udpated_list = [ ]
    for item in list_of_numbers:
        if item not in to_remove:
            udpated_list.append(item)



    print(udpated_list)


