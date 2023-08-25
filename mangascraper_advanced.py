import requests as re
import os
source_list = [
    "https://scans-hot.leanbox.us/manga/Boku-No-Hero-Academia/0359-001.png use this one for mangas at times",
    "https://scans-hot.leanbox.us/manga/Onepunch-Man/0166-001.png",
    "https://temp.compsci88.com/manga/Boku-No-Hero-Academia/0360-001.png",
    "https://cdn.black-clover.org/file/sugois/boruto/Chapter-71/01.jpg",
    "https://official-other.orience.us/manga/The-God-Of-High-School/0112-004.png",
    "https://temp.compsci88.com/manga/Boku-No-Hero-Academia/0366-002.png",
    "https://scans-hot.leanbox.us/manga/Boku-No-Hero-Academia/0367-001.png"
]
prename = "my hero academia"
postname = prename.replace(" ", "-")
manganame = postname.title()
# chapter_num = int(input("enter chapter number>>"))
chapter_num = 367
lim = 18

try:
    os.mkdir(os.path.join(os.getcwd(), f"{manganame}-{chapter_num}"))
except:
    print(f"error while creating folder for {chapter_num}")
os.chdir(os.path.join(os.getcwd(), f"{manganame}-{chapter_num}"))

def manga_downloader():
    page_number = 0
    page_name = 0
    while page_name < lim:
        page_number += 1
        page_name += 1
        with open(f"actual {manganame}-{chapter_num}-{page_name}.png", "wb") as f:
            if page_number < 10:
                image = re.get(
                    f"https://scans-hot.leanbox.us/manga/Boku-No-Hero-Academia/0367-00{page_number}.png"
                    )
                f.write(image.content)
                print(f"Downloading {manganame}-{chapter_num}-{page_name}.png....")
            elif page_number in range(10, 100):
                image = re.get(
                    f"https://scans-hot.leanbox.us/manga/Boku-No-Hero-Academia/0367-0{page_number}.png"
                    )
                f.write(image.content)
                print(f"Downloading {manganame}-{chapter_num}-{page_name}.png....")
            elif page_number in range(100, lim + 1):
                image = re.get(
                    f"https://temp.compsci88.com/manga/Boku-No-Hero-Academia/0366-00{page_number}.png"
                    )
                f.write(image.content)
                print(f"Downloading {manganame}-{chapter_num}-{page_name}.png....")


manga_downloader()
a = manga_downloader()
