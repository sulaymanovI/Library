
class Book:         #Создать Одну Книгу

    _id_counter=1

    def __init__(self, title , author , year) -> None:    #Инициализирование атрибутов
    
        self.id = Book._id_counter
        Book._id_counter+=1
        self.title=title
        self.author = author
        self.year = year
        self.status="В наличии"
    
    def __str__(self) -> str:
        return f"\nID : {self.id}\nНазвания : {self.title}\
        \nГод выпуска : {self.year}\nАвтор : {self.author}\
        \nСтатус : {self.status}"
    