received_gifts=input().split(" ")

commands=input().split(" ")

while commands[0]!="No":


    if commands[0]=="OutOfStock":
        for i in range(0,len(received_gifts)-1,1):
            if received_gifts[i] == commands[1]:
                received_gifts[i] = "None"

    elif commands[0]=="Required":
        if len(commands)>int(commands[2]):
            received_gifts[int(commands[2])] = commands[1]


    elif commands[0]=="JustInCase":
        received_gifts[-1] = commands[ 1 ]

    commands = input ().split ( " " )

for i in range(0,len(received_gifts)-1,1):
    if received_gifts[i]=='None':
        received_gifts.pop(i)

print(*received_gifts, sep=' ')
