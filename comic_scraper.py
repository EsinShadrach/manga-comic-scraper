import requests as re
import pyttsx3 as tts
# https://scans-hot.leanbox.us/manga/Boku-No-Hero-Academia/0359-001.png use this one for mangas at times
# https://scans-hot.leanbox.us/manga/Onepunch-Man/0166-001.png
# https://temp.compsci88.com/manga/Boku-No-Hero-Academia/0360-001.png
# https://official-other.orience.us/manga/The-God-Of-High-School/0112-004.png
prename = "god of high school"
postname = prename.replace(" ", "-")
manganame = postname.title()
chapter_num = int(input("enter chapter number>>"))
lim = 60

def manga_downloader_edited():
    page_number = 0
    page_name = 0
    while page_name < 60:
        page_number += 1
        page_name += 1
        with open(f"{manganame}_{chapter_num}_{page_name}.png", "wb") as f:
            if page_number < 10:
                image = re.get(
                    f"https://official-other.orience.us/manga/The-God-Of-High-School/0{chapter_num}-00{page_number}.png"
                    )
                f.write(image.content)
                print(f"Downloading {manganame}_{chapter_num}_{page_name}.png....")
            elif page_number in range(10, 100):
                image = re.get(
                    f"https://official-other.orience.us/manga/The-God-Of-High-School/0{chapter_num}-0{page_number}.png"
                    )
                f.write(image.content)
                print(f"Downloading {manganame}_{chapter_num}_{page_name}.png....")
            elif page_number in range(100, lim + 1):
                image = re.get(
                    f"https://official-other.orience.us/manga/The-God-Of-High-School/0{chapter_num}-{page_number}.png"
                    )
                f.write(image.content)
                print(f"Downloading {manganame}_{chapter_num}_{page_name}.png....")


manga_downloader_edited()
