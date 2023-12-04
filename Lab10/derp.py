"""
141 Tree Lab - Derp the Interpreter

The Derp interpreter parses and evaluates prefix integer expressions
containing basic arithmetic operators (*,//,-,+). It performs arithmetic with
integer operands that are either literals or variables (read from a
symbol table).  It dumps the symbol table, prints the infix expression with
parentheses to denote order of operation, and evaluates the expression to
print the result.

Author: CS@RIT.EDU

Author: PUT YOUR FULL NAME HERE
"""

import derp_types as derp


def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    precondition: tokens is a non-empty list of strings
    """
    if not tokens:
        pass
    elif tokens[0].isidentifier():
        return derp.VariableNode(tokens.pop(0))
    elif tokens[0].isdigit():
        return derp.LiteralNode(tokens.pop(0))
    else:
        temp = tokens.pop(0)
        return derp.MathNode(parse(tokens), temp, parse(tokens))


def infix(node: str):
    """infix: Node -> String
    Perform an inorder traversal of the node and return a string that
    represents the infix expression.
    precondition: node is a valid derp tree node
    """
    equation = ""
    if not node:
        return
    elif node.left and node.right:
        infix(node.left)
    elif not node.left:
        infix(node.right)
    else:


def evaluate(node, sym_tbl):
    """
    evaluate: Node * dict(key=String, value=int) -> int
    Return the result of evaluating the expression represented by node.
    Precondition: all variable names must exist in sym_tbl
    precondition: node is a valid derp tree node
    """

    pass


def main() -> None:
    """
    main: None -> None
    The main program prompts for the symbol table file, and a prefix
    expression. It produces the infix expression, and the integer result of
    evaluating the expression
    """

    print("Hello Herp, welcome to Derp v1.0 :)")
    in_file = input("Herp, enter symbol table file: ")
    file = open(in_file, 'r')
    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")
    while True:
        prefix_exp = input("derp> ")
        if prefix_exp == "":
            break
        else:
            prefix_list = prefix_exp.split()
        root = prefix_list[0]
        tr = parse(prefix_list)
        infix_str = infix(tr)
        print(f"Derping the infix expression: {infix_str}")
        for line in file:
            result = evaluate(tr, line)
        print(f"Derping the evaluation: {result}")
    print("Goodbye Herp :(")

if __name__ == "__main__":
    main()
