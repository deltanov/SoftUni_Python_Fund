n=int(input())
text=input()
full_list=list()
selected_list=[]

for i in range(n):
    current_text=input()
    full_list.append(current_text)
    if text in current_text:
        selected_list.append(current_text)




print(full_list)
print(selected_list)