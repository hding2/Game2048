# Game2048
Build game 2048 and visualize it. The first file is the main.py file where we run all the codes and will import all functions from the second file game2048.py. 

Game Rule
The matrix is switching between static and moving these two situations.
Initial the 4*4 matrix with randomly generated new number 2 in any two empty cells.
For each move, check all items first, then: (1) if two numbers are the same and adjacent in the moving direction, add up and move to the right space; (2) previous cells back to space; (3) move all rest cells; (4) randomly generate a new number 2 in any empty cell; (5) if no space, no two numbers are the same and adjacent in any direction, return fail.

Approach: slide-merge-slide


Example 1:
[2, 0, 2, 0] → [4, 0, 0, 0] (move left)
[2, 0, 2, 0] → [2, 2, 0, 0] → [4, 0, 0, 0] → [4, 0, 0, 0]

Example 2:
[2, 0, 2, 3] → [4, 3, 0, 0] (move left)
[2, 0, 2, 3] → [2, 2, 3, 0] → [4, 0, 3, 0] → [4, 3, 0, 0]

Example 3:
[2, 2, 2, 2] → [4, 4, 0, 0] (move left)
[2, 2, 2, 2] → [2, 2, 2, 2] → [4, 0, 4, 0] → [4, 4, 0, 0]

