import ball_puzzle_animate as animate
import cs_stack as stk
from typing import NewType

stack = NewType("stack", list)


def get_stk_from_type(
    ball_type: str, stack_1: stack, stack_2: stack, stack_3: stack, stk_list: list
) -> None:
    match ball_type:
        case "B":
            move(stack_1, stack_3, stk_list)
        case "R":
            move(stack_1, stack_2, stk_list)
        case "G":
            if stk.top(stack_2) == "R":
                move(stack_2, stack_3, stk_list)
                move(stack_1, stack_2, stk_list)
                move(stack_3, stack_2, stk_list)
            else:
                move(stack_1, stack_2, stk_list)
        case _:
            return None


def move(starting_stk, ending_stk, stk_list) -> None:
    """
    This function will move the ball from the starting stk to the ending stk.
    """
    stk.push(ending_stk, stk.pop(starting_stk))
    animate.animate_move(stk_list, starting_stk, ending_stk)


def algorithm(stack_1, stack_2, stack_3, i) -> None:
    """
    This function will take in a ball type and will move the ball to the
    correct stk.
    """
    stk_list = [stack_1, stack_2, stack_3]
    get_stk_from_type(stk.top(stack_1), stack_1, stack_2, stack_3, stk_list)
    for _ in range(i - 1):
        get_stk_from_type(stk.top(stack_1), stack_1, stack_2, stack_3, stk_list)
    while stk.top(stack_2) == "R":
        move(stack_2, stack_1, stk_list)


def main():
    usr_input = input("Enter initalization text: ")
    red_stack = stk.make_empty_stack()
    green_stack = stk.make_empty_stack()
    blue_stack = stk.make_empty_stack()
    animate.animate_init(usr_input)
    for i in usr_input:
        stk.push(red_stack, i)
    algorithm(red_stack, green_stack, blue_stack, len(usr_input))
    animate.animate_finish()


if __name__ == "__main__":
    main()
