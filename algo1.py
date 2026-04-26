#Richard Le
#Richard.le@csu.fullerton.edu
#Marco Chavez
#marco_chavez@csu.fullerton.edu
#Arman Madatyan 
#armanmadatyan@csu.fullerton.edu
#Jeremy Mejia
#fr.jeremy@csu.fullerton.edu

from collections import deque

# A healthy tree (represented by 1) will burn down after one day (bruned tree 2)
# empty area = 0 doesn't affect burning
# no trees burned initially and impposible for healthy trees to burn, return -1 

def burn_forest(forest):
    # checks if forest list is empty, if no trees to burn, return 0
    if not forest:
        return 0
    
    rows = len(forest)      # stores the number of rows in the forest grid
    cols = len(forest[0])   # stores the number of columns in the forest grid

    queue = deque() # Creates a queue to store the positions of the burned trees
    healthy_tree = 0    # count of healthy trees

    # we loop through the rows and cols in the forest
    for row in range(rows):
        for col in range(cols):
            # checks if current position is a burned tree, if so, we append into the queue
            if forest[row][col] == 2:
                queue.append((row,col))
            # checks if current position is a healthyTree, if that's the case, increment healthyTree count by 1
            elif forest [row][col] == 1:
                healthy_tree += 1
    
    # implies that there are no healthy trees at the start
    if healthy_tree == 0:
        return 0    # return 0 if no days are needed
    
    # implies that there is healthy trees but no burned trees
    if queue == 0:
        return -1   # returns -1 because fire cannot spread
    
    # store the four possible directions that the fires can spread
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

    days = 0 # store the number of days that pass

    # continue while fire can spread
    while queue and healthy_tree > 0:
        # we store how many burned trees will spread fire today
        current_size = len(queue) 

        # process only the rees that were bruned on this day
        for _ in range(current_size):   
            # removes the next burned tree from the queue
            row, col = queue.popleft() 

            # check each neighboring/adjacent direction
            for row_change, col_change in directions: 
                new_row = row + row_change # calcualtes the neighboring row
                new_col = col + col_change # calcualtes the neighboring col

                # checks if neighboring tree is inside the grid
                if 0 <= new_row < rows and 0 <= new_col < cols: 
                    # checking if nieghbor is a healthy tree
                    if forest[new_row][new_col] == 1:
                        # change the healthy tree into a bruned tree
                        forest[new_row][new_col] = 2 
                        # decrements healthyTree count by 1
                        healthy_tree -= 1
                        # adds teh newly burned tree to the queue
                        queue.append((new_row, new_col))

        days += 1 # increase day count after one full spread cycle

    # checks if there are heathly trees left
    if healthy_tree > 0:
        return -1   # reutnr -1 if not all thealthy trees can burn
    
    return days # returns the minimum number of days needed

# Example test
forest = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

print(burn_forest(forest))  # Expected output: 4

'''
forest = [
 [2,1,1],
 [0,1,1],
 [1,0,0]
]

print(burn_forest(forest))  # Expected output: -1
'''