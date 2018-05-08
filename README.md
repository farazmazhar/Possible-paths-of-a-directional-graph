## All possible paths of directional graph
This program iterates a directional graph and displays all possible paths.

### Files
[graph.py](graph.py) contains data structures for Graph and its Node(s).
[driver.py](driver.py) contains logic to traverse a graph.
[input](input) contains nodes and edges to nodes.

#### Input file format
Input file instructions:
A node must have an edge otherwise it will be ignored. 
The file must follow 'x,y' convention. 
Invalid input such as 'a,b,c', 'a', 'a,a' etc will be ignored. 
Nodes that are self-joined will be ingored.

### Explanation
The algorithm does a depth first search. When a new node is found, it is appended to the path and the path is displayed. This happens till a node that can't traverse further.