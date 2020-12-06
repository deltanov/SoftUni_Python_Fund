note=input()

to_do_list=[0 for i in range(10)]


while not note=="End":

    data=note.split('-')
    importance = int(data[0])
    task = data[1]
    to_do_list.insert(importance,task)


    note=input()

while 0 in to_do_list:
    to_do_list.remove(0)

print(to_do_list)

# result=[]
#
# for element in to_do_list:
#     if element!=0:
#         result.append(element)
# print(result)