### Nayla Farah Nida
### 2306213426

My Project: 

(Librarree Books)[http://nayla-farah-librarreebooks.pbp.cs.ui.ac.id/]

<details>
  <summary>Tugas 6: JavaScript dan AJAX</summary>

1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
   
- JavaScript selalu dieksekusi di lingkungan klien sehingga mengurangi beban server dan mempercepat proses eksekusi.
  
- Kompatibel untuk semua browser.
  
- Membuat website yang interaktif dan responsif.
  
- JavaScript fleksibel untuk front-end maupun back-end dengan adanya Node.js
  
- Dapat digunakan pada berbagai framework dan library.
  
2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
   
Fungsi dari await adalah menunggu hingga fetch() selesai, baik hasilnya berhasil mendapat data atau gagal. 

Setelah promise terpenuhi, response bisa langsung digunakan di baris kode berikutnya.

Jika tidak menggunakan await, fetch akan berjalan secara asynchronous dan langsung mengembalikan promise tanpa menunggu sampai selesai melakukan permintaan, sehingga response dari server mungkin belum tersedia saat kode berikutnya dieksekusi.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

@csrf_exempt digunakan untuk mengecualikan pengecekan CSRF pada view tertentu, sehingga memungkinkan AJAX POST tanpa token CSRF. Kita sudah pastikan bahwa permintaan POST berasal dari source yang terpecaya dan API atau endpoint khusus tidak mengubah data penting, oleh karena itu decorartor ini digunakan karena penggunaan CSRF dianggap tidak perlu.

*Kenapa perlu menggunakan @crsf_exempt?*

- Penggunaan @csrf_exempt memungkinkan permintaan AJAX POST dilakukan tanpa perlu mengirimkan token CSRF, sehingga memudahkan pengembangan API.
  
- Tanpa @csrf_exempt, permintaan POST tanpa token CSRF akan menghasilkan 403 Forbidden dari Django, karena Django tidak menerima token valid dari permintaan tersebut.
  
- Dengan @csrf_exempt, kita menghindari kompleksitas pada integrasi dengan front-end, dengan melewatkan langkah tambahan untuk menangani token CSRF secara manual, terutama jika view tersebut tidak mengubah data penting atau sensitif.

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Data yang dikirimkan dari frontend ke backend bisa dimanipulasi oleh pengguna atau pihak ketiga sebelum sampai ke server. Bahkan jika kita memiliki validasi di frontend, seorang pengguna bisa mengabaikan atau menghapus validasi tersebut (misalnya, menggunakan developer tools atau mengirim permintaan langsung ke server melalui API tanpa melibatkan UI). Oleh karena itu, pembersihan di backend memberikan lapisan keamanan tambahan yang tidak bisa dilewati.

5. Cara implementasi tugas:

- Membuat fungsi ```add_book_entry_ajax``` di ```views.py``` yang mengembalikan response JSON untuk data.
- Membuat fungsi untuk refresh produk.
- Membuat fungsi untuk mengirim AJAX ```GET``` request dengan JavaScript untuk fetch data.
- Menambahkan tombol di ```main.html``` sebagai trigger untuk show modal.
- Membuat fungsi untuk show modal dan hide modal.
- Membuat fungsi untuk handle submission form dan mengirim ```POST``` request lewat AJAX, kemudian refresh display produk tanpa harus refresh satu page.
  
</details>

<details>
<summary>Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS</summary>

## Urutan prioritas CSS selector:

1. Inline style = 1000

``` 
<h1 style="color: purple;">Judul</h1>
```

3. ID selector = 100

```
#header {
  background-color: yellow;
}
```

5. Class, pseudo-classes, attribute selector = 10

```
.highlight {
  color: green;
}

a:hover {
  color: red;
}

input[type="text"] {
  border: 1px solid black;
}
```
7. Elements and pseudo-elements selector = 1

```
body {
  color: blue;
}
```

## Pentingnya responsive design dan contoh aplikasinya:

Responsive design adalah teknik merancang website, dimana website tersebut secara otomatis dapat menyesuaikan skala konten dan elemennya dengan ukuran layar yang digunakan user untuk membuka website, sehingga struktur dan tampilan website tetap rapih dan enak dilihat.

Mengapa responsive design penting?
Tujuan utama dari responsive design adalah untuk menghindari membuat ulang design website untuk setiap perangkat. Dengan responsive design, kita dapat meningkatkan user experience, meningkatkan peringkat dalam SEO (search engine operation), dan yang paling penting menghemat biaya dan Waktu pengembangan.

Contoh aplikasi yang sudah menerapkan responsive design:
Youtube,Google, X, 
Contoh aplikasi yang belum menerapkan responsive design:
MY APP LMAO

## Perbedaan antara margin, border, dan padding:

![css-box-model](https://github.com/user-attachments/assets/60a691ed-a593-4fa9-9c5b-8a9fd24a55b5)

Content - dapat berupa teks atau foto
Padding - area kosong (transparan) disekitar content
Border - Batasan yang mengelilingi padding dan content
Margin - area kosong (transparan) diluar border

```
div {
  /* width | style | color */
  border: 15px solid green;

  /* top | right | bottom | left */
  padding: 25px 50px 75px 100px;

  /* top | right | bottom | left */
  margin: 25px 50px 75px 100px;
}
```

## Flexbox vs Grid:

![grid_flex](https://github.com/user-attachments/assets/d3377422-e159-40cf-9c2f-40afb9abd8fc)

*Flexbox*:
Sistem layout satu dimensi untuk mengatur elemen dalam baris atau kolom

Properti flexbox:
1. display: flex;
2. flex-direction: (```row``` atau ```column```);
3. justify-content (```flex-start```, ```flex-end```, ```center```, ```space-betweem```, ```space-around```)
4. align-items (```flex-start```, ```flex-end```, ```center```,```baseline```,```stretch```)
5. flex-wrap (```nowrap```, ```wrap```, ```wrap-reverse```)

```
.container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
```

*Grid*:
Merupakan layout dua dimensi dengan baris dan kolom, dimana elemen diposisikan seperti tabel. 

Properti grid:
1. display: grid;
2. grid-template-columns atau grid-template-rows
3. gap
4. grid-column grid-row
5. justify-items dan align-items
6. grid-auto-rows dan grid-auto-columns

```
.container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 20px;
}
```

Kapan harus menggunakan flexbox atau grid:
*Flexbox* : Ketika tata letak bersifat linear, seperti navbar, daftar produk, atau untuk mengatur elemen lain dalam satu baris atau kolom.
*Grid* : Ketika tata letak bersifat dua dimensi, seperti halaman yang penuh dengan beberapa kolom dan baris.

Keduanya sering digunakan bersama, grid untuk membuat struktur layout utama, dan flexbox untuk mengatur detail dalam setiap elemen grid.

## Cara implementasi tugas:

- Framework yang saya gunakan untuk kustmoisasi halaman login, register, tambah produk, dan main adalah Tailwind.

- Mengatur static files di settings.py, kemudian membuat directory static untuk menyimpan CSS dam image.

- Buat navbar menggunakan Tailwind CSS yang secara otomatis berubah bentuk (collapsed) pada ukuran layar yang lebih kecil.

- Gunakan grid layout dan flexbox untuk memastikan produk-produk dalam card bisa diatur ulang sesuai ukuran layar. Atur penggunaan gambar, padding, dan margin agar proporsional di berbagai resolusi layar.

</details>

<details>
<summary>Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django</summary>

## Perbedaan antara HttpResponseRedirect dan redirect

```HttpResponseRedirect()``` hanya dapat mengambil argumen berupa URL, sedangkan ```redirect``` dapat menerima argumen berupa model, view, atau URL. '''Redirect()''' lebih fleksibel dalam hal apa yang dapat dialihkan karena dapat menerima argumen yang lebih beragam. 

## Cara kerja penghubungan model Product dengan User:

Django memiliki model pengguna bawaan yang disebut User, yang dapat diimpor dari django.contrib.auth.models. Model ini mewakili pengguna yang terdaftar di sistem.
Relasi antara model Product dan User dibuat dengan menambahkan ForeignKey di model Product, yang menghubungkan setiap entri produk ke satu pengguna.

```user = models.ForeignKey(User, on_delete=models.CASCADE)```

```on_delete=models.CASCADE```: Parameter ini menentukan apa yang akan terjadi jika pengguna dihapus. Dengan CASCADE, jika pengguna dihapus, semua produk yang terkait dengan pengguna tersebut juga akan dihapus secara otomatis.

*Cara Kerja di Database*
Setiap produk akan memiliki kolom user_id (secara default) yang akan menyimpan ID dari pengguna yang terkait dengan produk tersebut. Ini akan berfungsi sebagai Foreign Key di level database. Dengan hubungan ini, kita bisa mengakses peoduk berdasarkan pengguna
```
# Mendapatkan user dengan id
user = User.objects.get(id=2)

# Mendapatkan produk yang dimiliki user
user_products = Product.objects.filter(user=user)

# Menampilkan semua produk yang dimiliki user
for product in user_products:
    print(product.name)
```

## Perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? dan bagaimana Django mengimplementasikan kedua konsep tersebut:

```authentication```adalah proses memverifikasi identitas user, sedangkan ```authorization``` adalah proses memverifikasi apa saja yang dapat diakses oleh user tersebut.

Contoh authentication: Saat login,  user memasukkan username dan password. Kemudian sistem membandingkan informasi yang diberikan user dengan data yang tersimpan di database.

Contoh authorization: Setelah login, Django menentukan apa saja yang bisa dilakukan oleh user tersebut. Misal, hanya admin yang dapat menambah atau menghapus produk.

## Cara Django mengingat pengguna yang telah login, kegunaan lain dari cookies, dan apakah semua cookies aman digunakan?:

Django mengingat pengguna yang telah login menggunakan *session*. Setelah pengguna berhasil login, Django membuat session untuk user tersebut dan menyimpannya di database (atau media penyimpanan lain, seperti cookies atau cache), sehingga user tidak perlu login ulang selama sesi masih berlaku.

Pada tigas ini, kita menggunakan cookies untuk mengingat iformasi user. Selain itu, cookies dapat berguna untuk menyimpan preferensi user, melacak aktivitas user, menyimpan data keranjang belanja, dan mencegah Serangan CSRF (Cross-Site Request Forgery) dengan menyimpan crsf_token di cookies. Namun, tidak semua cookies aman, terutama jika tidak dienkripsi atau jika digunakan oleh pihak ketiga untuk pelacakan tanpa sepengetahuan pengguna. 

## Cara implementasi tugas:

- Membuat fungsi login, register, dan logout di ```views.py```. Kemudian import dan daftarkan di urlpatterns urls.py.

- Merestriksi ```main.html``` dengan decorator ```@login_required``` sehingga user berada di login form (login.html) dahulu. Opsi register ditunjukkan di login form, sedangkan opsi logout berupa tombol di ```main.html```.
  
- Menghubungkan model dengan user, dengan cara menambahkan model user:
```user = models.ForeignKey(User, on_delete=models.CASCADE)```

Supaya main page hanya menampilkan produk yang dimiliki user, ubah fungsi ```show_main``` dari:
```book_entries = Book.objects.all()```

menjadi:
```book_entries = Book.objects.filter(user=request.user)```
</details>

<details>
<summary>Tugas 3: Implementasi Form dan Data Delivery pada Django</summary>

## Mengapa implementasi data delivery dalam platform diperlukan:

Data delivery berguna dalam proses menerima, mengirim, dan memproses data. Data delivery memungkinkan platform berfungsi secara efisien, aman, dan dapat diakses, untuk mendukung operasional dan memberikan ‘user experience’ yang baik kepada para pengguna.

## Mengapa JSON lebih populer dibandingkan XML:

XML lebih baik digunakan ketika kita membutuhkan struktur data yang kompleks. Menurut saya, lebih baik menggunakan JSON karena sintaksnya lebih sederhana, lebih efisien, lebih mudah digunakan dalam aplikasi web, dan lebih kompatibel dengan bahasa pemrograman modern (Python, Javascript, Java). Hal lain yang membuat JSON lebih populer adalah JSON dioptimalkan untuk web karena merupakan bagian dari ekosistem JavaScript. JSON juga mendukung API web karena JSON adalah format utama yang digunakan dalam API RESTful.

## Fungsi method is_valid() pada form Django:

Method is_valid() berfungsi untuk memvalidasi data yang diisi oleh pengguna dalam form, dan memastikan bahwa data yang diterima memenuhi semua kriteria validasi yang ditentukan sebelum data tersebut diproses lebih lanjut. Kita butuh method ini untuk membantu menjaga integritas data, keamanan, dan pengalaman pengguna dalam aplikasi.

## Fungsi csrf_token saat membuat form Django:

Kita membutuhkan csrf_token  saat membuat form di Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery), yang merupakan salah satu jenis serangan keamanan di mana penyerang mencoba memaksa pengguna untuk mengirim permintaan berbahaya ke server tanpa sepengetahuan atau izin mereka. 

Penyerang dapat memanfaatkan fakta bahwa pengguna sudah login ke suatu aplikasi untuk melakukan aksi atas nama mereka. Sebagai contoh, jika pengguna sudah login ke aplikasi perbankan, penyerang dapat memaksa transfer dana melalui permintaan POST palsu yang dikirim tanpa disadari oleh pengguna.

Tanpa csrf_token, aplikasi Django akan rentan terhadap serangan CSRF. Penyerang dapat membuat permintaan palsu yang tampaknya datang dari pengguna yang valid dan mengirimkan aksi berbahaya ke server, seperti mengganti data atau menghapus akun pengguna.

## Cara implementasi tugas:

- Untuk membuat form, dalam file forms.py, saya membuat struktur form baru yang menerima data 'name', 'author', 'price', dan 'image', dengan Book sebagai model.

- Kemudian, di views.py, saya membuat fungsi baru bernama create_book_entry dengan parameter request dan membuat instance form BookEntryForm. Di dalam fungsi terdapat conditional untuk memeriksa apakah form valid (is_valid()) dan apakah request method adalah POST, yang menandakan bahwa pengguna telah mengirimkan form. Jika keduanya terpenuhi, data yang diisi di form akan diarahkan (redirect) ke halaman main.

- Setelah membuat fungsi create_book_entry, fungsi tersebut di import ke urls.py dan menambahkannya ke urlpatterns supaya bisa diakses.

- Untuk membuat fungsi yang dapat menampilkan objek dalam format JSON dan XML, saya perlu mengambil semua objek dari model (BookEntry.objects.all()), kemudian melakukan serialisasi ke format JSON dan XML menggunakan serializers.

- Fungsi untuk menampilkan objek berdasarkan ID menggunakan get(pk=id) kemudian serialisasikan objek tersebut.

- Setelah membuat fungsi di views.py, saya menambahkan URL routing untuk setiap fungsi di urls.py.

### Screenshot Postman 
**JSON**
![Screenshot 2024-09-18 074950](https://github.com/user-attachments/assets/224d7de8-a54d-4386-89cb-031b9ce522e1)

**XML**
![Screenshot 2024-09-18 075018](https://github.com/user-attachments/assets/7e465fad-f5b7-4d19-89cb-7f181f215d6c)

**JSON by ID**
![Screenshot 2024-09-18 074920](https://github.com/user-attachments/assets/a1fd390d-3472-4812-9ded-07d7f6060705)

**XML by ID**
![Screenshot 2024-09-18 075040](https://github.com/user-attachments/assets/0f879e15-97ba-481d-9a02-aad7af575891)

</details>
<details>
<summary>Tugas 2: Implementasi MVT pada Django</summary>

## Cara implementasi tugas:

- Untuk membuat proyek baru di Django, saya perlu membuat direktori baru untuk proyek saya yang bernama librarree-books-eshop. 
Setelah itu, saya mengaktifkan virtual environment dan menyiapkan dependecies yang diperlukan dengan membuat file requirements.txt, kemudian menginstal dependencies tersebut.

- Sebelum membuat aplikasi main, saya pastikan virtual environment aktif, supaya aplikasi hanya mengakses dependencies yang telah diinstal dalam virtual environment saja.

- Setelah aplikasi main terbuat, saya menyambungkan aplikasi dengan proyek dengan mendaftarkan 'main' ke dalam list INSTALLED_APPS di settings.py proyek.
Untuk konfigurasi routing, saya membuat file URL untuk aplikasi main dan menambahkannya ke file URL proyek Utama.

- Selanjutnya, saya membuat direktori template, membuat file HTML, dan views.py yang akan mengembalikan tampilan yang akan ditampilkan saat URL diakses. Lalu saya mendefinisikan model Product dalam models.py dengan atribut name, price, dan description.

- Setelah semuanya siap,saya bisa menjalankan server Django dengan perintah python "manage.py runserver"

## Gambar request-response cycle Django:

![request-response cycle 2](https://github.com/user-attachments/assets/d03dc27b-534b-4b67-9120-80c3729f02d0)

- urls.py bertindak sebagai manajer yang mengontrol rute client request ke fungis view yang spesifik.

- models.py menyediakan interface untuk views.py berinteraksi dengan database.
  
- views.py mengambil data lewat perantara model and mengirimnya ke template untuk rendering.

- HTML template merupakan response akhir atau tampilan yang akan dikirim kembali lewat view ke client.

## Fungsi git dalam pengembangan perangkat lunak:

Git berperan sebagai version control, yaitu sistem yang mencatat serta menyimpan semua perubahan dan modifikasi pada sebuah file. 
Fungsi utamanya dalam pengembangan perangkat lunak adalah untuk menyimpan catatan modifikasi, memberi akses histori, dan memungkinkan kita untuk mengembalikan file ke kondisi atau versi sebelum-sebelumnya. Dengan git, kita juga mendapat kemudahan berkolaborasi dengan pengembang lain karena adanya fitur branching dan merging.

## Mengapa Django menjadi framework yang pertama dipelajari dalam pengembangan perangkat lunak?

Selain karena menggunakan Bahasa python yang sudah pernah dipelajari dan kita sudah familiar, Django menjadi framework yang popular digunakan dalam pengembangan perangkat lunak karena memiliki beberapa fitur yang dapat memudahkan proses seperti autentikasi pengguna,ORM, dan manajemen admin. Django juga menggunakan pola arsitektur yang terorganisir seperti Model-View-Template yang memisahkan antara logika aplikasi dari tampilan dan data. 

## Mengapa model pada Django disebut sebagai ORM?

Disebut object-relational-mapping (ORM) karena model tersebut merepresentasikan objek dari data yang disimpan dalam basis data relational. ORM memungkinkan untuk berinteraksi dengan database menggunakan objek python tanpa harus menulis kode SQL secara manual.
</details>
