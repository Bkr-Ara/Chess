from population import Population
from game_UI import show_solution


def main():
    population_size = 50

    # Création de la population initiale
    population = Population(population_size)

    while True:
        # Vérification de la validité de la population courante
        population.check_population()

        # Évaluation de la génération courante
        maxFit, bestSolution = population.evaluate()
        print(f"Génération {population.generation} : meilleure fitness = {maxFit}")

        if maxFit == 64:
            break

        # Génération de la nouvelle population
        population.create_new_generation()

    # Affichage de la solution
    show_solution(bestSolution.path, population.generation)


if __name__ == "__main__":
    main()