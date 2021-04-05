# Graph-Traversal-BFS
A graph traversal program based on Breadth First Search algorithm

This program traverses a field of arrows (red or blue). It finds a route from the arrow in the top left corner to the bullseye in the bottom right corner. It follows the direction that the arrows point, and it only stop on the other colored arrow or the bullseye. For example, starting on red, then choosing a blue arrow (in the direction that the red arrow is pointing), then from the blue arrow choosing a red arrow in the direction the blue arrow is pointing. Continuing in this fashion until it finds the bullseye in the bottom right corner.

To run the graph traversal program using command line:
```
    python verifyGraph.py <input_graph_file> <output_soln_file>
Ex: python verifyGraph.py small.txt small-soln.txt
```
To run the verification program:
```
    python verifyGraph.py <input_graph_file> <output_soln_file>
Ex: python verifyGraph.py small.txt small-soln.txt
```
