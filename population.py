import random, math, itertools
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

    def roulette_selection(self):
        new_genotypes = random.choices(self.genotypes,weights=self.fittnes_values,k=len(self.genotypes))

        self.genotypes = new_genotypes
        self.get_fitness_values()
        self.__get_best_genotype()

    def rank_selection(self):
        genotype_fitness_pair = [(1/self.fittnes_values[i],self.genotypes[i]) for i in range(len(self.fittnes_values))]

        genotype_fitness_pair.sort(key=lambda fintness_value: fintness_value[0])

        self.genotypes = random.choices(self.genotypes,weights=[1/x for x in reversed(range(1,len(self.genotypes)+1))],k=len(self.genotypes))
        self.get_fitness_values()
        self.__get_best_genotype() 

    def random_crossing(self,amount):
        for crossing in range(amount):
            first_parent_index = random.randint(0,len(self.genotypes)-1)
            second_parent_index = random.randint(0,len(self.genotypes)-1)

            while(second_parent_index == first_parent_index):
                second_parent_index = random.randint(0,len(self.genotypes)-1)
            
            first_parent = list(itertools.chain.from_iterable(self.genotypes[first_parent_index].solution))
            second_parent = list(itertools.chain.from_iterable(self.genotypes[second_parent_index].solution))

            crossing_point = random.randint(0,len(first_parent))

            first_children = first_parent[crossing_point::]
            second_children = second_parent[crossing_point::]

            first_parent[crossing_point::] = second_children
            second_parent[crossing_point::] = first_children        

            first_new_genotype = []
            second_new_genotype = []

            for i in range(len(self.genotypes[first_parent_index].solution)):
                first_new_genotype.append(first_parent[i*5:(i+1)*5])
                second_new_genotype.append(second_parent[i*5:(i+1)*5])

            self.genotypes[first_parent_index].update_solution(first_new_genotype)
            self.genotypes[second_parent_index].update_solution(second_new_genotype)

            self.get_fitness_values()
            self.__get_best_genotype() 

    def tournament_crossing(self,amount):
        for crossing in range(amount):
            first_tournament_group = random.choices(self.genotypes,k=random.randint(1,math.floor(len(self.genotypes)/2)))
            second_tournament_group = random.choices(self.genotypes,k=random.randint(1,math.floor(len(self.genotypes)/2)))
            
            first_fittnes_values = []
            second_fittnes_values = []
            
            for genotype in first_tournament_group: 
                genotype_fittnes_value = 0
                for i in range(len(self.groups)):
                    genotype_fittnes_value += fitness_function(genotype.solution[i],self.groups[i])
                first_fittnes_values.append([genotype_fittnes_value,genotype])

            for genotype in second_tournament_group: 
                genotype_fittnes_value = 0
                for i in range(len(self.groups)):
                    genotype_fittnes_value += fitness_function(genotype.solution[i],self.groups[i])
                second_fittnes_values.append([genotype_fittnes_value,genotype])

            first_fittnes_values.sort(key=lambda fintness_value: fintness_value[0])
            second_fittnes_values.sort(key=lambda fintness_value: fintness_value[0])

            first_parent_index = self.fittnes_values.index(first_fittnes_values[0][0])
            second_parent_index = self.fittnes_values.index(second_fittnes_values[0][0])
            
            first_parent = list(itertools.chain.from_iterable(first_fittnes_values[0][1].solution))
            second_parent = list(itertools.chain.from_iterable(second_fittnes_values[0][1].solution))

            crossing_point = random.randint(0,len(first_parent))

            first_children = first_parent[crossing_point::]
            second_children = second_parent[crossing_point::]

            first_parent[crossing_point::] = second_children
            second_parent[crossing_point::] = first_children        

            first_new_genotype = []
            second_new_genotype = []

            for i in range(len(self.genotypes[first_parent_index].solution)):
                first_new_genotype.append(first_parent[i*5:(i+1)*5])
                second_new_genotype.append(second_parent[i*5:(i+1)*5])

            self.genotypes[first_parent_index].update_solution(first_new_genotype)
            self.genotypes[second_parent_index].update_solution(second_new_genotype)

            self.get_fitness_values()
            self.__get_best_genotype() 

        
        

    