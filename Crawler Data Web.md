# Crawler Data Web

Nama			: Aisy Qonitah Suwardi

NRP		   	: 160411100015

Mata kuliah      	: Penambangan dan Pencarian Web

Jurusan	     	: Teknik Informatika

Dosen pengampu   : Mulaab, S.Si., M.Kom.



##### Langkah-Langkah Crawler Data pada Web

1. Install requests pada python menggunakan cmd

2. Install BeautifulSoup4 pada python menggunakan cmd

3. Kemudian cari website yang akan digunakan untuk diambil datanya

   > https://www.cottonink.co.id/shop/catalog/new/

4. Setelah itu code pada python akan disesuaikan.

   

##### Penjelasan Program Crawler Data

```python
	page = requests.get(src)
    soup = BeautifulSoup(page.content, 'html.parser')
```

Code diatas digunakan oleh program untuk mendownload data/kode html pada website kemudian diubah kedalam object yang ada di BeautifulSoup.



```python
content = soup.find(class_='product__list js-filter is-open')
producs = content.findAll(class_='product__main-img product__main-img1-4')
```

Code diatas digunakan untuk mempermudah area pencarian data yang akan diambil. Lebih tinggi tingkat akurasi lebih mudah data diambil.



```python
for baju in producs:
        judul = buku.find(class_='link link--nou product__name').getText()
        keterangan = buku.find(class_='product__shortdesc').getText()
        harga = buku.find(class_='product__price').getText()
```

Code diatas digunakan untuk mengambil data pada website.



```python
conn.execute("INSERT INTO BAJU \
                        VALUES ('%s', '%s', '%s')" %(judul, keterangan, harga));

```

Code diatas digunakan untuk menyimpan data yang telah diambil pada website ke database.



```python
conn = sqlite3.connect('test.db')
conn.execute('drop table if exists BAJU')
conn.execute('''CREATE TABLE BAJU
         (JUDUL          TEXT     NOT NULL,
         KETERANGAN       TEXT     NOT NULL,
         HARGA           TEXT     NOT NULL);''')
```

Code diatas digunakan untuk membuat database dan tabel untuk menampung data.