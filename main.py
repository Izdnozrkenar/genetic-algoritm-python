from book import Book, Covers, Papers, Fonts
from books_excel_helper import get_books_csv_data
from groups_excel_helper import get_groups_csv_data
from goal_function_helpers import goal_function

#get data from csv files 
books_data = get_books_csv_data()
groups_data = get_groups_csv_data()

