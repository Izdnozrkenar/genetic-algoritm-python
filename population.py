import random, math
from genotype import Genotype
from fitness_function_helpers import fitness_function

class Population():
    def __init__(self, size, groups, books):
        self.groups = groups
        
        genotypes = []

        for new_genotype in range(size):
            genotypes.append(Genotype(books,len(groups)))

        self.genotypes = genotypes
        self.get_fitness_values()
        self.best_genotype = None
        self.__get_best_genotype()

    def get_fitness_values(self):
        fittnes_values = []
        
        for genotype in self.genotypes: 
            genotype_fitness = 0
            for i in range(len(self.groups)):
                genotype_fitness += fitness_function(genotype.solution[i],self.groups[i])
            fittnes_values.append(genotype_fitness)
        
        self.fittnes_values = fittnes_values

    def __get_best_genotype(self):
        contendter = self.genotypes[self.fittnes_values.index(min(self.fittnes_values))].solution,min(self.fittnes_values)
        
        if(self.best_genotype == None or self.best_genotype[1] > contendter[1]):
            self.best_genotype = contendter
    
    def print_population(self):
        for genotype in self.genotypes:
            print(genotype.solution)

    def mutation(self, mutation_rate):
        number_of_mutated_genes = math.floor(len(self.genotypes)*15*mutation_rate)

        for random_chromosome in range(number_of_mutated_genes):
            index_to_mutate = random.randint(0,len(self.genotypes)*15-1)

            gene_to_mutate = self.genotypes[math.floor(index_to_mutate/15)].solution[index_to_mutate%3][index_to_mutate%5]

            if(gene_to_mutate=="1"):
                self.genotypes[math.floor(index_to_mutate/15)].update_chromosome(index_to_mutate%3,index_to_mutate%5,"0")
            else:
                self.genotypes[math.floor(index_to_mutate/15)].update_chromosome(index_to_mutate%3,index_to_mutate%5,"1")

        
        self.get_fitness_values()
        self.__get_best_genotype()   

    