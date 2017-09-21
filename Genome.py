from random import randint, random


class Genome:

    def __init__ (self, size = 8, genes = []):
        if not len(genes):
            self.genes = [randint(0, size - 1) for x in range(size)]
            self.size = size
        else:
            self.genes = genes
            self.size = len(genes)

    def __eq__(self, other):
        return(self.genes == other.genes)

    def fitness(self, power):

        best_score = 3 * self.size

        def direction_score(direction):
            genes = self.genes
            length = len(genes)
            score_range = range(-length, 2*length)

            hash = dict()
            [hash.__setitem__(x,0) for x in score_range]

            for col_num, gene in enumerate(genes):
                hash[gene + direction * col_num] += 1

            return(sum([hash[x] ** power for x in score_range]))

        score = sum(direction_score(d) for d in [-1,0,1])
        return(score - best_score)

    def __add__(self, other):
        child_genes = []
        for i in range(self.size):
            if random() < .5:
                child_genes.append(self.genes[i])
            else:
                child_genes.append(other.genes[i])
        return(Genome(genes = child_genes))

    def mutate(self, rate):
        for i in range(self.size):
            if random() < rate:
                self.genes[i] = randint(0, self.size-1)

if __name__ == '__main__':
    good  = Genome(genes = [1, 3, 0, 2])
    good2 = Genome(genes = [1, 3, 0, 2])
    # print(good)
    # print(good2)
    # print(good == good2)
    bad = Genome(genes = [0, 0, 0, 0])
    # kid = good + bad
    # bad.mutate(1)
    pop = [bad, good]
    print([x.fitness(2) for x in pop])
    pop.sort(key = lambda x: x.fitness(2))
    print([x.fitness(2) for x in pop])
    # bad.mutate(1)
    # print([x.fitness(2) for x in pop])
