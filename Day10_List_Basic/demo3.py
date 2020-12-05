# some_text = "a b c d"
# my_list = some_text.split(" ")
# print(my_list)


# my_list = ["a", "b", "c"]
# print(";".join(my_list))


tail = input()
body = input()
head = input()

meerkat = [tail, body, head]
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
print(meerkat)
