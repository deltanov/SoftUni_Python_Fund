deck=input().split(":")

command=input()

while not command=="Ready":
    instructions=command.split()

    if instructions[0]=="Add":
        if instructions[1] not in deck:
            print("Card not found.")
        deck.append(instructions[1])

    if instructions[0]=="Insert":
        index_instr = int ( instructions[ 2 ] )
        if instructions[ 1 ] not in deck or index_instr>len(deck):
            print("Error!")
        if index_instr<len(deck):

            deck.insert(index_instr,instructions[1])

    if instructions[0]=="Remove":
        if instructions[ 1 ] not in deck:
            print ( "Card not found." )
        else:
            deck.remove(instructions[1])

    if instructions[ 0 ] == "Swap":
        a=deck.index(instructions[1])
        b =deck.index(instructions[2])
        deck[a],deck[b]=deck[b],deck[a]

    if instructions[ 0 ] == "Shuffle":

        deck.reverse()


    command=input()

print(" ".join(deck))
