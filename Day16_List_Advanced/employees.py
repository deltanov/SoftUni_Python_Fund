employees=list(map(int, input().split(" ")))
happiness_factor=int(input())

#palindromes=[word for word in words if word ==word[::-1]]
increased_happines=[element*happiness_factor for element in employees]
avg_happines=sum(increased_happines) / len(increased_happines)

count = 0
for i in increased_happines:
    if i >= avg_happines:
        count = count + 1
# print(employees)
# print(increased_happines)
# print(avg_happines)

if count>=len(increased_happines)/2:
    print(f"Score: {count}/{len(increased_happines)}. Employees are happy!")
else:
    print ( f"Score: {count}/{len(increased_happines)}. Employees are not happy!" )