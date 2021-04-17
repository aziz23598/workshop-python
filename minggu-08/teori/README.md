Pustaka Standar
LINK GitHub : https://github.com/aziz23598/workshop-python
1.	Antarmuka Sistem Operasi
Modul os menyediakan puluhan fungsi untuk berinteraksi dengan sistem operasi:
 
Pastikan untuk menggunakan import os daripada menggunakan os import *. Ini akan menjaga os.open () dari membayangi fungsi built-in open() yang beroperasi sangat berbeda. 
Bawaan fungsi dir() dan help() berguna sebagai alat bantu interaktif untuk bekerja dengan modul besar seperti os:
 
Untuk file harian dan tugas manajemen direktori, modul shutil modul menyediakan antarmuka tingkat yang lebih tinggi yang lebih mudah digunakan:
 

2.	File Wildcard
Modul Glob menyediakan fungsi untuk membuat daftar file dari pencarian direktori wildcard:
 
3.	Argumen Baris Perintah
Skrip utilitas umum sering kali perlu memproses argumen baris perintah. Argumen ini disimpan dalam atribut modul sys argv sebagai daftar. Misalnya hasil keluaran berikut dari berjalan di baris perintah:python demo.py one two three
 
Modul argparse menyediakan mekanisme yang lebih canggih untuk argumen baris perintah proses. Skrip berikut mengekstrak satu atau lebih nama file dan sejumlah baris opsional untuk ditampilkan:
 
Saat dijalankan pada baris perintah dengan , skrip disetel ke dan ke .python top.py --lines=5 alpha.txt beta.txtargs.lines5args.filenames['alpha.txt', 'beta.txt']

4.	Kesalahan Pengalihan Output dan Penghentian Program
Modul sys juga memiliki atribut untuk stdin , stdout , dan stderr . Yang terakhir berguna untuk memancarkan peringatan dan pesan kesalahan untuk membuatnya terlihat bahkan ketika stdout telah dialihkan:
 
Cara paling langsung untuk menghentikan skrip adalah dengan menggunakan sys.exit().

5.	Pencocokan Pola String
Modul re menyediakan alat ekspresi reguler untuk pengolahan string yang canggih. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi ringkas dan dioptimalkan:
 
Ketika hanya kemampuan sederhana yang dibutuhkan, metode string lebih disukai karena lebih mudah dibaca dan di-debug:
 

6.	Matematika
Modul Math memberikan akses ke mendasari C fungsi perpustakaan untuk floating point matematika:
 
Modul random menyediakan alat untuk membuat pilihan acak:
 
Modul Statistics menghitung sifat statistik dasar (mean, median, varians, dll) dari data numerik:
 
Proyek SciPy < https://scipy.org > memiliki banyak modul lain untuk komputasi numerik.

7.	Akses Internet
Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua cara yang paling sederhana adalah urllib.requestuntuk mengambil data dari URL dan smtplibuntuk mengirim email:
 

8.	Tanggal dan Waktu
Modul Datetime persediaan kelas untuk memanipulasi tanggal dan waktu di kedua sederhana dan cara yang kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus penerapannya adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran. Modul ini juga mendukung objek yang peka zona waktu.
 

9.	Kompresi Data
Pengarsipan data umum dan kompresi format secara langsung didukung oleh modul termasuk: zlib, gzip, bz2, lzma, zipfiledan tarfile.
 

10.	Pengukuran Kinerja
Beberapa pengguna Python mengembangkan minat yang dalam untuk mengetahui kinerja relatif dari berbagai pendekatan untuk masalah yang sama. Python menyediakan alat pengukuran yang menjawab pertanyaan tersebut dengan segera.
Misalnya, mungkin tergoda untuk menggunakan fitur tuple packing dan unpacking daripada pendekatan tradisional untuk bertukar argumen. Modul timeit cepat menunjukkan keunggulan kinerja yang sederhana:
 
Berbeda dengan tingkat timeit perincian yang bagus, modul profiledan pstatsmenyediakan alat untuk mengidentifikasi bagian waktu yang kritis dalam blok kode yang lebih besar.

11.	Kontrol Kualitas
Salah satu pendekatan untuk mengembangkan perangkat lunak berkualitas tinggi adalah menulis pengujian untuk setiap fungsi saat dikembangkan dan menjalankan pengujian tersebut secara sering selama proses pengembangan.
Modul doctest menyediakan alat untuk memindai modul dan memvalidasi tes tertanam dalam docstrings program ini. Konstruksi pengujian sesederhana memotong-dan-menempel panggilan biasa beserta hasilnya ke dalam docstring. Ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul doctest untuk memastikan kode tetap sesuai dengan dokumentasi:
 
Modul unittest ini tidak mudah seperti doctestmodul, tetapi memungkinkan satu set yang lebih komprehensif dari tes untuk dipertahankan dalam file terpisah:
 

