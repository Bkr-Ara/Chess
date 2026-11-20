import random
from chromosome import Chromosome

BOARD_SIZE = 8

MOVES = {
    1: (+1, -2),   # up-right
    2: (+2, -1),   # right-up
    3: (+2, +1),   # right-down
    4: (+1, +2),   # down-right
    5: (-1, +2),   # down-left
    6: (-2, +1),   # left-down
    7: (-2, -1),   # left-up
    8: (-1, -2),   # up-left
}


class Knight:
    def __init__(self, chromosome=None):
        self.position = (0, 0)
        self.chromosome = chromosome if chromosome is not None else Chromosome()
        self.path = [self.position]
        self.fitness = 0

    # ------------------------------------------------------------------
    def move_forward(self, direction):
        dx, dy = MOVES[direction]
        x, y = self.position
        self.position = (x + dx, y + dy)

    def move_backward(self, direction):
        dx, dy = MOVES[direction]
        x, y = self.position
        self.position = (x - dx, y - dy)

    # ------------------------------------------------------------------
    def is_valid(self, pos):
        x, y = pos

        # hors de l'échiquier ?
        if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
            return False

        # déjà visitée ?
        if pos in self.path:
            return False

        return True

    # ------------------------------------------------------------------
    def check_moves(self):
        self.position = (0, 0)
        self.path = [self.position]

        step = random.choice([1, -1])
        genes = self.chromosome.genes

        for i in range(len(genes)):
            original = genes[i]
            chosen = None

            for k in range(8):
                direction = (original - 1 + step * k) % 8 + 1
                self.move_forward(direction)
                if self.is_valid(self.position):
                    chosen = direction          # mouvement valide trouvé
                    break
                self.move_backward(direction)   # illégal : on annule

            if chosen is None:
                # aucun mouvement valide : on garde le mouvement (illégal) et on s'arrête
                self.move_forward(original)
                self.path.append(self.position)
                break

            genes[i] = chosen                   # on corrige le gène
            self.path.append(self.position)

    # ------------------------------------------------------------------
    def evaluate_fitness(self):
        fitness = 0
        for i in range(len(self.path)):
            x, y = self.path[i]

            # hors de l'échiquier
            if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
                break

            # déjà visitée plus tôt dans le chemin
            if self.path[i] in self.path[:i]:
                break

            fitness += 1
        self.fitness = fitness
        return fitness