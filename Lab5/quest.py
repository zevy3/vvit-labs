class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return 'Название книги: {}, Автор: {}, Год издания: {}'.format(self.title, \
                                                                       self.author, self.year)

book1 = Book('Робин Бобин',1984)

print(book1.get_info())
