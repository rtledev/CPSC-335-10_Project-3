#Richard Le
#Richard.le@csu.fullerton.edu
#Marco Chavez
#marco_chavez@csu.fullerton.edu
#Arman Madatyan 
#armanmadatyan@csu.fullerton.edu
#Jeremy Mejia
#fr.jeremy@csu.fullerton.edu


#Determines best possible route given stop constraints
def CheapestRoute(routes, src, dst, k):

    #initialize queue
    # queue format (current location, stops, current cost)
    queue = [(src, 0, 0)]
    
    #stores best answer
    answer = float('inf')
    
    #loops through paths
    while queue:

        #removes current state
        current_node, stops, current_cost = queue.pop(0)

        #skip when stops are exceeded
        if stops > k + 1:
            continue

        #compare the best answer and current cost
        if current_node == dst:
            answer = min(answer, current_cost)
        
        #search available paths
        for neighbor in routes.get(current_node, []):
            #split neighbor
            next_node, price = neighbor
            #add new path to queue
            queue.append((next_node, stops + 1, current_cost + price))

    if answer == float('inf'): #never reached final destination
        return -1
    else:
        return answer # cheapest cost




#routes
route = {
    0: [(1, 100), (2, 500)],
    1: [(2, 100)]
}

#format is (src, dst, k), (src, dst, k)
route_examples = [(0, 2, 1), (0, 2, 0)]

#print answer
for src, dst, k in route_examples:
    answer = CheapestRoute(route, src, dst, k)
    print(f"{answer}")