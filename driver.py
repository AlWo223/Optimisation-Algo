import math

### Store input data
num_gates = int(input().strip())
fees = list(map(int, input().strip().split(" ")))
access_time = list(map(int, input().strip().split(" ")))

### Initialize variables
travel_time = 0
travel_cost = 0
minimum_path = fees[0]

### Calculate travel time and cost
for i in range(1, num_gates):
    ### Update minimum path
    if(fees[i-1]<minimum_path):
        minimum_path = fees[i-1]
    ### Add cost and time for linear travel
    travel_time += 1
    travel_cost += fees[i-1]
    ### Calculate waiting time
    waiting_time = access_time[i] - travel_time
    ### Add cost and time resulting from waiting
    while(waiting_time>0):
        travel_cost += minimum_path * 2
        travel_time += 2
        waiting_time -= 2
### Return minimum travel_cost
print(travel_cost)