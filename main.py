from book import Book, Covers, Papers, Fonts
from books_excel_helper import get_books_csv_data
from groups_excel_helper import get_groups_csv_data
from population import Population
from fittness_function_helpers import fittness_function

#get data from csv files 
books_data = get_books_csv_data()
groups_data = get_groups_csv_data()

pop = Population(5,groups_data,books_data)
#pop.print_population()

print(pop.best_genotype)
pop.mutation(0.9)
print(pop.best_genotype)