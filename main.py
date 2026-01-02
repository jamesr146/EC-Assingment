import random
import math 




from Visualization import plot



#Each individual represents a permutation of cargo ID
class Individual: 
    def __init__(self, genome):
        self.genome = genome[:]
        self.fitness = None

    def copy (self):
        new = Individual(self.genome)
        new.fitness = self.fitness
        return new 
    


#Stores a lits of individuals and provides utility methods 
class Population:
    def __init__(self, individuals):
        
        self.individuals = individuals

    def get_best(self):
        
        return min(self.individuals, key=lambda ind: ind.fitness)
        
#Randomly selects 'K' individuals and selects the best 
def tournamanet_selection(pop, k=3):
    
    competitors = random.sample(pop.individuals, k)
    return min(competitors, key=lambda ind: ind.fitness).copy()


#Mutation operator for permutation based genomes
def swap_mutation (individual, mutation_rate=0.1):
    
    new_genome = individual.genome[:]
    for i in range(len(new_genome)):
        if random.random() < mutation_rate:
            j = random.randrange(len(new_genome))
            new_genome[i], new_genome[j] = new_genome[j], new_genome[i]
    return Individual(new_genome)



#Crossover operator for permutations
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



#GA evolution loop
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


#Container requirements 
CONTAINER_W = 20.0
CONTAINER_H = 15.0
CONTAINER_MAX_HEIGHT = 9999999.0 


CYLINDERS = [
    {"diameter": 2.0, "weight": 100.0},
    {"diameter": 2.4, "weight": 150.0},
    {"diameter": 1.6, "weight": 80.0},
    {"diameter": 3.0, "weight": 200.0}
]


def radius(cid):
    return CYLINDERS[cid]["diameter"] / 2.0

def weight(cid):
    return CYLINDERS[cid]["weight"]




#Row by row placement starting at rear of container
def decode_ordering(ordering):
   
    placed = []

    x = 0.0
    y = 0.0
    row_height = 0.0

    for cid in ordering:
        r = radius(cid)
        d = 2.0 * r

        if x + d > CONTAINER_W:
            x = 0.0
            y += row_height
            row_height = 0.0

        if y + d > CONTAINER_H:
            break 


        cx = x + r 
        cy = y + r 
        placed.append((cid, cx, cy))

        x += d 
        row_height = max(row_height, d)

    return placed



#Fitness lower = better
def cargo_fitness(ind):
    
    ordering = ind.genome
    placed = decode_ordering(ordering)


    penalty = 0.0 

    unplaced = len(ordering) - len(placed)
    penalty += unplaced * 1_000_000


    total_w = sum(weight(cid) for (cid, _, _) in placed)
    if total_w > CONTAINER_MAX_HEIGHT:
        penalty += (total_w - CONTAINER_MAX_HEIGHT) * 10_000.0

    if total_w > 0:
        com_x = sum(x * weight(cid) for (cid, x, _) in placed) / total_w
        safe_min = 0.2 * CONTAINER_W
        safe_max = 0.8 * CONTAINER_W

        if com_x < safe_min:
            penalty += (safe_min - com_x) * 100_000.0
        elif com_x > safe_min:
            penalty += (com_x - safe_min) * 100_000.0

    else: 
        penalty += 1_000_000.0

    if placed:
        max_y = max(y + radius(cid) for (cid, _, y) in placed)
        penalty += max_y


    return penalty


    
if __name__ == "__main__":
    random.seed(0)

    num_items = len(CYLINDERS)
    pop_size = 40

    pop = Population([
        Individual(random.sample(range(num_items), num_items ))
        for _ in range(pop_size)
    ])

    best = evolve(pop, cargo_fitness, generations=200)
    
    print("Final Best", best.genome, best.fitness)
    placements = decode_ordering(best.genome)
    
    print("Placements (id, x, y):")
    for cid, x, y in placements:
        print(cid, x, y)
       
       
    plot(placements, CONTAINER_W, CONTAINER_H, CYLINDERS)

  



