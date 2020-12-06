def custom_split(text, sep):
    result=text.split(sep)
    return result

# a="Hello, there"
# b="Hello;there"
#
# result_a=a.split(",")
# result_b=b.split(";")
#
# print(result_a)
# print(result_b)

print(custom_split("hello, there", ","))

print(3*'a')

total_price=5.3245
print(f"{total_price:.2f}")