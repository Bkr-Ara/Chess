import random

GENES_LENGTH = 63        
MUTATION_RATE = 0.05     # probabilité de mutation de chaque gène


class Chromosome:
    def __init__(self, genes=None):
        #Sans gènes : génère 63 mouvements aléatoires (1 à 8)
        if genes is None:
            self.genes = [random.randint(1, 8) for _ in range(GENES_LENGTH)]
        else:
            self.genes = list(genes)

    def crossover(self, partner):
        
        point = random.randint(1, GENES_LENGTH - 1)
        genes1 = self.genes[:point] + partner.genes[point:]
        genes2 = partner.genes[:point] + self.genes[point:]
        return Chromosome(genes1), Chromosome(genes2)

    def mutation(self):
        
        for i in range(len(self.genes)):
            if random.random() < MUTATION_RATE:
                self.genes[i] = random.randint(1, 8)

