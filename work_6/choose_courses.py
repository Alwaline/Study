courses = {
    'ml': {
        'available' : 10,
        'average_mark': 80 
    },
    'django': {
        'available' : 15,
        'average_mark': 60 
    },
    'philosophy': {
        'available' : 20,
        'average_mark': 0
    },
}

menu = '''
Меню:
1. Выбрать курс
2. Посмотреть распределение
3. Посмотреть список курсов
'''



chart_student = []



def check_available(course = None):
    if course is None:
        return courses['ml']['available'] + courses['django']['available'] + courses['philosophy']['available']
    return courses[course]['available']


def get_average(scores):
    return sum(scores) // len(scores)


def add_record(course, student):
    chart_student.append((student, course))
    courses[course]['available'] -= 1
    print(f'\nВы были добавлены на курс {course}')


def choose_cours():
    
    student = input("\nВведите своё имя: ")
    student += ' гр. ' + input("Введите номер группы: ")
    score = list(map(int, input('Введите оценки по предметам через пробел (5 штук): ').split()))

    if len(score) < 5:
        print("Что-то мало оценок 🗿")
        return

    average_score = get_average(score)

    print('\nДоступные для вас курсы:\n')
    
    n = 1
    access_courses = dict()

    for key in courses.keys():
        available = check_available(key)
        if courses[key]['average_mark'] < average_score and available:
            print(f'{n}. Курс {key}, свободных мест: {available}')
            access_courses[n] = key
            n += 1
    
    choose = int(input('\nВыберите курс по выбору: '))
    add_record(access_courses[choose], student)
    input('\nНажмите Enter, чтобы продолжить...')


def print_chooses():
    print('\nСписок распределенных студентов:\n')
    for num, respond in enumerate(chart_student):
        print(f'{num+1}. Студент: {respond[0]}; Курс: {respond[1]}')
    input('\nНажмите Enter, чтобы продолжить...')


def print_all_courses():
    n = 1
    print('\n Список всех курсов:\n')
    for name, course in courses.items():
        print(f'{n}. Курс: {name}; Средний балл для зачисления: {course["average_mark"]}; Количество свободных мест: {course["available"]}')
        n += 1
    input('\nНажмите Enter, чтобы продолжить...')


command = {

    '1': choose_cours,
    '2': print_chooses,
    '3': print_all_courses
}


def main():
    
    while check_available():

        print(menu)

        choose = input()
        if choose:
            command[choose]()
        else:
            break

    else:
        print('Места на курсах по выбору закончились')


if __name__ == "__main__":
    main()