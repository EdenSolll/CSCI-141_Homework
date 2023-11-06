"""
This program solves a ball sorting puzzle.
The puzzle consists of three stacks of balls, each of which can hold balls of different colors.
The goal is to move all the balls from the first stack to their matching color stack.

The program uses a stack data structure to keep track of the balls in each stack and implements an algorithm to move the balls to their corresponding stacks.
The program also uses an animation module to visualize the moves made by the algorithm.

The program can be run by executing the main() function, which prompts the user to enter the initialization text for the game and then
solves the puzzle using the algorithm function. The program outputs the number of moves required to solve the puzzle and displays an animation of the moves made.

Author: Eden Grace
Date: 12/7/2023
File: ball_puzzle.py
"""

import ball_puzzle_animate as animate
import cs_stack as stk
from typing import NewType

stack = NewType("stack", list)


def get_stack_from_type(ball_type: str, stack_1: stack, stack_2: stack, stack_3: stack, stack_list: list[stack]) -> tuple[int, int]:
    """
    Given a ball type and three stacks, moves the ball to the appropriate stack and returns the number of moves made.

    Args:
    - ball_type (str): the type of ball to move (either "R", "G", or "B")
    - stack_1 (stack): the first stack
    - stack_2 (stack): the second stack
    - stack_3 (stack): the third stack
    - stack_list (list[stack]): a list of the three stacks

    Returns:
    - int: the number of moves made to move the ball to the appropriate stack
    """
    moves = 0
    stop = 0
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
                    return moves, stop + 1
                else:
                    for _ in range(instances_of_R):
                            moves += move(stack_3, stack_2, stack_list)
        case _:
            return 0, 0
    return moves, stop


def move(starting_stack: stack, ending_stack: stack, stack_list: list[stack]) -> int:
    """
    Moves the top ball from the starting stack to the ending stack and animates the move.

    Args:
        starting_stack (stack): The stack from which the ball is to be moved from.
        ending_stack (stack): The stack to which the ball is to be moved.
        stack_list (list[stack]): The list of all stacks in the game.

    Returns:
        int: 1, indicating that a move was completed.
    """
    stk.push(ending_stack, stk.pop(starting_stack))
    animate.animate_move(stack_list, stack_list.index(starting_stack), stack_list.index(ending_stack))
    return 1


def algorithm(stack_1: stack, stack_2: stack, stack_3: stack) -> int:
    """
    This function takes in three stacks and returns the number of moves required to move each items to their corresponding stack.

    Parameters:
    stack_1 (Stack): The first stack
    stack_2 (Stack): The second stack
    stack_3 (Stack): The third stack

    Returns:
    int: The number of moves required to move all the elements to their correct stack.
    """
    moves = 0
    stack_list = [stack_1, stack_2, stack_3]
    while stk.is_empty(stack_1) is False:
        result_1, stop = get_stack_from_type(stk.top(stack_1), stack_1, stack_2, stack_3, stack_list)
        moves += result_1
        if stop > 0:
            break
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
