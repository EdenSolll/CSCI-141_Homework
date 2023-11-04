# import cs_stack as Stack
#
# red_stack = Stack.make_empty_stack()
# blue_stack = Stack.make_empty_stack()
# green_stack = Stack.make_empty_stack()
#
#
# if red_stack.top() == "Red":
# get_stack_from_type(red_stack.top()).push(red_stack.pop())
#
#
# red_stack: list[str] = []
# blue_stack: list[str] = []
# green_stack: list[str] = []
#
#
# def get_stack_from_type(ball_type: str) -> list[str]:
#    match ball_type:
#        case "Red":
#            return red_stack
#        case "Blue":
#            return blue_stack
#        case "Green":
#            return green_stack
#    return None
#
import ball_puzzle_animate.py as ani


def main():
    usr_input = input("Enter initalization text: ")
    ani.animate_init(usr_input)


if __name__ == "__main__":
    main()
