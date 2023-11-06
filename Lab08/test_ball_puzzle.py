import ball_puzzle as bp

# Test Case 1: Solving a simple puzzle with only one move needed
# Input: "R"
# Expected Output: "Puzzle solved in 1 move!"
# This test case only involves one red ball, which can be moved directly to the third stack.
# Therefore, only one move is needed to solve the puzzle.
# The animation will show the red ball being moved from the first stack to the third stack.
# The final state of the stacks will be:
# Stack 1: []
# Stack 2: []
# Stack 3: ["R"]

# Test Case 2: Solving a puzzle with multiple balls of different colors
# Input: "RGBBRGB"
# Expected Output: "Puzzle solved in 13 moves!"
# This test case involves a more complex puzzle with a mix of red (R), green (G), and blue (B) balls.
# The algorithm will move the balls according to the specified rules.
# The animation will show the sequence of moves.
# The final state of the stacks will be:
# Stack 1: []
# Stack 2: []
# Stack 3: ["R", "R", "R", "G", "G", "B", "B"]

# Test Case 3: Solving a puzzle with no possible moves
# Input: "BGBGBG"
# Expected Output: "Puzzle solved in 0 moves!"
# In this test case, all balls are initially stacked in a way that no valid moves can be made.
# The algorithm should detect this and return 0 moves without attempting any moves.

# Test Case 4: Solving a puzzle with multiple moves involving green balls
# Input: "GRGRGRG"
# Expected Output: "Puzzle solved in 7 moves!"
# This test case involves green (G) balls, which can be moved on top of any other element.
# The algorithm will take advantage of this rule to efficiently move the balls to the third stack.
# The animation will show the sequence of moves.

# Test Case 5: Solving an empty puzzle
# Input: ""
# Expected Output: "Puzzle solved in 0 moves!"
# In this test case, the input is an empty string, indicating that there are no balls to move.
# The algorithm should return 0 moves without attempting any moves.
