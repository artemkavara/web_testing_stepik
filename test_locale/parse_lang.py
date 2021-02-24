#imports
import requests
from bs4 import BeautifulSoup

#get link to parse list of languages
url = "http://selenium1py.pythonanywhere.com/en-gb/"

#set up parser
r = requests.get(url)
soup = BeautifulSoup(r.text)

#get list of available languages
list_lang_html = soup.find_all("option")
list_lang = [line["value"] for line in list_lang_html]

#write languages in file
with open("list_lang.txt", "w") as f:
    for lang in list_lang:
        f.write(lang+"\n")