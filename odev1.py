import requests
from bs4 import BeautifulSoup

dosya = open("common.txt", "r")

oku = dosya.read().splitlines()

for i in range(4614):
    
    urlalp = "https://alperenkayademir.com/" + oku[i]
    r = requests.get(urlalp)
    if (r.status_code==200):
        print(urlalp)


"""
C:\CASPER\AppData\Local\Programs\Python\Python38-32\python.exe C:/Users/CASPER/Desktop/Phyton/odev1.py
https://alperenkayademir.com/
https://alperenkayademir.com/admin
https://alperenkayademir.com/controlpanel
https://alperenkayademir.com/cpanel
https://alperenkayademir.com/index.html
https://alperenkayademir.com/index.php
https://alperenkayademir.com/pipermail
https://alperenkayademir.com/robots.txt
https://alperenkayademir.com/webmail

Process finished with exit code 0
"""