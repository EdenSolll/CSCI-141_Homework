import ball_puzzle_animate as animate
import cs_stack as stk
from typing import NewType

stack = NewType("stack", list)


def get_stack_from_type(
    ball_type: str, stack_1: stack, stack_2: stack, stack_3: stack, stack_list: list
) -> None:
    match ball_type:
        case "B":
            move(stack_1, stack_3, stack_list)
        case "R":
            move(stack_1, stack_2, stack_list)
        case "G":
            instances_of_R = 0
            while stk.is_empty(stack_2) is False and stk.top(stack_2) == "R":
                move(stack_2, stack_3, stack_list)
                instances_of_R += 1
            while stk.is_empty(stack_1) is False and stk.top(stack_1) == "G":
                move(stack_1, stack_2, stack_list)
            if instances_of_R > 0:
                for _ in range(instances_of_R):
                    move(stack_3, stack_2, stack_list)
        case _:
            return None


def move(starting_stack, ending_stack, stack_list) -> None:
    """
    This function will move the ball from the starting stk to the ending stk.
    """
    stk.push(ending_stack, stk.pop(starting_stack))
    animate.animate_move(
        stack_list, stack_list.index(starting_stack), stack_list.index(ending_stack)
    )


def algorithm(stack_1, stack_2, stack_3, i) -> None:
    """
    This function will take in a ball type and will move the ball to the
    correct stk.
    """
    stack_list = [stack_1, stack_2, stack_3]
    get_stack_from_type(stk.top(stack_1), stack_1, stack_2, stack_3, stack_list)
    while stk.is_empty(stack_1) is False:
        get_stack_from_type(stk.top(stack_1), stack_1, stack_2, stack_3, stack_list)
    while stk.is_empty(stack_2) is False:
        if stk.top(stack_2) == "R":
            move(stack_2, stack_1, stack_list)


def main():
    usr_input = input("Enter initalization text: ")
    red_stack = stk.make_empty_stack()
    green_stack = stk.make_empty_stack()
    blue_stack = stk.make_empty_stack()
    animate.animate_init(usr_input)
    for i in usr_input:
        stk.push(red_stack, i)
    print(stk.is_empty(green_stack))
    algorithm(red_stack, green_stack, blue_stack, len(usr_input))
    animate.animate_finish()


if __name__ == "__main__":
    main()
