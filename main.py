import random


#Individual
class Individual: 
    def __init__(self, genome):
        self.genome = genome [:]
        self.fitness = None

    def copy (self):
        new = Individual(self.genome)
        new.fitness = self.fitness
        return new 
    


#population 
class Population:
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



#GA operators
def ordered_crossover(parent1, parent2):
    size = len(parent1.genome)
    a, b = sorted(random.sample(range(size), 2))

    child_genome = [None] * size
    child_genome[a:b] = parent1.genome[a:b]

    fill = [g for g in parent2.genome if g not in child_genome] 

    idx = 0
    for i in range(size):
        if child_genome[i] is None:
            child_genome[i] = fill[idx]
            idx += 1 

    return Individual(child_genome)


#GA evolve loop
def evolve(pop, fitness_fn, generations=50, crossover_rate=0.9, mutation_rate=0.1):
    for ind in pop.individuals:
        ind.fitness = fitness_fn(ind)

    for gen in range(generations):
        new_individuals = []


        elite = pop.get_best().copy()
        new_individuals.append(elite)


        while len(new_individuals) < len(pop.individuals):
            parent1 = tournamanet_selection(pop)
            parent2 = tournamanet_selection(pop)

            if random.random() < crossover_rate:
                child = ordered_crossover(parent1, parent1)
            else:
                child = parent1.copy()


            child = swap_mutation(child, mutation_rate=mutation_rate)

            child.fitness = fitness_fn(child)

            new_individuals.append(child)

        pop = Population(new_individuals)

        best = pop.get_best()
        print(f"Gen {gen}: Best fitnes = {best.fitness}")
   
    return pop.get_best()


#temp fitness
def dummy_fitness(ind):
    return ind.genome[0]




if __name__ == "__main__":
    num_items = 10
    pop_size = 10

    pop = Population([
        Individual(random.sample(range(num_items), num_items ))
        for i in range(pop_size)
    ])

    best = evolve(pop, dummy_fitness, generations=30)
    print("Final Best", best.genome, best.fitness)

