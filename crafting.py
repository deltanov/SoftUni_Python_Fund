particles=input().split("|")
odd_i = []
even_i = []
command=input()
while not command=="Done":

    list_command=command.split()

    if len(list_command)==3:

        if list_command[1]=="Right":
            index_r = int ( list_command[ 2 ] )
            if (len(particles)-1)-index_r>0:
                particles[index_r],particles[index_r+1]=particles[index_r+1],particles[index_r]

        if list_command[1]=="Left":
            index_l = int ( list_command[ 2 ] )
            if index_l>0 and (len(particles)-1)-index_l>0:
                particles[index_l],particles[index_l-1]=particles[index_l-1],particles[index_l]

    if len(list_command)==2:
        if list_command[1]=="Even":
            for i in range (0,len(particles)):
                if i%2==0:
                    even_i.append(particles[i])
            print ( " ".join ( even_i ) )

    if len(list_command)==2:
        if list_command[1]=="Odd":
            for i in range (0,len(particles)):
                if not i%2==0:
                    odd_i.append(particles[i])
            print ( " ".join ( odd_i ) )
    command = input ()

weapon_name=("".join ( particles ))

print(f"You crafted {weapon_name}!")