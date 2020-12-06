def repeat_string(text,num_rep):
    result=""
    for i in range (0,num_rep,1):
        result += text
    return result


input_string=input()
n_rep=int(input())

print(repeat_string(input_string,n_rep))
