T = int(input())

for t in range(T):
    li = input().split()
    X = int(li[0])
    Y = int(li[1])
    st = list(li[2])
    cost = 0
    lastChar = ''
    for i in range(len(st)-1):
        if st[i]=='C' and st[i+1]=='J':
            cost+=X
        if st[i+1]=='C' and st[i]=='J':
            cost+=Y
        if st[i]=='C' or st[i]=='J':
            lastChar = st[i]
        if st[i]=='?' and st[i+1]=='J':
            if lastChar=='C':
                cost+=X
        if st[i]=='?' and st[i+1]=='C':
            if lastChar=='J':
                cost+=Y

    print("Case #"+str(t+1)+": "+str(cost))