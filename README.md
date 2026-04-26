# CPSC-335-10_Project-3
- Richard Le
- Richard.le@csu.fullerton.edu
- Marco Chavez
- marco_chavez@csu.fullerton.edu
- Arman Madatyan 
- armanmadatyan@csu.fullerton.edu
- Jeremy Mejia
- fr.jeremy@csu.fullerton.edu

# CPSC 335 — Project 3 — Algorithm 1
## The Spread of Fire in a Forest  

## Description
This program simulates the spread of a wildfire in a forest grid and calculates the minimum number of days required to burn all healthy trees.

The forest is represented as a 2D grid:
- 0 = empty space  
- 1 = healthy tree  
- 2 = burned tree  

Rules:
- A healthy tree becomes burned if it is adjacent (up, down, left, right) to a burned tree  
- Fire spreads one level per day  
- If some trees cannot be reached, the program returns -1  
- If no healthy trees exist, the program returns 0  

The algorithm uses **Breadth-First Search (BFS)**:
- All initially burned trees are added to a queue  
- Fire spreads level-by-level (day-by-day)  
- Each level represents one day  

## Sample Outputs
Example 1 Output: 4  
Example 2 Output: -1  
Example 3 Output: 0  

## How to Run
Make sure Python 3 is installed.
And Libary collections using deque

# CPSC 335 — Project 3 — Algorithm 2
