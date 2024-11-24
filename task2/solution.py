"""
Задание 2:
Необходимо реализовать скрипт, который будет получать с
русскоязычной википедии список всех животных
(https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту)
и записывать в файл в формате beasts.csv количество животных на каждую букву алфавита.
Содержимое результирующего файла:
А,642
Б,412
В
Примечание:
анализ текста производить не нужно, считается любая запись из категории
(в ней может быть не только название, но и, например, род)
"""

import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict

def get_animals_count():
    base_url = "https://ru.wikipedia.org"
    url = base_url + "/wiki/Категория:Животные_по_алфавиту"
    animals_count = defaultdict(int)

    while True:
        response = requests.get(url)

        # Проверка успешности запроса
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from Wikipedia. Status code: {response.status_code}")

        soup = BeautifulSoup(response.content, 'html.parser')

        # Поиск всех ссылок на животных
        links = soup.select('div.mw-category-group a')

        for link in links:
            text = link.text.strip()
            if text and text[0].isalpha():  # Проверяем, что текст не пуст и начинается с буквы
                first_letter = text[0].upper()
                animals_count[first_letter] += 1

        # Поиск ссылки на следующую страницу
        next_page = soup.find('a', string='Следующая страница')
        if next_page:
            url = base_url + next_page['href']  # Обновляем URL на следующую страницу
        else:
            break  # Если нет следующей страницы, выходим из цикла

    # Запись данных в CSV файл
    with open('beasts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for letter in sorted(animals_count.keys()):
            writer.writerow([letter, animals_count[letter]])

if __name__ == "__main__":
    get_animals_count()