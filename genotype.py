import random
import math

class Genotype():
    def __init__(self, books, groups_amount):
        solution = []

        for group in range(groups_amount):
            solution.append(books[random.randint(0,len(books)-1)].binary)

        self.solution = solution

    def update_solution(self,solution):
        self.solution = solution
    
    def update_chromosome(self, group_index, chromosome_index, value):
        self.solution[group_index][chromosome_index] = value
        

    
