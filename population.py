import random
from knight import Knight


def get_fitness(knight):
    return knight.fitness


class Population:
    def __init__(self, population_size):
        self.population_size = population_size
        self.generation = 1
        self.knights = []
        for i in range(population_size):
            self.knights.append(Knight())
    
    def check_population(self):
        for knight in self.knights:
            knight.check_moves() #check_moves

    def evaluate(self):
        best = self.knights[0] 
        for knight in self.knights:
            knight.evaluate_fitness() #evaluate_fitness
            if knight.fitness > best.fitness:
                best = knight
        return best.fitness, best

    def tournament_selection(self, size):
        sample = random.sample(self.knights, size)
        sample.sort(key=get_fitness, reverse=True)
        return sample[0], sample[1]


    def create_new_generation(self):
        new_knights = []
        while len(new_knights) < self.population_size:
            parent1, parent2 = self.tournament_selection(3)
            child1, child2 = parent1.chromosome.crossover(parent2.chromosome)
            child1.mutation()
            child2.mutation()
            new_knights.append(Knight(child1))
            new_knights.append(Knight(child2))
        self.knights = new_knights
        self.generation += 1