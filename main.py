from book import Book, Covers, Papers, Fonts
from books_excel_helper import get_books_csv_data
from groups_excel_helper import get_groups_csv_data
from population import Population

#get data from csv files 
books_data = get_books_csv_data()
groups_data = get_groups_csv_data()

#population size must be at least 2 
pop = Population(20,groups_data,books_data)

print(pop.best_genotype)
pop.tournament_crossing(3)
print(pop.best_genotype)
pop.mutation(0.3)
print(pop.best_genotype)
pop.random_crossing(2)
print(pop.best_genotype)
pop.mutation(0.7)
print(pop.best_genotype)
