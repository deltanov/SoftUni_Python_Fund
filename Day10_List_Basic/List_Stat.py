n=int(input())
positive_values=list()
negative_values=list()

for i in range(n):
    current_value=int(input())
    if current_value>=0 :
        positive_values.append(current_value)
    else:
        negative_values.append(current_value)
print(positive_values)
print(negative_values)
print(f"Count of positives: {len(positive_values)}. Sum of negatives: {sum(negative_values)}")

