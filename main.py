import random
from population import Individual, Population 




def tournamanet_selection(pop, k=3):
    competitors = random.sample(pop.individuals, k)
    return min(competitors, key=lambda ind: ind.fitness).copy()

def swap_muatation (individual mutation_rate=0.1):
    new_genome = individual.genmome[:]
    for i in range(len(new_genome)):
        if random.random() < mutation_rate:
        j = random.randrange(len(new_genome))
        new_genome[i], new_genome[j] = new_genome[j], new_genome[i]
    return individual(new_genome)







#population 
class individual: 
    def __init__(self, genome):
        self.genome = genome [:]

    def copy (self):
        new = individual(self.genome)
        new.fitness = self.fitness
        return new 
    

class population:
    def __init__(self, individuals):
        self.individuals = individuals

    def get_best(self):
        return min(self.individuals, ley=lambda ind: ind.fitness)
        