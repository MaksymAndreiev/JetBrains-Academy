import os
import requests
import string
from bs4 import BeautifulSoup


class WebScraper:

    def __init__(self, base_url, pages_to_observe, type_of_art):
        self.base_url = base_url
        self.type_of_art = type_of_art
        self.pages_to_observe = pages_to_observe

    def complete_url_to_request(self, page_number):
        return self.base_url + f'/nature/articles?searchType=journalSearch&sort=PubDate&page={page_number+1}'

    def dir_make_and_proceed(self, page_number):
        os.mkdir(f'Page_{page_number + 1}')
        os.chdir(f'Page_{page_number + 1}')

    def return_to_parent_dir(self):
        os.chdir(os.path.dirname(os.getcwd()))

    def get_request(self, page_number):
        return requests.get(self.complete_url_to_request(page_number), headers={'Accept-Language': 'en-US,en;q=0.5'})

    def soup_from_main_pages(self, page_content):
        pass

    def change_article_name(self, word):
        list_from_article_letters = [letter for letter in word]
        for i in range(len(list_from_article_letters)):
            if list_from_article_letters[i] in string.punctuation:
                list_from_article_letters[i] = ''
            elif list_from_article_letters[i] == ' ':
                list_from_article_letters[i] = '_'
        return ''.join(list_from_article_letters)

    def write_text_from_data(self, data_text, file_name):
        # prepare fetched text to write
        full_text = ''
        for line in data_text:
            if line != '\n':
                full_text += line
        # write text in binary
        with open(f'{file_name}.txt', 'wb') as article_text:
            article_text.write(full_text.encode('UTF-8'))


nature_Scraper = WebScraper("https://www.nature.com", range(int(input())), input())

for page_n in nature_Scraper.pages_to_observe:
    nature_Scraper.dir_make_and_proceed(page_n)
    request_from_page = nature_Scraper.get_request(page_n)
    try:
        if request_from_page:
            soup = BeautifulSoup(request_from_page.content, 'html.parser')
            soup_articles_list = soup.findAll('article', {"class": "u-full-height c-card c-card--flush"})
            for article in soup_articles_list:
                article_link = article.find('a', {"class": "c-card__link u-link-inherit"})["href"]
                article_type = article.find('span', {"data-test": "article.type"}).text.strip()
                article_name = article.find('a', {"class": "c-card__link u-link-inherit"}).text.strip()

                # change article name according with requirements
                required_article_name = nature_Scraper.change_article_name(article_name)

                # follow by article link, fetch info
                if article_type == f'{nature_Scraper.type_of_art}':
                    url_to_follow = nature_Scraper.base_url + article_link
                    request_from_url_to_follow = requests.get(url_to_follow, headers={'Accept-Language': 'en-US,en;q=0.5'})
                    try:
                        if request_from_url_to_follow:
                            soup_from_url_to_follow = BeautifulSoup(request_from_url_to_follow.content, 'html.parser')
                            try:
                                article_text_unprepared = soup_from_url_to_follow.find('div', {"class": "article__body cleared"}).text
                            except AttributeError:
                                article_text_unprepared = soup_from_url_to_follow.find('div', {"class": "article-item__body"}).text

                            # write text to file
                            nature_Scraper.write_text_from_data(article_text_unprepared, required_article_name)
                        else:
                            print(f'The URL returned {request_from_url_to_follow.status_code}!')
                    except KeyError:
                        print(f'The URL returned {request_from_url_to_follow.status_code}!')
    except KeyError:
        print(f'The URL returned {request_from_page.status_code}!')
    finally:
        nature_Scraper.return_to_parent_dir()

print('Saved all articles.')

