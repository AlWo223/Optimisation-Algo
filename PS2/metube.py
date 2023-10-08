import math
### Store input data

N = int(input().strip()) # Number of intersections, total distance
dp = [math.inf] * (2**10) # list for storing all potential category states
dp[0] = 0

categoryDict = {}
categoryBitCounter = 0 # translate categories to bits

for ii in range(0, N):
    length, categories = input().strip().split(" ")
    bitmask = 0

    for category in categories:
        if not(category in categoryDict):
            categoryDict[category] = categoryBitCounter # generate bit code for category
            categoryBitCounter += 1

        bitmask |= (1 << (categoryDict[category])) # build bitmask of movie

    for mask in range(0, len(dp)):
        if(dp[mask]==math.inf):
            continue
        maskNew = mask | bitmask
        dp[maskNew] = min(dp[maskNew], dp[mask] + int(length))

print(dp[2**len(categoryDict)-1])