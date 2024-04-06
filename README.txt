Time and Space Complexity:
   If,
       d is the depth of the goal node
       b = 4 is the branching factor(taking that every node definitely has 4 moves)

BREADTH FIRST SEARCH:
BFS, or Breadth-First Search, is a graph traversal algorithm employed in Artificial Intelligence to systematically explore and analyze the nodes or states within a problem space.     
Unlike Depth-First Search (DFS), which delves as deeply as possible into a branch before backtracking, BFS prioritizes exploring all the immediate neighbors of a node before moving on to deeper levels.

 1. For BFS
- Time Complexity: O(4^(d+1))
- Space Complexity: O(4^(d+1))

 Run the  python code.py input.txt 0
 - input.txt is a txt file includes the pos of soldiers, tresure, musk
 - 0 is for bfs and 1 is for dfs\n
OUTPUT:
	
exploredNodes = [[0, 4], [0, 3], [1, 4], [0, 2], [2, 4], [0, 1], [1, 2], [2, 3]]
searchQueue = [
[[0, 3], [1, 4]]
[[1, 4], [0, 2]]
[[0, 2], [2, 4]]
[[2, 4], [0, 1], [1, 2]]
[[0, 1], [1, 2], [2, 3], [3, 4]]
[[1, 2], [2, 3], [3, 4], [1, 1]]
[[2, 3], [3, 4], [1, 1]]
[[3, 4], [1, 1]]
]
shortestPath = [[0, 4], [1, 4], [2, 4], [2, 3]]

DEPTH FIRST SEARCH:

	
Depth-First Search (DFS) in the context of Artificial Intelligence is a systematic algorithm used to traverse and explore the nodes or states within a problem space by delving as deeply as possible along each branch of the search tree before backtracking. Unlike Breadth-First Search (BFS), which explores all immediate neighbors of a node before moving on to deeper levels, DFS prioritizes exploring deeper nodes first, traversing down a branch until it reaches a leaf node or a dead-end before backtracking to explore other branches.
	


 2. For DFS
- Time Complexity: O(4^(d+1))
- Space Complexity: O(4*d)

Run the  python code.py input.txt 0
- input.txt is a txt file includes the pos of soldiers, tresure, musk
- 0 is for bfs and 1 is for dfs\n


OUTPUT:

	
exploredNodes = [[0, 4], [1, 4], [2, 4], [3, 4], [3, 3], [4, 3], [4, 2], [4, 1], [3, 1], [3, 0], [2, 0], [1, 0], [1, 1], [0, 1], [0, 2], [1, 2], [2, 3]]        
searchQueue = [
[[0, 3], [1, 4]]
[[0, 3], [2, 4]]
[[0, 3], [2, 3], [3, 4]]
[[0, 3], [2, 3], [3, 3]]
[[0, 3], [2, 3], [4, 3]]
[[0, 3], [2, 3], [4, 2]]
[[0, 3], [2, 3], [4, 1]]
[[0, 3], [2, 3], [3, 1]]
[[0, 3], [2, 3], [3, 0]]
[[0, 3], [2, 3], [2, 0]]
[[0, 3], [2, 3], [1, 0]]
[[0, 3], [2, 3], [1, 1]]
[[0, 3], [2, 3], [1, 2], [0, 1]]
[[0, 3], [2, 3], [1, 2], [0, 2]]
[[0, 3], [2, 3], [1, 2]]
[[0, 3], [2, 3]]
[[0, 3]]
]
shortestPath = [[0, 4], [1, 4], [2, 4], [2, 3]]
	