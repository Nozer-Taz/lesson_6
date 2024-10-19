

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.read = False
    
    def mark_as_read(self):
        self.read = True

    def mark_as_unread(self):
        self.read = False
    
    def __str__(self):
        return f"Title: {self.title} - {'read' if self.read else 'unread'}"

    def __repr__(self):
        return f"Title: {self.title} - {'read' if self.read else 'unread'}"


class Library:
    def __init__(self):
        self.books_list = []

    def add_book(self, other):
        self.books_list.append(other)
    


    def del_book(self, title):
        for i in self.books_list:
            if i.title == title:
                self.books_list.remove(i)
    
    def filter_by_status(self, status):
        read_books = []
        for i in self.books_list:
            if i.read:
                read_books.append(i)
        if len(read_books) == 0:
            return 'No read books.'
        else:
            for i in read_books:
                print(i)



    def list_books(self):
        for i in self.books_list:
            print(f'{i.title} -- {"read" if i.read else "unread"}')
    
    def find_by_title(self, title):
        
        for i in self.books_list:
            
            if i.title == title:
                return 'Book is listed in library.'
        return 'No such book.'
    
    def find_by_author(self, author):

        for i in self.books_list:
            
            if i.author == author:
                return f'{i.title} - {i.author}'
        return 'No such author'

    def mark_book_as_read(self, title):

        for i in self.books_list:
            if i.title == title:
                i.mark_as_read()
                break
        else:
            print('No such book in library')


# Выполнение кода
# 1. Реализуйте добавление новых книг в библиотеку.

library = Library()

book1 = Book('Wuthering heights', 'Emily Bronte', 1847)
book2 = Book('Crime and Punishment', 'Fedor Dostoyevky', 1866)
book3 = Book('The Master and Margarita', 'Mikhail Bulgakov', 1967)
book4 = Book('1984', 'George Orwell', 1949)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# 2. Реализуйте поиск книг по названию или автору.

library.find_by_title('Wuthering heights')

library.find_by_author('Mikhail Bulgakov')

# 3. Реализуйте возможность пометить книгу как прочитанную или непрочитанную.

library.mark_book_as_read('1984')

book1.mark_as_read()

# 3.5 Удаление книги и фильтрация по статусу

library.del_book('The Master and Margarita')
print(library.books_list)


library.filter_by_status('read')

# 4. Создайте интерфейс командной строки, который позволит пользователю управлять библиотекой

while True:
    command_input = input('What should we do, choose one of the following: list_all, book_info, mark_book_as_read, exit?\n')

    if command_input == 'list_all':
        library.list_books()

    elif command_input == 'book_info':
        book_name = input('Enter book title for info: ')
        for i in library.books_list:
            if i.title == book_name:
                print(i.title)
                print(i.author)
                print(i.year)

    elif command_input == 'mark_book_as_read':
        book_name = input('Enter book title to mark as read: ')
        library.mark_book_as_read(book_name)
        
    elif command_input == 'exit':
        break
