"""
141 Tree Lab - Derp the Interpreter

The Derp interpreter parses and evaluates prefix integer expressions
containing basic arithmetic operators (*,//,-,+). It performs arithmetic with
integer operands that are either literals or variables (read from a
symbol table).  It dumps the symbol table, prints the infix expression with
parentheses to denote order of operation, and evaluates the expression to
print the result.

Author: CS@RIT.EDU

Author: Eden Grace
"""

import derp_types as derp

OPERATORS = ["+", "-", "*", "/", "%", "//", "**"]


def parse(
    tokens: list[str],
) -> derp.LiteralNode | derp.VariableNode | derp.MathNode:
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    precondition: tokens is a non-empty list of strings
    """
    if not tokens:
        raise ValueError("Empty token list")
    elif tokens[0].isidentifier():
        return derp.VariableNode(tokens.pop(0))
    elif tokens[0].isdigit():
        return derp.LiteralNode(int(tokens.pop(0)))
    else:
        temp = tokens.pop(0)
        return derp.MathNode(parse(tokens), temp, parse(tokens))


def infix(node: derp.LiteralNode | derp.VariableNode | derp.MathNode) -> str:
    """infix: Node -> String
    Perform an in order traversal of the node and return a string that
    represents the infix expression.
    precondition: node is a valid derp tree node
    """
    equation: str = ""
    if node:
        if isinstance(node, derp.VariableNode):
            equation += str(node.name)
        elif isinstance(node, derp.LiteralNode):
            equation += str(node.val)
        elif isinstance(node, derp.MathNode):
            equation += f"({infix(node.left)} {node.operator} {infix(node.right)})"
    return equation


def evaluate(node: derp.LiteralNode | derp.VariableNode | derp.MathNode) -> int:
    """
    evaluate: Node * dict(key=String, value=int) -> int
    Return the result of evaluating the expression represented by node.
    precondition: node is a valid derp tree node
    """
    result: int = 0
    equation = infix(node).strip(" ()").split()
    if len(equation) == 1 and equation[0].isnumeric():
        return int(equation[0])
    for i, char in enumerate(equation):
        if char in OPERATORS:
            match char:
                case "+":
                    result += int(equation[i - 1]) + int(equation[i + 1])
                case "-":
                    result += int(equation[i - 1]) - int(equation[i + 1])
                case "*":
                    result += int(equation[i - 1]) * int(equation[i + 1])
                case "/":
                    result += int(equation[i - 1]) / int(equation[i + 1])
                case "//":
                    result += int(equation[i - 1]) // int(equation[i + 1])
                case "**":
                    result += int(equation[i - 1]) ** int(equation[i + 1])
    return result


def main() -> None:
    """
    main: None -> None
    The main program prompts for the symbol table file, and a prefix
    expression. It produces the infix expression, and the integer result of
    evaluating the expression
    """

    print("Hello Herp, welcome to Derp v1.0 :)")
    in_file = input("Herp, enter symbol table file: ")

    # Student: Construct and display the symbol table here

    file = open(in_file, "r")
    for line in file:
        print(line)

    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")

    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation

    while True:
        prefix_exp = input("derp> ")
        if prefix_exp == "":
            break
        else:
            # Student: Generate the list of tokens from the prefix expression.

            prefix_list = prefix_exp.split()

        # Student: Call parse() with the list of tokens and save the root of the parse tree.

        tr = parse(prefix_list)

        # Student: Generate the infix expression by calling infix and saving the string.

        infix_str = infix(tr)
        print(f"Derping the infix expression: {infix_str}")

        # Student: Evaluate the parse tree by calling evaluate and saving the integer result.

        result = evaluate(tr)

        # Student: Modify the print statement to include the result.

        print(f"Derping the evaluation: {result}")

    print("Goodbye Herp :(")


if __name__ == "__main__":
    main()
