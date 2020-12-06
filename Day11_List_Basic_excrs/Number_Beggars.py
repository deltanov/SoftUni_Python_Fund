beggars = input().split(", ")
n = int(input())
beggars = list(map(int , beggars))
s_all = []
for j in range(0 ,n):
      sj = []
      for i in range(0 + j,len(beggars) , n):
            sj.append(beggars[i])
      sum_j = sum(sj)
      s_all.append(sum_j)
print(s_all)

# we should make another list with the number of beggers and sum in each position.