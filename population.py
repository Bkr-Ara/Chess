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


