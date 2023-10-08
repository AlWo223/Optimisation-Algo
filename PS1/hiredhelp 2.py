### Store input data
n, k = map(int, input().strip().split(" "))
deadlines = list(map(int, input().strip().split(" ")))
deadlines.sort()

workload = [0] # list of current workload
counter = 0

for deadline in deadlines:
    worker = 0
    added = False
    while (worker<len(workload)):
        wl = workload[worker]
        if(wl<k and wl<deadline):
            workload[worker] += 1
            added = True
            if(workload[worker]==k):
                counter += 1
                workload.pop(worker)
            break
        worker += 1
    if not added:
        workload.append(1)

print(counter)