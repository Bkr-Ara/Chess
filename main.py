from population import Population
def main():
    population_size = 50
    population = Population(population_size)

    while True:
        population.check_population()
        maxFit, bestSolution = population.evaluate()
        if maxFit == 64:
            break
        population.create_new_generation()

    display_solution(bestSolution)


if __name__ == "__main__":
    main()
