number_of_wagons=input()
n_wagons=int(number_of_wagons)


train=[0 for i in range (n_wagons)] # this list comprehension builds a list consisting of 0 based on the length of the original list

command=input()

while command!='End':

    data=command.split()

    if data[0]=='add':
        number_of_people = int(data[1])
        train[-1] += number_of_people

    elif data[0]=='insert':

        index=int(data[1])
        number_of_people = int (data[2])
        train[index] += number_of_people


    elif data[0]=='leave':

        index = int ( data[ 1 ] )
        number_of_people = int ( data[ 2 ] )
        train[ index ] -= number_of_people

    command = input()

print(train)