12.	Batteries Included
Python memiliki filosofi "termasuk baterai". Ini paling baik dilihat melalui kemampuan canggih dan kuat dari paket yang lebih besar. Sebagai contoh:
•	The xmlrpc.clientdan xmlrpc.servermodul membuat melaksanakan prosedur panggilan jarak jauh ke dalam tugas yang hampir sepele. Terlepas dari nama modul, tidak diperlukan pengetahuan langsung atau penanganan XML.
•	The emailpaket perpustakaan untuk mengelola pesan email, termasuk MIME dan lainnyaDokumen pesan berbasis RFC 2822 . Tidak sepertismtplibdan poplibyang benar-benar mengirim dan menerima pesan, paket email memiliki perangkat yang lengkap untuk membangun atau mendekode struktur pesan yang kompleks (termasuk lampiran) dan untuk mengimplementasikan encoding internet dan protokol header.
•	The jsonpaket menyediakan dukungan kuat untuk parsing format data interchange populer ini. The csvdukungan modul membaca langsung dan menulis file dalam format Nilai Comma-Separated, umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh xml.etree.ElementTree, xml.domdan xml.saxpaket. Bersama-sama, modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.
•	The sqlite3modul pembungkus untuk perpustakaan basis data SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL sedikit tidak standar.
•	Internasionalisasi didukung oleh sejumlah modul termasuk gettext, locale, dan codecspaket.
Bagian kedua ini mencakup modul yang lebih maju yang mendukung kebutuhan pemrograman profesional. Modul ini jarang muncul dalam skrip kecil.
13.	Pemformatan Output
Modul reprlib menyediakan versi repr()disesuaikan untuk menampilkan disingkat kontainer besar atau sangat bersarang:
 
Modul Pprint menawarkan kontrol yang lebih canggih lebih mencetak baik built-in dan benda-benda yang ditetapkan pengguna dengan cara yang dapat dibaca oleh interpreter. Jika hasilnya lebih dari satu baris, "printer cantik" menambahkan jeda baris dan lekukan untuk menampilkan struktur data dengan lebih jelas:
 
Modul Textwrap meformat paragraf teks agar sesuai dengan lebar layar yang diberikan:
 
Modul locale mengakses database format data tertentu budaya. Atribut pengelompokan fungsi format lokal menyediakan cara langsung untuk memformat angka dengan pemisah grup:
 

14.	Templating
Modul string termasuk serbaguna Template kelas dengan sintaks disederhanakan cocok untuk mengedit oleh pengguna akhir. Ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi.
Formatnya menggunakan nama placeholder yang dibentuk $dengan pengenal Python yang valid (karakter alfanumerik dan garis bawah). Di sekeliling placeholder dengan tanda kurung kurawal memungkinkannya diikuti oleh lebih banyak huruf alfanumerik tanpa spasi. Menulis $$membuat satu pelolosan $:
 
Metode substitute()menimbulkan KeyErrorketika pengganti tidak disediakan dalam kamus atau argumen kata kunci. Untuk aplikasi gaya gabungan surat, data yang diberikan pengguna mungkin tidak lengkap dan safe_substitute()metodenya mungkin lebih sesuai - ini akan membiarkan placeholder tidak berubah jika datanya hilang:
 
Subclass template dapat menentukan pembatas kustom. Misalnya, utilitas penggantian nama batch untuk browser foto dapat memilih untuk menggunakan tanda persen untuk placeholder seperti tanggal saat ini, nomor urut gambar, atau format file:
 
Aplikasi lain untuk pembuatan template adalah memisahkan logika program dari detail berbagai format keluaran. Ini memungkinkan untuk mengganti template khusus untuk file XML, laporan teks biasa, dan laporan web HTML. 

15.	Bekerja dengan Tata Letak Rekaman Data Biner
Modul struct menyediakan pack()dan unpack()fungsi untuk bekerja dengan format rekaman biner variabel panjang. Contoh berikut menunjukkan cara melakukan perulangan melalui informasi header dalam file ZIP tanpa menggunakan zipfilemodul. Kode paket "H"dan "I"masing-masing mewakili dua dan empat byte nomor unsigned. Ini "<"menunjukkan bahwa mereka adalah ukuran standar dan dalam urutan byte little-endian:
 

16.	Multi-threading
Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Utas dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima masukan pengguna saat tugas lain berjalan di latar belakang. Kasus penggunaan terkait menjalankan I / O secara paralel dengan komputasi di thread lain.
Kode berikut menunjukkan bagaimana threadingmodul tingkat tinggi dapat menjalankan tugas di latar belakang sementara program utama terus berjalan:
 
