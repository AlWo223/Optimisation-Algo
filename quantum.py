import heapq
import math

### Store input data
N = int(input().strip())
#L, nop, nw = map(int, input().strip().split(" "))
def apply_operation(word, operation):
    output = ""
    #word = [int(bit) for bit in word]
    for bit, letter in zip(word, operation):
        if(letter=="N"):
            output+= bit # do nothing
        if(letter=="F"):
            # inver bit
            if(bit=="0"):
                output+="1"
            else:
                output+="0"
        if(letter=="S"):
            output+="1" # set bit to 1
        if(letter=="C"):
            output+="0" # reset bit to 0
    return ''.join(output)

def dijkstra(N):
    output_output_list = []

    for ii in range(0, N):
        L, nop, nw = map(int, input().strip().split(" "))
        operations = {}

        for jj in range(0, nop):
            op_code, op_cost = input().strip().split(" ")
            operations[op_code] = int(op_cost)

        output_list = []

        for jj in range(0, nw):
            ### Dijsktra Algorithm to find cheapest operations for bit code
            word, target = input().strip().split(" ")
            
            minimum_costs = {word: 0}
            visited_words = set()
            pq = [(0, word)]

            while pq:
                current_cost, current_word = heapq.heappop(pq)
                visited_words.add(current_word)
                if current_word == target:
                    break
                for operation in operations:
                    neighbour = apply_operation(current_word, operation)
                    if neighbour not in visited_words:
                        possible_costs = minimum_costs[current_word] + operations[operation]
                        if (possible_costs < minimum_costs.get(neighbour, math.inf)):
                            minimum_costs[neighbour] = possible_costs
                            heapq.heappush(pq, (minimum_costs[neighbour], neighbour))

            if(target in minimum_costs):
                output = str(minimum_costs[target])
            else:
                output = "NP"
            output_list.append(output)

        output_output_list.append(output_list)

    for output_list in output_output_list:
        print(" ".join(output_list))

dijkstra(N)