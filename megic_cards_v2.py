deck=input().split(":")
deck1=list()
command=input()

while not command=="Ready":
    instructions=command.split()

    if instructions[0]=="Add":
        if instructions[1] not in deck:
            print("Card not found.")

        else:

            deck1.append(instructions[1])

    if instructions[0]=="Insert":
        index_instr = int ( instructions[ 2 ] )
        if instructions[ 1 ] not in deck or index_instr>len(deck):
            print("Error!")
        else:

            #deck1[index_instr]=instructions[1]

            deck1.insert(index_instr,instructions[1])

    if instructions[0]=="Remove":
        if instructions[ 1 ] not in deck1:
            print ( "Card not found." )
        else:
            deck1.remove(instructions[1])

    if instructions[ 0 ] == "Swap":
        a=deck1.index(instructions[1])
        b =deck1.index(instructions[2])
        deck1[a],deck1[b]=deck1[b],deck1[a]

    if instructions[ 0 ] == "Shuffle":

        deck1.reverse()


    command=input()

print(" ".join(deck1))