Tantangan utama dari aplikasi multi-utas adalah mengoordinasikan utas yang berbagi data atau sumber daya lainnya. Untuk itu, modul threading menyediakan sejumlah primitif sinkronisasi termasuk kunci, peristiwa, variabel kondisi, dan semaphore.
Meskipun alat tersebut kuat, kesalahan desain kecil dapat mengakibatkan masalah yang sulit untuk direproduksi. Jadi, pendekatan yang disukai untuk koordinasi tugas adalah memusatkan semua akses ke sumber daya dalam satu utas dan kemudian menggunakan queuemodul untuk memberi makan utas tersebut dengan permintaan dari utas lain. Aplikasi yang menggunakan Queueobjek untuk komunikasi dan koordinasi antar utas lebih mudah dirancang, lebih mudah dibaca, dan lebih andal.

17.	Logging
Modul logging menawarkan sistem logging fitur dan fleksibel penuh. Sederhananya, pesan log dikirim ke file atau ke sys.stderr:
 
Secara default, pesan informasional dan debugging disembunyikan dan output dikirim ke kesalahan standar. Opsi keluaran lainnya termasuk perutean pesan melalui email, datagram, soket, atau ke Server HTTP. Filter baru dapat memilih routing yang berbeda berdasarkan prioritas pesan: DEBUG, INFO, WARNING, ERROR, dan CRITICAL.
Sistem pencatatan dapat dikonfigurasi langsung dari Python atau dapat dimuat dari file konfigurasi yang dapat diedit pengguna untuk pencatatan yang disesuaikan tanpa mengubah aplikasi.

18.	Referensi Lemah
Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus). Memori dibebaskan segera setelah referensi terakhirnya dihapus.
Pendekatan ini berfungsi dengan baik untuk sebagian besar aplikasi tetapi terkadang ada kebutuhan untuk melacak objek hanya selama mereka digunakan oleh sesuatu yang lain. Sayangnya, melacaknya saja akan membuat referensi yang menjadikannya permanen. The weakrefModul menyediakan alat untuk objek pelacakan tanpa membuat referensi. Ketika objek tidak lagi dibutuhkan, secara otomatis dihapus dari tabel weakref dan callback dipicu untuk objek weakref. Aplikasi umum menyertakan objek cache yang mahal untuk dibuat:
 

19.	Alat untuk Bekerja dengan Daftar
Banyak kebutuhan struktur data yang dapat dipenuhi dengan tipe daftar bawaan. Namun, terkadang ada kebutuhan untuk implementasi alternatif dengan trade-off kinerja yang berbeda.
Modul arraymenyediakan array()objek yang seperti daftar yang menyimpan hanya homogen data dan menyimpannya lebih kompak. Contoh berikut menunjukkan larik bilangan yang disimpan sebagai bilangan biner unsigned dua byte (kode jenis "H") daripada 16 byte biasa per entri untuk daftar reguler objek int Python:
 
Modul collections menyediakan deque()objek yang seperti daftar dengan menambahkan lebih cepat dan muncul dari sisi kiri namun pencarian lebih lambat di tengah. Objek ini sangat cocok untuk mengimplementasikan antrian dan luasnya pencarian pohon pertama:
 
Selain implementasi daftar alternatif, pustaka juga menawarkan alat lain seperti bisectmodul dengan fungsi untuk memanipulasi daftar yang diurutkan:
 
Modul heapqmenyediakan fungsi untuk melaksanakan tumpukan berdasarkan daftar reguler. Entri dengan nilai terendah selalu disimpan di posisi nol. Ini berguna untuk aplikasi yang berulang kali mengakses elemen terkecil tetapi tidak ingin menjalankan urutan daftar lengkap:
 

20.	Aritmatika Titik Apung Desimal
Modul decimal menawarkan Decimaldatatype untuk desimal aritmatika floating point. Dibandingkan dengan float implementasi built-in dari floating point biner, class ini sangat membantu
•	aplikasi keuangan dan penggunaan lain yang membutuhkan representasi desimal yang tepat,
•	kontrol atas presisi,
•	kontrol atas pembulatan untuk memenuhi persyaratan hukum atau peraturan,
•	melacak tempat desimal signifikan, atau
•	aplikasi di mana pengguna mengharapkan hasil untuk mencocokkan perhitungan yang dilakukan dengan tangan.
Misalnya, menghitung pajak 5% untuk biaya telepon 70 sen memberikan hasil yang berbeda dalam titik mengambang desimal dan titik mengambang biner. Perbedaan menjadi signifikan jika hasil dibulatkan ke sen terdekat:
 
Hasil Decimal menyimpan nol miring, otomatis menyimpulkan empat signifikansi tempat dari multiplicands dengan dua tempat penting. Desimal mereproduksi matematika seperti yang dilakukan dengan tangan dan menghindari masalah yang dapat muncul ketika titik mengambang biner tidak dapat merepresentasikan besaran desimal secara tepat.
Representasi yang tepat memungkinkan Decimalkelas untuk melakukan penghitungan modulo dan uji kesetaraan yang tidak cocok untuk titik mengambang biner:
 
Modul Decimal menyediakan aritmatika dengan sebanyak presisi yang diperlukan:
