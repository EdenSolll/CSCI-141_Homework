"""
Question 1:

Red = ["Red0", "Green0", "Blue0", "Green1"]
Green = []
Blue = []

Step-1:

Red = ["Green0", "Blue0", "Green1"]
Green = []
Blue = ["Red0"]

Step-2:

Red = ["Blue0", "Green1"]
Green = ["Green0"]
Blue = ["Red0"]

Step-3

Red = ["Blue0", "Green1"]
Green = ["Green0", "Red0"]
Blue = []

Step-4

Red = ["Green1"]
Green = ["Green0", "Red0"]
Blue = ["Blue0"]

Step-5

Red = ["Green1"]
Green = ["Green0"]
Blue = ["Blue0", "Red0"]

Step-6

Red = []
Green = ["Green0", "Green1"]
Blue = ["Blue0", "Red0"]

Step-7

Red = ["Red0"]
Green = ["Green0", "Green1"]
Blue = ["Blue0"]
"""

"""
Question 2:

Each tube should be a stack because stacks are first in first out,
When a ball is dropped into a tube, it cannot be accessed if there are any balls that have been more recently added to the tube.
Therefore the tubes should be treated as stacks

The balls as far as I can tell should be treated simply as strings, and if the string is the same as the name of the stack then it should be moved to that stack.
"""

"""
Question 3

def move(starting_stack, ending_stack:
    ending_stack.apennd(starting_stack.pop())
"""

"""
Question 4

Step-1:
Attempt to move the next ball in the starting stack to its corrisponding stack
Step-2:
If it's corrisponding stack is the starting stack move it to the second stack
Step-3:
Attempt to move the next ball in the starting stack to its corrisponding stack
Step-4:
If the stack is blocked by the first ball then move the ball blocking it to the top of the third stack, then move the ball from the first stack to the stack where it belongs, then the ball in the third stack back on top of the stack where the ball was just added.
Step-5:
Once no balls remain in the left container, smiply move the balls in the middle tube to the left tube until no balls matching the left tube's color remain
"""


red_stack: list[str] = []
blue_stack: list[str] = []
green_stack: list[str] = []


def get_stack_from_type(ball_type: str) -> list[str]:
    match ball_type:
        case "Red":
            return red_stack
        case "Blue":
            return blue_stack
        case "Green":
            return green_stack
    return None
