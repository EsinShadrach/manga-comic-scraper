import requests
import os
# manga_name = input("enter folder name>>> ")
manga_name = ""

page1 = "https://temp.compsci88.com/manga/Onepunch-Man/0165-001.png"
page_file_name1 = "1-2.png"

def manga_download(manga_name, filename, link):
    # try:
    #     os.mkdir(os.path.join(os.getcwd(), folder_name))
    # except:
    #     print("error while creating folder for " + folder_name)
    # os.chdir(os.path.join(os.getcwd(), folder_name))
    with open(filename, "wb") as f:
        image = requests.get(link)
        f.write(image.content)
        print("downloading... " + filename)
manga_download(manga_name, page_file_name1, page1)
