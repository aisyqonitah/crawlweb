import requests
from bs4 import BeautifulSoup
import sqlite3

def crawl (src):
    '''
        Function ini berguna untuk web crawling
        src = (string) berupa url web yang akan di crawl
    '''
    #Download html dari web
    page = requests.get(src)

    #Mengubah html ke object beautiful soup
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find(class_='product__list js-filter is-open')

    producs = content.findAll(class_='product__main-img product__main-img1-4')

    for baju in producs:
        judul = buku.find(class_='link link--nou product__name').getText()
        keterangan = buku.find(class_='product__shortdesc').getText()
        harga = buku.find(class_='product__price').getText()
        conn.execute("INSERT INTO BAJU \
                        VALUES ('%s', '%s', '%s')" %(judul, keterangan, harga));

   


conn = sqlite3.connect('test.db')
conn.execute('drop table if exists BAJU')
conn.execute('''CREATE TABLE BAJU
         (JUDUL          TEXT     NOT NULL,
         KETERANGAN       TEXT     NOT NULL,
         HARGA           TEXT     NOT NULL);''')

src = 'https://www.cottonink.co.id/shop/catalog/new/'

crawl(src)
conn.commit()
cursor = conn.execute("SELECT * from BAJU")

for row in cursor:
    print(row)
