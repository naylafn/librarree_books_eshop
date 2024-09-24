### Nayla Farah Nida
### 2306213426

# tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

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


# Tugas 3: Implementasi Form dan Data Delivery pada Django

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


# Tugas 2: Implementasi MVT pada Django

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

