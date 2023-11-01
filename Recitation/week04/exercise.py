"""
CSCI-141 Computer Science 1 Recitation Exercise
04-RecursionToLoop
Bunny Population

A program that uses a formula to determine the bunny population based on
an initial population and a number of generations to go through.
This program has a tail recursive function, bunny_pop_rec, and
an iterative function, bunny_pop_iter, that both accomplish the same
task.

This is the starter code for the pair exercise that is asking you to
implement the recursive and iterative functions.
"""


def bunny_pop_rec(pop, gen):
    """
    Recursively compute the bunny population.
    :param pop: current population
    :param gen: current generation
    :return: the population at this generation
    """
    if gen == 0:
        return pop
    else:
        return bunny_pop_rec((pop // 2) * 10, gen - 1)


def bunny_pop_iter(pop, gen):
    """
    Iteratively compute the bunny population.
    :param pop: current population
    :param gen: current generation
    :return: the population at this generation
    """
    while gen > 0:
        pop = (pop // 2) * 10
        gen -= 1
    return pop


def test_bunnies():
    """
    A test function for both the recursive and iterative bunny population
    functions.  The results should be visually verified when run.
    """
    pop = 1
    gen = 3
    while gen <= 10:
        print("bunny_pop_rec(", pop, ",", gen, ") =", bunny_pop_rec(pop, gen))
        print("bunny_pop_iter(", pop, ",", gen, ") =", bunny_pop_iter(pop, gen))
        gen = gen + 1


def main():
    """
    Run the test function for the bunny population.
    :return:
    """
    test_bunnies()


if __name__ == "__main__":
    main()


"""
question 4

bunnies_pop_rec(10, 3) = bunnies_pop_rec(50, 2)
bunnies_pop_rec(50, 2) = bunnies_pop_rec(250, 1)
bunnies_pop_rec(250, 1) = bunnies_pop_rec(1250, 0)
bunnies_pop_rec(1250, 0) = bunnies_pop_rec(1250, 0)
"""

"""
question 5

Time   0   1   2   3
pop   10  50   250 1250
gen    3   2   1   0
"""
