Input dan Output
LINK GitHub : https://github.com/aziz23598/workshop-python 
Ada beberapa cara untuk mempresentasikan output dari suatu program. Pertama data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke file untuk digunakan di masa mendatang. Pada pertemuan ini akan membahas beberapa kemungkinan tersebut.
1.	Pemformatan Output Lebih Menarik
Sejauh ini kita telah menemukan dua cara menulis nilai yaitu, pernyataan ekspresi dan fungsi print(). Cara ketiga adalah menggunakan metode write() objek file, file keluaran standar dapat dirujuk sebagai sys.stdout.
Seringkali kita menginginkan lebih banyak kontrol atas pemformatan output kita daripada sekadar mencetak nilai yang dipisahkan spasi. Ada beberapa cara untuk memformat keluaran.
1)	Untuk menggunakan literal string yang diformat , awali string dengan f atau F sebelum tanda kutip pembuka atau tanda kutip tiga. Di dalam string ini, kita dapat menulis ekspresi Python antara { dan } karakter yang dapat merujuk ke variabel atau nilai literal.
 
2)	Metode string str.format() membutuhkan usaha lebih manual. kita masih akan menggunakan { dan } untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan mendetail, tetapi kita juga harus memberikan informasi yang akan diformat.
 
3)	Terakhir, kita dapat melakukan semua penanganan string sendiri dengan menggunakan operasi pemotongan dan penggabungan string untuk membuat tata letak apa pun yang dapat kita bayangkan. Jenis string memiliki beberapa metode yang melakukan operasi yang berguna untuk mengisi string dengan lebar kolom tertentu.
Saat kita tidak memerlukan keluaran mewah tetapi hanya ingin tampilan cepat beberapa variabel untuk keperluan debugging, kita dapat mengonversi nilai apa pun menjadi string dengan fungsi repr() atau str().
Fungsi str() dimaksudkan untuk mengembalikan representasi dari nilai-nilai yang cukup terbaca-manusia, sementara repr() dimaksudkan untuk menghasilkan representasi yang dapat dibaca oleh interpreter (atau akan memaksa SyntaxError jika tidak ada yang setara sintaks). Untuk objek yang tidak memiliki representasi tertentu untuk konsumsi manusia, str() akan mengembalikan nilai yang sama seperti repr(). Banyak nilai, seperti angka atau struktur seperti daftar dan kamus, memiliki representasi yang sama menggunakan salah satu fungsi. String, khususnya, memiliki dua representasi berbeda.
Contoh:
 
Modul string berisi Template kelas yang belum menawarkan cara lain untuk menggantikan nilai-nilai ke dalam string, menggunakan placeholder seperti $x dan menggantinya dengan nilai-nilai dari sebuah kamus, tapi menawarkan kontrol jauh lebih sedikit dari format.
a.	String Literal Terformat
Literal string yang diformat (juga disebut f-string) memungkinkan kita menyertakan nilai ekspresi Python di dalam string dengan mengawali string dengan f atau F dan menulis ekspresi sebagai {expression}.
Penentu format opsional bisa mengikuti ekspresi. Ini memungkinkan kontrol yang lebih besar atas bagaimana nilai diformat. Contoh berikut membulatkan pi ke tiga tempat setelah desimal:
 
Meneruskan bilangan bulat setelah ':' akan menyebabkan bidang itu menjadi jumlah minimum karakter yang lebar. Ini berguna untuk membuat kolom berbaris.
 
Pengubah lain dapat digunakan untuk mengonversi nilai sebelum diformat. '!a' terapkan ascii(), '!s' terapkan str(), dan '!r' terapkan repr():
 

b.	Metode format String ()
Penggunaan dasar metode str.format() ini terlihat seperti berikut:
 
Tanda kurung dan karakter di dalamnya (disebut bidang format) diganti dengan objek yang diteruskan ke metode str.format(). Angka dalam tanda kurung dapat digunakan untuk merujuk ke posisi objek yang diteruskan ke metode str.format().
 
Jika argumen kata kunci digunakan dalam metode str.format() ini, nilainya dirujuk dengan menggunakan nama argumen.
 
Argumen posisi dan kata kunci dapat digabungkan secara sembarangan:
 
Jika kita memiliki string format yang sangat panjang yang tidak ingin kita pisahkan, alangkah baiknya jika kita dapat mereferensikan variabel yang akan diformat berdasarkan nama, bukan berdasarkan posisi. Ini dapat dilakukan hanya dengan meneruskan dict dan menggunakan tanda kurung siku '[]' untuk mengakses kunci.
 
