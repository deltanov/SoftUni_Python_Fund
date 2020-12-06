
#a='123'
#print(a[::-1]) #prints in reverse list

def is_palindrome (element):
    reversed_element=element[::-1]
    if element==reversed_element:
        return True
    return False

def separate_element(text, sep):
    numbers_as_strings=text.split(sep)
    return numbers_as_strings


data=input()

nums_strings=separate_element(data,", ")

for el in nums_strings:
    print(is_palindrome(el))