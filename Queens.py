from Genome import Genome
from copy import deepcopy
from random import choice

def Solve(n = 8,
          power = 2,
          population_size = None,
          copy_size = None,
          new_size = None,
          mutation_rate = .01,
          mutate_best = True,
          use_chess_ranks = True,
          verbose = False,
          return_gen = False):

    if population_size is None:
        population_size = 5 * n
        if verbose: print(
            'Population size set to ', population_size, '.',
            sep='')

    if copy_size is None:
        copy_size = int(.05 * population_size)
        if verbose: print(
            copy_size, 'members will be cloned from one generation to the next.')

    if new_size is None:
        new_size = copy_size
        if verbose: print(
            new_size, 'new members will be introduced to each generation.')

    population = [Genome(size = n) for x in range(population_size)]
    population.sort(key = lambda x: x.fitness(power))

    gen_number = 0

    while population[0].fitness(power):

        if verbose:
            print('Generation ', gen_number,
                  'Best', population[0].fitness(power),
                  'Worst', population[0].fitness(power))

        gen_number += 1

        next_gen = []

        # have the best members clone directly into the next
        for i in range(copy_size):
            next_gen.append(deepcopy(population[i]))

        # introduce new random members into the population
        for i in range(new_size):
            next_gen.append(Genome(size = n))

        # breed to fill out the remainder of the population
        while len(next_gen) < population_size:
            parent_0 = choice(population)
            parent_1 = choice(population)
            child = parent_0 + parent_1
            next_gen.append(child)

        for i, member in enumerate(next_gen):
            if i or mutate_best:
                member.mutate(mutation_rate)

        population = next_gen[:]
        population.sort(key=lambda x: x.fitness(power))

    if return_gen: return(gen_number)

    winner = population[0].genes

    if use_chess_ranks: winner = [x + 1 for x in winner]
    return(winner)


if __name__ == '__main__':
    print(Solve(verbose=True))