Ini juga dapat dilakukan dengan melewatkan tabel sebagai argumen kata kunci dengan notasi '**'.
 
Ini sangat berguna jika dikombinasikan dengan fungsi bawaan vars(), yang mengembalikan kamus yang berisi semua variabel lokal.
Sebagai contoh, baris berikut menghasilkan kumpulan kolom yang tersusun rapi yang menghasilkan bilangan bulat dan kuadrat serta kubusnya:
 

c.	Pemformatan String Manual
Berikut adalah tabel kotak dan kubus yang sama, yang diformat secara manual:
 
(Perhatikan bahwa satu spasi di antara setiap kolom ditambahkan menurut cara kerjanya print(): selalu menambahkan spasi di antara argumennya.)
Metode str.rjust() string benda kanan membenarkan string dalam bidang lebar yang diberikan oleh padding dengan spasi di sebelah kiri. Ada metode serupa str.ljust() dan str.center(). Metode ini tidak menulis apa pun, mereka hanya mengembalikan string baru. Jika string input terlalu panjang, mereka tidak memotongnya, tetapi mengembalikannya tanpa perubahan; ini akan mengacaukan tata letak kolom kita tetapi itu biasanya lebih baik daripada alternatifnya, yang akan berbohong tentang suatu nilai. (Jika kita benar-benar menginginkan pemotongan, kita selalu dapat menambahkan operasi slice, seperti dalam x.ljust(n)[:n].)
Ada metode lain str.zfill(), yang mengisi string numerik di sebelah kiri dengan nol. Ini memahami tentang tanda plus dan minus:
 

d.	Pemformatan string lama
Operator % (modulo) juga dapat digunakan untuk pemformatan string. Diberikan , contoh in diganti dengan nol atau lebih elemen . Operasi ini umumnya dikenal sebagai interpolasi string. Sebagai contoh: 'string' % values % string values
 

2.	Membaca dan Menulis File
open() mengembalikan file objek , dan ini paling sering digunakan dengan dua argumen: .open(filename, mode)
 
Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter yang menjelaskan cara penggunaan file tersebut. mode bisa 'r' ketika file hanya akan dibaca, 'w' untuk hanya menulis (file yang ada dengan nama yang sama akan dihapus), dan 'a' membuka file untuk ditambahkan; data apa pun yang ditulis ke file secara otomatis ditambahkan ke bagian akhir. 'r+' membuka file untuk membaca dan menulis. The Modus argumen adalah opsional; 'r' akan diasumsikan jika dihilangkan.
Biasanya, file dibuka dalam mode teks artinya, kita membaca dan menulis string dari dan ke file, yang disandikan dalam pengkodean tertentu. Jika encoding tidak ditentukan, defaultnya bergantung pada platform (lihat open()). 'b' ditambahkan ke mode membuka file dalam mode biner : sekarang data dibaca dan ditulis dalam bentuk objek byte. Mode ini harus digunakan untuk semua file yang tidak berisi teks.
Dalam mode teks, default saat membaca adalah mengonversi akhir baris khusus platform ( \ndi Unix, \r\ndi Windows) menjadi hanya \n. Saat menulis dalam mode teks, defaultnya adalah mengonversi kemunculan \n kembali ke akhir baris khusus platform. Modifikasi di balik layar ke file data ini baik-baik saja untuk file teks, tetapi akan merusak data biner seperti itu di JPEG atau EXE file. Berhati-hatilah saat menggunakan mode biner saat membaca dan menulis file semacam itu.
Ini adalah praktik yang baik untuk menggunakan with kata kunci saat menangani objek file. Keuntungannya adalah bahwa file ditutup dengan benar setelah rangkaiannya selesai, bahkan jika pengecualian dimunculkan di beberapa titik. Menggunakan with juga jauh lebih pendek daripada menulis padanan try- finallyblok:
 
Jika kita tidak menggunakan with kata kunci, maka kita harus memanggil f.close() untuk menutup file dan segera membebaskan semua sumber daya sistem yang digunakan olehnya.
Peringatan : Memanggil f.write() tanpa menggunakan with kata kunci atau memanggil f.close() dapat mengakibatkan argumen f.write() tidak sepenuhnya ditulis ke disk, meskipun program berhasil keluar.
Setelah objek file ditutup, baik dengan with pernyataan atau dengan memanggil f.close(), upaya untuk menggunakan objek file secara otomatis akan gagal.
 

