# TODO: Write a code that does everything in thoughts.md file

import json
import requests
from bs4 import BeautifulSoup


def main():
    manga_name: str = input("Enter Manga Name here: ")
    search_url = f"https://mangakakalot.com/search/story/{manga_name.replace(' ', '_')}"

    search_response: str = requests.get(url=search_url).text

    soup = BeautifulSoup(markup=search_response, features='html.parser')
    manga_soup = soup.find_all(name='div', attrs={'class': 'story_item'})
    if manga_soup != []:
        manga_data = []

        for manga in manga_soup:
            manga: BeautifulSoup = manga
            searchData = manga.find(name='h3', attrs={'class': 'story_name'})
            other_data = manga.findAll(name='span')
            
            manga_data.append({
                'name': searchData.getText().strip(),
                'preview_image': manga.find(name='img').get('src'),
                'manga_link': searchData.find(name='a').get('href'),
                'authors': other_data[0].getText().strip(),
                'updated': other_data[1].getText().strip(),
                'view': other_data[2].getText().strip(),
            })

        with open(file='data.json', mode='w') as f:
            f.write(json.dumps(obj=manga_data, indent=4))
    else:
        print("Manga not found")



if __name__ == "__main__":
    main()
