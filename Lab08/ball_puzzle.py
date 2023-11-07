"""
This module contains a program that solves a ball puzzle game. The game consists of three stacks of balls, each of which can hold balls of different colors. 
The objective of the game is to move all the balls from the first stack to the third stack while following certain rules. 
The rules are as follows:
2. Only the top element of a stack can be moved to another stack.
3. A red element can only be moved to an empty stack or on top of another red element.
4. A blue element can only be moved to an empty stack or on top of another blue element.
5. A green element can be moved to an empty stack or on top of any other element.

The program uses a stack data structure to keep track of the balls in each stack and implements an algorithm to move the balls
 from the first stack to the third stack while following the rules. The program also uses an animation module to visualize the moves made by the algorithm.

The program can be run by executing the main() function, which prompts the user to enter the initialization text for the game and then 
solves the puzzle using the algorithm function. The program outputs the number of moves required to solve the puzzle and displays an animation of the moves made.

Professor: Lima
Author:  Eden Grace
Date: 12/7/2023
file: ball_puzzle.py
"""


import ball_puzzle_animate as animate
import cs_stack as stk
from typing import NewType

stack = NewType("stack", list)


def get_stack_from_type(ball_type: str, stack_1: stack, stack_2: stack, stack_3: stack, stack_list: list[stack]) -> int:
    """
    Given a ball type and three stacks, moves the ball to the appropriate stack and returns the number of moves made.

    Args:
    - ball_type (str): the type of ball to move (either "B", "R", or "G")
    - stack_1 (stack): the first stack
    - stack_2 (stack): the second stack
    - stack_3 (stack): the third stack
    - stack_list (list[stack]): a list of the three stacks

    Returns:
    - int: the number of moves made to move the ball to the appropriate stack
    """

def get_stack_from_type( ball_type: str, stack_1: stack, stack_2: stack, stack_3: stack, stack_list: list[stack]) -> int:
    moves = 0
    match ball_type:
        case "B":
            moves += move(stack_1, stack_3, stack_list)
        case "R":
            moves += move(stack_1, stack_2, stack_list)
        case "G":
            instances_of_R = 0
            while stk.is_empty(stack_2) is False and stk.top(stack_2) == "R":
                moves += move(stack_2, stack_3, stack_list)
                instances_of_R += 1
            while stk.is_empty(stack_1) is False and stk.top(stack_1) == "G":
                moves += move(stack_1, stack_2, stack_list)
            if instances_of_R > 0:
                if stk.is_empty(stack_1) is True:
                    for _ in range(instances_of_R):
                        moves += move(stack_3, stack_1, stack_list)
                        
                else:
                    for _ in range(instances_of_R):
                            moves += move(stack_3, stack_2, stack_list)
        case _:
            raise IndexError
    return moves


def move(starting_stack: stack, ending_stack: stack, stack_list: list[stack]) -> int:
    """
    Moves the top ball from the starting stack to the ending stack and animates the move.

    Args:
        starting_stack (stack): The stack from which the ball is to be moved.
        ending_stack (stack): The stack to which the ball is to be moved.
        stack_list (list[stack]): The list of all stacks in the game.

    Returns:
        int: 1, indicating that the move was successful.
    """
    stk.push(ending_stack, stk.pop(starting_stack))
    animate.animate_move(stack_list, stack_list.index(starting_stack), stack_list.index(ending_stack))
    return 1


def algorithm(stack_1: stack, stack_2: stack, stack_3: stack) -> int:
    """
    This function takes in three stacks and returns the number of moves required to move all the elements from stack_2 to stack_3
    while following certain rules. The rules are as follows:
    2. Only the top element of a stack can be moved to another stack.
    3. A red element can only be moved to an empty stack or on top of another red element.
    4. A blue element can only be moved to an empty stack or on top of another blue element.
    5. A green element can be moved to an empty stack or on top of any other element.
    
    Parameters:
    stack_1 (Stack): The first stack
    stack_2 (Stack): The second stack
    stack_3 (Stack): The third stack
    
    Returns:
    int: The number of moves required to move all the elements from stack_2 to stack_3 while following the rules.
    """
    moves = 0
    stack_list = [stack_1, stack_2, stack_3]
    moves += get_stack_from_type(stk.top(stack_1), stack_1, stack_2, stack_3, stack_list)
    while stk.is_empty(stack_1) is False:
        moves += get_stack_from_type(stk.top(stack_1), stack_1, stack_2, stack_3, stack_list)
    while stk.is_empty(stack_2) is False and stk.top(stack_2) == "R":
        moves += move(stack_2, stack_1, stack_list)
    return moves


def main():
    usr_input = input("Enter initalization text: ")
    red_stack = stk.make_empty_stack()
    green_stack = stk.make_empty_stack()
    blue_stack = stk.make_empty_stack()
    animate.animate_init(usr_input)
    for i in usr_input:
        stk.push(red_stack, i)
    print(f'Puzzle solved in {algorithm(red_stack, green_stack, blue_stack)} moves!')
    animate.animate_finish()


if __name__ == "__main__":
    main()