a.	Metode Objek File
Contoh lainnya di bagian ini akan mengasumsikan bahwa objek file yang disebut f telah dibuat.
Untuk membaca konten file, panggil f.read(size), yang membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). size adalah argumen numerik opsional. Jika ukuran dihilangkan atau negatif, seluruh konten file akan dibaca dan dikembalikan; itu masalah kita jika file tersebut dua kali lebih besar dari memori mesin kita. Jika tidak, paling banyak karakter ukuran (dalam mode teks) atau ukuran byte (dalam mode biner) dibaca dan dikembalikan. Jika akhir file telah tercapai, f.read() akan mengembalikan string kosong (' ').
 
f.readline() membaca satu baris dari file; karakter baris baru ( \n) tertinggal di akhir string, dan hanya dihilangkan di baris terakhir file jika file tidak diakhiri dengan baris baru. Ini membuat nilai kembali tidak ambigu; jika f.readline()mengembalikan string kosong, akhir file telah tercapai, sedangkan baris kosong diwakili oleh '\n', string yang hanya berisi satu baris baru.
 
Untuk membaca baris dari file, kita dapat melakukan loop di atas objek file. Ini hemat memori, cepat, dan mengarah ke kode sederhana:
 
Jika kita ingin membaca semua baris file dalam daftar, kita juga dapat menggunakan list(f) atau f.readlines().
Menulis f.write(string) konten string ke file, mengembalikan jumlah karakter yang ditulis.
 
Jenis objek lain perlu dikonversi - baik menjadi string (dalam mode teks) atau objek byte (dalam mode biner) - sebelum menulisnya:
 
f.tell() mengembalikan integer yang memberikan posisi objek file saat ini dalam file yang direpresentasikan sebagai jumlah byte dari awal file saat dalam mode biner dan angka buram saat dalam mode teks.
Untuk mengubah posisi objek file, gunakan . Posisi dihitung dari menambahkan offset ke titik referensi; titik referensi dipilih oleh argumen whence . Nilai dimana 0 mengukur dari awal file, 1 menggunakan posisi file saat ini, dan 2 menggunakan akhir file sebagai titik referensi. whence dapat dihilangkan dan default ke 0, menggunakan awal file sebagai titik referensi.f.seek(offset, whence)
 
Dalam file teks (yang dibuka tanpa bdalam mode string), hanya pencarian relatif terhadap awal file yang diperbolehkan (pengecualian mencari ke akhir file dengan ) dan satu-satunya nilai offset yang valid adalah yang dikembalikan dari , atau nol. Nilai offset lainnya menghasilkan perilaku tidak terdefinisi.seek(0, 2) f.tell()
Objek file memiliki beberapa metode tambahan, seperti isatty() dan truncate() yang lebih jarang digunakan; lihat Referensi Perpustakaan untuk panduan lengkap untuk mengarsipkan objek.

b.	Menyimpan data terstruktur dengan
String dapat dengan mudah ditulis dan dibaca dari sebuah file. Bilangan membutuhkan sedikit usaha, karena metode read() ini hanya mengembalikan string, yang harus diteruskan ke fungsi seperti int(), yang mengambil string seperti '123' dan mengembalikan nilai numerik 123. Saat kita ingin menyimpan tipe data yang lebih kompleks seperti daftar bersarang dan kamus, penguraian dan pembuatan serial dengan tangan menjadi rumit.
Daripada membuat pengguna terus-menerus menulis dan men-debug kode untuk menyimpan tipe data yang rumit ke file, Python memungkinkan kita menggunakan format pertukaran data populer yang disebut JSON (JavaScript Object Notation) . Modul standar yang dipanggil jsondapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string; proses ini disebut serialisasi . Merekonstruksi data dari representasi string disebut deserializing . Antara serialisasi dan deserialisasi, string yang mewakili objek mungkin telah disimpan dalam file atau data, atau dikirim melalui koneksi jaringan ke mesin yang jauh.
Jika kita memiliki sebuah objek x, kita dapat melihat representasi string JSON-nya dengan baris kode sederhana:
 
Varian lain dari fungsi dumps() tersebut, disebut dump(), cukup membuat serial objek menjadi file teks. Jadi jika f adalah file teks objek dibuka untuk menulis, kita bisa melakukan ini:
 
Untuk memecahkan kode objek lagi, jika f merupakan objek file teks yang telah dibuka untuk dibaca:
 
Teknik serialisasi sederhana ini dapat menangani daftar dan kamus, tetapi serialisasi instance kelas arbitrer di JSON membutuhkan sedikit usaha ekstra. Referensi jsonmodul berisi penjelasan tentang ini.
