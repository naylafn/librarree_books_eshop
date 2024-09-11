# Tugas 2: Implementasi MVT pada Django

### Nayla Farah Nida

### 2306213426


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
