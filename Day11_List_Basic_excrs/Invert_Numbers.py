input_string=input()

list_input=input_string.split(" ")

for i in range(0, len(list_input)):
    list_input[i] = int(list_input[i])

for i in range(0, len(list_input)):
    list_input[i] = list_input[i]*(-1)

print(list_input)