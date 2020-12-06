# command=input()
#
# while command!='end':
#     command=input()

train_length = int(input())
train = [0] * train_length
command = input()

while command != "end":
    data = command().split (" ")

    if data[0]=='add':
        number_of_people = int(data[1])
        train[-1] += number_of_people
    elif data == 'insert':
        index = int ( data[ 1 ] )
        number_of_people = int ( data[ 2 ] )
        train[ -1 ] += number_of_people
    elif data=='leave':
        index = int ( data[ 1 ] )
        number_of_people = int ( data[ 2 ] )
        train[ index ] -= number_of_people
    command = input()

print(train)
