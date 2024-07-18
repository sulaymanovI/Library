from book import Book

class Library:  # Создание Библиотеку

    def __init__(self) -> None: 
        self.books = []

    def add_book(self,title,author,year):  #Добавление книги
        new_book=Book(title,author,year)
        self.books.append(new_book)
        print("Книга добавлена успешно!")
    
    def remove_book(self,book_id):  #Удаление книги
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book_id)
                return "Книга удалена успешно!"
        print("Книга с таким ID не найдена.")
    
    def find_books(self,search_term):      #Поиск книги
        results=[book for book in self.books if \
        search_term.lower() in book.title.lower() \
        or search_term.lower() in book.author.lower() \
        or search_term == str(book.year)]
        
        if results:
            for book in results:
                print(book)
        else:
            print("Книги по вашему запросу не найдены.")
    
    def display_books(self):        #Отображение всех книг
        if not self.books:
            print("В библиотеке нет книг.")
        else:
            for book in self.books:
                print(book)
    
    def change_status(self,book_id , new_status):      #Изменение статуса книги
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                print("Статус книги обновлён!")
                return 
        print("Книга с таким ID не найдена.")


