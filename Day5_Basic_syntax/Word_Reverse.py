word=input()
reverserd_word=""

print (len(word))
for i in range (len(word)-1,-1,-1):
    reverserd_word+=word[i]

print (reverserd_word)