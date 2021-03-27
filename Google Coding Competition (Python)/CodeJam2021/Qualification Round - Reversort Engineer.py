T = int(input())
def reversing(list, start, end):
    while start<end:
        list[start], list[end] = list[end], list[start]
        start+=1
        end-=1
def createArray(N, C):
    if C<N-1 or N*(N+1)/2-1<C:
        return 'IMPOSSIBLE'
    arr = [str(a) for a in range(1, N+1)]
    for i in range(N-2, -1, -1):
        if C==i+1:
            return " ".join(arr)
        if C>=len(arr):
            C-=len(arr)-i
            reversing(arr, i, len(arr)-1)
        else:
            reversing(arr, i, i+(C-i)-1)
            return " ".join(arr)
    return " ".join(arr)

for t in range(T):
    temp = input().split()
    N = int(temp[0])
    C = int(temp[1])
    st = createArray(N,C)
    print("Case #"+ str(t+1)+": "+st)


