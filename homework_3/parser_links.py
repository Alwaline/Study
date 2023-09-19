with open('file.xml', 'r', encoding='utf-8') as file:
    lines = file.readlines()
c = 0 # Количество ссылок
for line in lines:
    if 'http' in line: # выводит и хттп и хттпс
        
        end_link = 0
        while line.find('http', end_link) != -1:        #шоб выводил все ссылки в строке, а то без этого только одну выводит
            start_link = line.find('http', end_link)

            # возможные концы ссылок
            if line[start_link - 1] == '"': 
                end_link = line.find('"', start_link)
            elif line[start_link - 1] == ' ':
                end_link = line.find(' ', start_link)
            else:
                end_link = line.rfind('<')

            c += 1
            print(line[start_link:end_link])

print('\nВсего ссылок найдено: ', c)
        
