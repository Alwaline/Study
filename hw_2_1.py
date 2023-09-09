DICT_MORZE = morse_alphabet = {
    'а': '.-',
    'б': '-..',
    'в': '.--', 
    'г': '--.', 
    'д': '-..', 
    'е': '.', 
    'ё': '.', 
    'ж': '...-',
    'з': '--..', 
    'и': '..', 
    'й': '.---', 
    'к': '-.-', 
    'л': '.-..', 
    'м': '--', 
    'н': '-.', 
    'о': '---', 
    'п': '.--.', 
    'р': '.-.', 
    'с': '...', 
    'т': '-', 
    'у': '..-', 
    'ф': '..-.', 
    'х': '....', 
    'ц': '-.-.',
    'ч': '---.', 
    'ш': '----', 
    'щ': '--.-', 
    'ъ': '--.--', 
    'ы': '-.--', 
    'ь': '-..-', 
    'э': '..-..', 
    'ю': '..--', 
    'я': '.---', 
    ' ': '    '}

print('''
    Программа преобразует вводимую строку в шифр азбуки Морзе.
    На вход принимает строку без знаков препинания.
    Выводит шифр.
''')



text = input('Введите строку: ').lower()
new_text = ''
print('')
for sing in text:
    new_text += DICT_MORZE.get(sing, '    ') + ' '

print(new_text)

input('\nНажмите Enter, чтобы выйти...')
