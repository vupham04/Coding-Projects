T = int(input())
def reversing(list, start, end):
    while start<end:
        list[start], list[end] = list[end], list[start]
        start+=1
        end-=1
for t in range(T):
    n = input()
    l = input().split()
    cost = 0
    for i in range(len(l)- 1):
        j = i
        for g in range(i, len(l)):
            if int(l[g])<int(l[j]):
                j = g
        reversing(l, i, j)
        cost += j-i+1
    print("Case #"+str(t+1)+ ": "+ str(cost))

