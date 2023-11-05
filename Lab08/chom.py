import ball_puzzle_animate as animate
import cs_stack as stk
from typing import NewType

stack = NewType("stack", list)


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
                for _ in range(instances_of_R):
                    moves += move(stack_3, stack_2, stack_list)
        case _:
            raise IndexError
    return moves


def move(starting_stack: stack, ending_stack: stack, stack_list: list[stack]) -> int:
    stk.push(ending_stack, stk.pop(starting_stack))
    animate.animate_move( stack_list, stack_list.index(starting_stack), stack_list.index(ending_stack))
    return 1


def algorithm(stack_1, stack_2, stack_3) -> int:
    moves = 0
    stack_list = [stack_1, stack_2, stack_3]
    moves += get_stack_from_type(stk.top(stack_1), stack_1, stack_2, stack_3, stack_list)
    while stk.is_empty(stack_1) is False:
        moves += get_stack_from_type(stk.top(stack_1), stack_1, stack_2, stack_3, stack_list)
    while stk.is_empty(stack_2) is False:
        if stk.top(stack_2) == "R":
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
