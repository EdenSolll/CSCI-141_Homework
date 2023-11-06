import ball_puzzle_animate as animate
import cs_stack as stack

def get_stack_from_type(ball_type: str) -> list[str]:
   match ball_type:
       case "Red", "Blue":
           return blue_stack
       case "Green":
           return green_stack
   return None

def move(starting_stack, ending_stack):
    """
    This function will move the ball from the starting stack to the ending stack.
    """
    stack.push(ending_stack, stack.pop(starting_stack))

def aglorithm(stack_1, stack_2, stack_3):
    """
    This function will take in a ball type and will move the ball to the
    correct stack. 
    """
    for ball in stack_1:
        move(stack_1, get_stack_from_type(ball))

def main():
    usr_input = input("Enter initalization text: ")
    red_stack = stack.make_empty_stack()
    blue_stack = stack.make_empty_stack()
    green_stack = stack.make_empty_stack()
    for i in usr_input:
        stack.push(red_stack, i)


if __name__ == "__main__":
    main()
