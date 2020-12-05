

# print(list(range(1,6)))
#
# result = list(range(1,6))
# print (result)

# word="Hello"
#
# print (list(word))

# nums=[1,2,3,3,5]
# print(nums.count(3))

 #
 # num=156
 #
 # pri
# nt(list(str(num)))text="Hello

#obhojdane na text
# text="Hello"
# for char in text:
#     print(char)
#
# nums=[1,2,3,4]
#
# #obhojdane na list:
# for num in nums:
#     print(num)
#
# #hodene prez indexi na list:
# for index in range(0,len(nums)):
#     print(num)
#
# for index in range(0,len(nums)):
#     print(nums[index])
#     #nums[index]=1 - taka promeniame index
#
#
# for index in range(0,len(nums)):
#     print(f"{nums[index]},", end='')
#
#
# #unpacking - oznachava da vzeme kolektzia i da izpechata vsichki
# print(*nums)

data = [1, 12.5, False, "Hellp", 2 ]

list_only_integ = []

for index in range(0, len ( data ) ):

    if isinstance(index, int) and not isinstance ( index , bool ):
        list_only_integ.append(index)

list_only_integ.pop ( 0 )
print(list_only_integ )

#print(isinstance(5,int))

