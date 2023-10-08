import heapq

### Store input data
n, k = map(int, input().strip().split(" "))
deadlines = list(map(int, input().strip().split(" ")))
deadlines.sort()

workload_left = [k] # list of current workload

pq = [(k, 0)] # PQ considering the workload (worker with lowest workload preferred)

for deadline in deadlines:
    temp = []
    added = False

    while(pq):
        optimal_workload_left, optimal_worker = heapq.heappop(pq) # get optimal worker for new task
        if(optimal_workload_left>0 and k-optimal_workload_left<deadline):
            workload_left[optimal_worker] -= 1
            if not(workload_left[optimal_worker]==0):
                heapq.heappush(pq, (workload_left[optimal_worker], optimal_worker))
            added = True
            break
        temp.append((optimal_workload_left, optimal_worker))
    if not added:
        workload_left.append(k-1)
        heapq.heappush(pq, (workload_left[-1], len(workload_left)-1)) 
    for x in temp:
        heapq.heappush(pq, x)

print(workload_left.count(0))