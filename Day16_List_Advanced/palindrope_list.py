words=input().split()
searched_word=input()

palindromes=[word for word in words if word ==word[::-1]]

# for word in words:
#     if word == word[::1]:
#         palindromes.append(word)

print(palindromes)

occ= palindromes.count(searched_word)

print(f"Found palindrome {occ} times")

