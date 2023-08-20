import heapq

### Store input data
n, k = map(int, input().strip().split(" "))
deadlines = list(map(int, input().strip().split(" ")))
deadlines.sort()

workload = [0] # list of current workload
max = n/k # max number of workers who could make K shoes each

def assign(worker, deadline):
    if(len(workload)>=worker+1):
        if(workload[worker]<k and workload[worker]<deadline):
            workload[worker] += 1
        else:
            assign(worker+1, deadline)
    else:
        workload.append(1)

for ii in range(0, n):
    assign(0, deadlines[ii])

counter = 0
for e in workload:
    if e == k: counter +=1

print(counter)