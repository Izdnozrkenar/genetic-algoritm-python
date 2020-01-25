from book import Book, Covers, Papers, Fonts
from books_excel_helper import get_books_csv_data
from groups_excel_helper import get_groups_csv_data
from population import Population
import matplotlib.pyplot as plt

#get data from csv files 
books_data = get_books_csv_data()
groups_data = get_groups_csv_data()

#population size must be at least 2 
pop = Population(100,groups_data,books_data)

iterations = []
best_fitness_val = []

for i in range(20):
    iterations.append(i)
    pop.mutation(0.3)
    best_fitness_val.append(pop.best_genotype[1])

plt.plot(iterations,best_fitness_val)
plt.title('20 mutations', size=14)
plt.xlabel('iterations', size=14)
plt.ylabel('fitness value', size=14)
plt.savefig('plots/mutations.png', format='png')
