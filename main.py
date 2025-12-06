import random


#population 
class Individual: 
    def __init__(self, genome):
        self.genome = genome [:]
        self.fitness = None

    def copy (self):
        new = Individual(self.genome)
        new.fitness = self.fitness
        return new 
    

class population:
    def __init__(self, individuals):
        self.individuals = individuals

    def get_best(self):
        return min(self.individuals, key=lambda ind: ind.fitness)
        


def tournamanet_selection(pop, k=3):
    competitors = random.sample(pop.individuals, k)
    return min(competitors, key=lambda ind: ind.fitness).copy()

def swap_mutation (individual, mutation_rate=0.1):
    new_genome = individual.genome[:]
    for i in range(len(new_genome)):
        if random.random() < mutation_rate:
            j = random.randrange(len(new_genome))
            new_genome[i], new_genome[j] = new_genome[j], new_genome[i]
    return Individual(new_genome)




#temp
def dummy_fitness(ind):
    return sum(ind.genome)



if __name__ == "__main__":
    num_items = 10
    pop_size = 10

    pop = population([
        Individual(random.sample(range(num_items), num_items ))
        for i in range(pop_size)
    ])

    for ind in pop.individuals:
        ind.fitness = dummy_fitness(ind)

    best = pop.get_best()
    print("Best Before Mutation: ", best.genome, best.fitness)

    mutated = swap_mutation(best) 
    mutated.fitness = dummy_fitness(mutated)

    print("Best After Mutation: ", mutated.genome, mutated.fitness)


