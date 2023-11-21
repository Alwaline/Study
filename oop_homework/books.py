class Book:
    def __init__(self, name: str, author: str, year_edition: str, page_number: int) -> None:
        '''Создает экземпляр класса "Book".
        Принимает: название книги, автор, год издания, количество страниц.'''

        self.__name__ = name
        self.__author__ = author
        self.__year_edition__ = year_edition
        self.__page_number__ = page_number


    def __str__(self) -> str:
        '''Позволяет печатать понятное представление.'''
        return '\n' + self.__name__ + ' ' + self.__author__ + ' ' + self.__year_edition__ + ' ' + str(self.__page_number__) + '\n'


    def get_information(self) -> str:
        '''Возвращает информацию о книге: название книги, автор, год издания, количество страниц.'''
        return f"""\nИнформация:\nКнига: {self.__name__};
Автор: {self.__author__}; 
Год издания: {self.__year_edition__};
Количество страниц: {self.__page_number__}\n"""
    

    def set_page_number(self, page_number: int):
        '''Устанавливает количество страниц книги.
        Принимает: количетсво страниц.'''
        self.__page_number__ = page_number


def main():
    IT = Book('IT', 'Stephen King', '2014', 800)
    print(IT.get_information())
    IT.set_page_number(837)
    print(IT.get_information())
    print(IT)

    M_a_M = Book('Мастер и Маргарита', 'Михаил Булгаков', '2007', 42)
    print(M_a_M.get_information())
    M_a_M.set_page_number(346)
    print(M_a_M.get_information())
    print(M_a_M)

if __name__ == "__main__":
    main()
        


        

