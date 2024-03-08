import os
import json
import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--url", help="Direct link to manga")
args = parser.parse_args()


def main():
    if args.url:
        get_chapters(manga_url=args.url)
    else:
        manga_name: str = input("Enter Manga Name here: ")
        base_url = "https://mangakakalot.com/search/story"
        search_url = f"{base_url}/{manga_name.replace(' ', '_')}"

        search_response: str = requests.get(url=search_url).text

        soup = BeautifulSoup(markup=search_response, features='html.parser')
        manga_soup = soup.find_all(name='div', attrs={'class': 'story_item'})
        if manga_soup != []:
            manga_data = []

            for manga in manga_soup:
                manga: BeautifulSoup = manga
                searchData = manga.find(
                    name='h3', attrs={'class': 'story_name'})
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

            print("Found Manga's: \n")

            for index, i in enumerate(iterable=manga_data, start=1):
                print(f"{index}. {i['name']}\n")

            selected = input("Select A Manga >> ")
            limit = len(manga_data)

            if selected.isdigit() and int(selected) <= limit:
                print('\n')
                get_chapters(
                    manga_url=manga_data[int(selected) - 1]['manga_link'])

            elif selected.isdigit() and int(selected) > limit:
                print('Pick a number In the range!!')

            else:
                print('Pick a number!!')

        else:
            print("Manga not found")


def get_chapters(manga_url: str):
    manga_response = requests.get(url=manga_url).text
    soup = BeautifulSoup(markup=manga_response, features='html.parser')
    chapters_list = soup.find(
        name='ul',
        attrs={
            'class': 'row-content-chapter'
        }
    )

    chapters_list = []

    chapters = soup.find_all(name='li', attrs={'class': 'a-h'})

    for index, i in enumerate(iterable=chapters, start=1):
        chapter_name = i.find(name='a').getText().strip()

        data = {
            'id': len(chapters) - index + 1,
            'chapter_name': chapter_name,
            'link': i.find(name='a').get('href'),
            'views': i.find(name='span', attrs={'class': 'chapter-view'})
            .getText().strip(),
            'released': i.find(name='span', attrs={'class': 'chapter-time'})
            .getText().strip()
        }
        chapters_list.append(data)

    with open(file='data2.json', mode='w') as f:
        f.write(json.dumps(obj=chapters_list, indent=4))

    for i, index in enumerate(iterable=chapters_list, start=1):
        print(f"{i}. {index['chapter_name']}\n")

    selected = input("Select A Chapter >> ")
    limit = len(chapters_list)
    hint_text = f"(1 for most recent and {len(chapters_list)} for last)"
    print(
        f"HINT: Enter the number of the chapter you want to read {hint_text}"
    )

    if selected.isdigit() and int(selected) <= limit:
        print('\n')
        downloadManga(
            manga_name=chapters_list[int(selected) - 1]['chapter_name'],
            url=chapters_list[int(selected) - 1]['link'],
            chapter_num=chapters_list[int(selected) - 1]['id']
        )

    elif selected.isdigit() and int(selected) > limit:
        print('Pick a number In the range!!')
    else:
        print('Pick a number!!')


def downloadManga(manga_name, url, chapter_num):
    response = requests.get(
        url=url, headers={'Referer': 'https://chapmanganato.com/'}).text
    soup = BeautifulSoup(markup=response, features='html.parser')

    image_parent = soup.find(
        name='div',
        attrs={
            'class': 'container-chapter-reader'
        }
    )

    image_list = []

    image_and_index = enumerate(
        iterable=image_parent.find_all(name='img'),
        start=1
    )

    for index, image in image_and_index:
        data = {
            'page_name': index,
            'link': image.get('src')
        }
        image_list.append(data)

    for image in image_list:
        page_name = image['page_name']
        link = image['link']
        image_response = requests.get(
            url=link, headers={'Referer': 'https://chapmanganato.com/'})
        if image_response.status_code == 200:
            write_text = f"downloads/{manga_name}-{chapter_num}-{page_name}"

            with open(f"{write_text}.jpg", mode='wb') as file:
                file.write(image_response.content)
                print(
                    f"Downloaded {manga_name}-{chapter_num}-{page_name}.jpg..."
                )
        else:
            failed_name = f"{manga_name} - {chapter_num} - {page_name}.jpg..."
            print(
                f"Failed to download {failed_name}"
            )


if __name__ == "__main__":
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    main()
