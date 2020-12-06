RANGE_HIGH = range(81,126) #with capital letters we indicate Constants in Python.

RANGE_MIDIUM= range(51,81)

RANGE_LOW= range(1,51)


effort=0
put_out_fire=list()

#reading and splitting thedata

fire_data_i=input()

fire_data=fire_data_i.split("#")

water_amount=int(input())

#split for each iteration again for type of fire and values:
for fire in fire_data:
    type_of_fire, value = fire.split(" = ") #tis is an example how we can list 2 variables on 1 row in python
    value = int(value)

#check if the value is not valid - based on interval - and continue

    if type_of_fire=='High' and not value in RANGE_HIGH:
        continue #if we hit continue - the program will bring us back to the first for cycle
    elif type_of_fire=='Medium' and not value in RANGE_MIDIUM:
        continue
    elif type_of_fire=='Low' and not value in RANGE_LOW:
        continue

    #TODO check if water is enough

    if water_amount >=value:
        water_amount -=value
        effort += value*0.25
        put_out_fire.append(value)

print("Cells:")
for fire_value in put_out_fire:
    print(f" - {fire_value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_fire)}")


