### Store input data
N = int(input().strip()) # number of elements in S
S = list() # elements

for xx in range(0, N):
    S.append(int(input().strip()))

#S.sort(reverse=True)
listSet = set(S)
S = list(listSet)
S = list(sorted(S, reverse=True))

max = max(S)
min = min(S)
topLimit = max-min
bottomLimit = min-max

# Calculate pair sums, O(N^2)
pairs = {}
for aa in range(0, N):
    for bb in range(aa+1, N):
        pairSum = S[aa] + S[bb]
        if(pairSum>topLimit) or (pairSum<bottomLimit): continue
        #if(pairSum) not in pairs:
        pairs[pairSum] = (S[aa], S[bb])
        #pairs[pairSum].append((S[aa], S[bb]))
#print(pairs)
# a + b = d - c
for dd in range(0, N):
    for cc in range(0, N):
        if(cc == dd): continue
        c,d = S[cc], S[dd]
        searchValue = d - c
        if(searchValue in pairs):
            (a, b) = pairs[searchValue]
            #for (a, b) in pairs[searchValue]:
            noSharedIndices = (d != a) and (d != b) and (c != a) and (c != b)
            if(noSharedIndices):
                print(S[dd])
                exit()

print("no solution")