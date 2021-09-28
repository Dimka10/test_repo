books = {'Сияние': 'Стивен Кинг', 'Гроза': 'А.Н.Островский', 'Перси Джексон': 'Рико Риордан'}
readers = {}
def get_info():
    global readers
    global books
    print(f'Список читателей на данный момент такой: {readers}')
    print(f'Список книг такой: {books}')
def manager():
    global books
    print(f'Какую книгу вы хотите получить? Выберите из: {books}')
    book = input('Введите только название книги: ')
    name = input('Введите ваше имя: ')
    global readers
    if name in readers:
        print('Заявка уже оформлена!')
    else:
        readers[name] = book
        print('Ваша заявка успешно оформлена!')
# def manager():
    # global books
# def get_info():
#     pass
get_info()
manager()




