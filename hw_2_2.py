print('''
    Программа считывает данные с csv-файла и считает количество выживших мужчин и женщин.
''')
count_m = 0
count_f = 0
with open('train.csv', 'r') as file:
    file.readline()

    while s:= file.readline():
        surv = s[s.find(',')+1] == '1'
        if surv:
            count_m += s.find('male') > 0
            count_f += s.find('female') > 0
    

print('Количество выживших мужчин = ', count_m)
print('Количество выживших женщин = ', count_f)



input('\nНажмите Enter, чтобы выйти...')