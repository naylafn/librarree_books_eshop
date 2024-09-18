# Tugas 3: Implementasi Form dan Data Delivery pada Django

### Nayla Farah Nida
### 2306213426

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

