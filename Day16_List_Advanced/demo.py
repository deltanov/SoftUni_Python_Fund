
data=input().split()
numbers =[int(el) for el in data]

#print(id(data)) - gives address of the data

#bez list comprehension or without copy() - the new list will point to the original place in the memory! In this case by changing the elements in A, we will change B as well
# this is different for the vallues - they are not refferened type of variables


a = lambda x: print(x) # anonimnost na function