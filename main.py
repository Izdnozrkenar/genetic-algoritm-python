from book import Book, Covers, Papers, Fonts
from books_excel_helper import get_books_csv_data
from groups_excel_helper import get_groups_csv_data
from population import Population
import matplotlib.pyplot as plt

#get data from csv files 
books_data = get_books_csv_data()
groups_data = get_groups_csv_data()

#population size must be at least 2 
pop = Population(500,groups_data,books_data)

its = 10
best_fitness_val = []
av_fitness_val = []
iterations = []

for i in range(3):
    pop.roulette_selection()
    iterations.append(i)
    best_fitness_val.append(pop.best_genotype[1])
    av_fitness_val.append(pop.get_average_fitness_value())


for i in range(its):
    iterations.append(i+3)
    pop.tournament_crossing(40)
    best_fitness_val.append(pop.best_genotype[1])
    av_fitness_val.append(pop.get_average_fitness_value())

for i in range(3):
    pop.roulette_selection()
    iterations.append(i + 13)
    best_fitness_val.append(pop.best_genotype[1])
    av_fitness_val.append(pop.get_average_fitness_value())

for i in range(its):
    iterations.append(i+16)
    pop.tournament_crossing(4)
    best_fitness_val.append(pop.best_genotype[1])
    av_fitness_val.append(pop.get_average_fitness_value())

plt.step(iterations,best_fitness_val)
plt.step(iterations,av_fitness_val)
plt.title('Preselection and tournament crossing 20 groups', size=15)
plt.xlabel('iterations', size=15)
plt.ylabel('fitness value', size=15)
plt.savefig('plots/mutations.png', format='png')

