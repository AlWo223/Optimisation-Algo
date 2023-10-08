### Store input data
N = int(input().strip()) # number of elements in S
S = list() # elements

for xx in range(0, N):
    S.append(int(input().strip()))

S = list(sorted(S, reverse=True))

for xx in range(0, N): # sum of 3 elements
    for ii in range( N): # a 
        if(ii == xx): continue
        doubleCheck = set()
        sum1 = S[xx] - S[ii] # d - a = b + c
        for jj in range (ii+1, N): # b
            if(jj == xx): continue
            sum2 = sum1 - S[jj] # d - a - b = c
            if(sum2 in doubleCheck):
                print(S[xx])
                exit()
            else:
                doubleCheck.add(S[jj])

print("No Solution")