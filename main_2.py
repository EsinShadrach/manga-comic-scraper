# TODO: Write a code that does everything in thoughts.md file

import requests
from bs4 import BeautifulSoup


def main():
    manga_name: str = input("Enter Manga Name here: ")
    # ! ADD BLOCK FOR URL FORMATTING: " " -> % AND STUFF LIKE THAT
    search_url: str = f'https://mangasee123.com/search/?name={manga_name.replace(" ", "%")}'
    # ! ADD TRY CATCH BLOCK BASED ON STATUS CODE
    # search_response: str = requests.get(search_url).text
    print(search_url)


if __name__ == "__main__":
    main()
