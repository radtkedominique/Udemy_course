import requests
from bs4 import BeautifulSoup
from time import sleep
import csv
from random import choice

all_quotes = []
base_url = 'http://quotes.toscrape.com'
url = '/page/1'

while url:

    res = requests.get(base_url + url)
    print(f'Now scraping {base_url}{url}...')
    soup = BeautifulSoup(res.text, 'html.parser')
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
        all_quotes.append({
            'text' : quote.find(class_='text').get_text(),
            'author' : quote.find(class_='author').get_text(),
            'bio-link' : quote.find('a')['href']
        })

    next_btn = soup.find(class_='next')
    url = next_btn.find('a')['href'] if next_btn else None
    sleep(1) #to not be caught

#create file where quote dict is saved
with open('quotes.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=['text', 'author', 'bio-link'])
    writer.writeheader()
    writer.writerows(all_quotes)

#access quotes through file not scraping
quotes_all = []
with open('quotes.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        quotes_all.append(row)


#game-logic
quote = choice(quotes_all)
print(quote['text'])
print(quote['author'])

remaining_guesses = 4
guess = ''
while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
    guess = input(f'Wo said this quote? Guesses remaining: {remaining_guesses}')
    remaining_guesses -= 1
    if remaining_guesses == 3:
        res = requests.get(f'{base_url}{quote['bio-link']}')
        soup = BeautifulSoup(res.text, 'html.parser')
        birth_date = soup.find(class_='author-born-date').get_text()
        birth_place = soup.find(class_='author-born-location').get_text()
        print(f'Here is a hint: The author was born on {birth_date} in {birth_place}')
print('After while loop')

