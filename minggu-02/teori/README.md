Pengendali Aliran Program

A.	Pernyataan IF
Pada IF terdapat 2 bagian, yaitu bagian elif (else if) dan else. Untuk bagian elif bisa dibuat lebih dari satu kondisi. Tetapi bagian else sifatnya opsional, jadi bisa diberi atau tidak.

B.	Pernyataan FOR
Pernyataan for dalam Python sedikit berbeda dari Bahasa C atau Pascal. Pernyataan for dalam Python diulangi pada item-item dari urutan apa pun (daftar list atau string), dalam urutan yang muncul dalam urutan.

Kode yang memodifikasi koleksi collection sambil mengulangi koleksi yang sama bisa sulit untuk diperbaiki. Sebagai gantinya, biasanya lebih mudah untuk mengulang salinan koleksi atau membuat koleksi baru.

C.	Fungsi range()
Jika kita perlu mengulangi urutan angka, fungsi bawaan range() berguna. Ini menghasilkan urutan pregressions aritmatika

Titik akhir yang diberikan tidak pernah menjadi bagian dari urutan yang dihasilkan; range(10) menghasilkan 10 nilai, indeks sah legal untuk item dengan urutan panjang 10. Dimungkinkan untuk membiarkan rentang mulai dari nomor lain, atau untuk menentukan kenaikan yang berbeda (bahkan negatif; kadang-kadang ini disebut 'step').

Untuk beralih pada indeks urutan, kita dapat menggabungkan range() dan len().

Hal aneh terjadi jika Anda hanya mencetak rentang range. Dalam banyak hal objek dikembalikan oleh range() berperilaku seolah-olah itu adalah daftar list, tetapi sebenarnya tidak. Ini adalah objek yang mengembalikan item berurutan dari urutan yang diinginkan ketika kita mengulanginya, tetapi itu tidak benar-benar membuat daftar list, sehingga menghemat ruang. Objek seperti itu disebut iterable, yaitu, cocok sebagai target untuk fungsi dan konstruksi yang mengharapkan sesuatu dari mana mereka dapat memperoleh item berturut-turut sampai pasokan habis.
 
D.	Loops
Pernyataan break, seperti dalam C, keluar dari bagian terdalam yang terlampir perulangan for atau while. Pernyataan perulangan loop mungkin memiliki klausa else, pernyataan tersebut dieksekusi ketika loop berakhir melalui selesainya exhaustion iterable (dengan for) atau ketika kondisi menjadi salah (dengan while), tetapi tidak ketika loop diakhiri oleh pernyataan break. Contohnya seperti gambar diatas.
Ketika digunakan dengan sebuah perulangan, klausa else memiliki lebih banyak kesamaan dengan klausa else dari pernyataan try dibandingkan dengan pernyataan if: sebuah klausa else pernyataan try berjalan ketika tidak ada pengecualian terjadi, dan klausa else perulangan berjalan ketika tidak ada break terjadi. Pernyataan continue, juga sama seperti pada bahasa C, melanjutkan dengan pengulangan berikutnya dari loop.

E.	Pernyataan PASS
Pernyataan pass tidak melakukan apa-apa. Ini dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tindakan. Ini biasanya digunakan untuk membuat kelas minimal. Pernyataan pass dapat digunakan sebagai tempat-penampung place-holder untuk fungsi atau badan bersyarat conditional body saat kita bekerja pada kode baru, memungkinkan kita untuk terus berpikir pada tingkat yang lebih abstrak.

F.	Fungsi 
Def merupakan fungsi definition yang harus diikuti okeh nama fungsi dan daftar parameter formal yang ada didalam kurung. Pernyataan yang membentuk badan fungsi mulai dari baris berikutnya, dan harus diberi indentasi.
Pernyataan pertama dari badan fungsi secara opsional dapat berupa string literal, string literal ini adalah string dokumentasi fungsi, atau docstring.
execution dari suatu fungsi memperkenalkan tabel simbol baru yang digunakan untuk variabel lokal dari fungsi tersebut. Lebih tepatnya, semua tugas variabel dalam suatu fungsi menyimpan nilai dalam tabel simbol lokal; sedangkan referensi variabel pertama-tama terlihat pada tabel simbol lokal, kemudian pada tabel simbol lokal lampiran enclosing fungsi, kemudian pada tabel simbol global, dan akhirnya pada tabel nama bawaan. Dengan demikian, variabel global dan variabel lampiran enclosing fungsi tidak dapat secara langsung menetapkan nilai dalam suatu fungsi (kecuali, untuk variabel global, disebutkan dalam pernyataan global, atau, untuk variabel lampiran enclosing fungsi, dinamai dalam pernyataan nonlocal), meskipun mungkin direferensikan.

Definisi fungsi mengasosiasikan nama fungsi dengan objek fungsi dalam tabel simbol saat ini. Sebuah interpreter dapat mengenali objek yang ditunjuk dengan nama itu sebagai fungsi yang ditentukan oleh pengguna. Nama lain juga dapat menunjuk ke objek fungsi yang sama dan juga dapat digunakan untuk mengakses fungsi tersebut.
 
fib bukan fungsi melainkan prosedur karena tidak mengembalikan nilai. Fungsi  tanpa pernyataan return mengembalikan nilai. Nilai ini disebut None. Menulis nilai None biasanya dihilangkan suppressed oleh interpreter jika itu akan menjadi satu-satunya nilai yang ditulis.

G.	Mendefinisikan fungsi
Bentuk yang paling berguna adalah menentukan nilai bawaan untuk satu atau lebih argumen. Ini menciptakan fungsi yang bisa dipanggil dengan argumen yang lebih sedikit daripada yang didefinisikan untuk diizinkan.
Fungsi ini dapat dipanggil dengan beberapa cara:
•	hanya memberikan argumen wajib: ask_ok('Do you really want to quit?')
•	memberikan salah satu argumen opsional: ask_ok('OK to overwrite the file?', 2)
•	atau bahkan memberikan semua argumen: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

Nilai bawaan dievaluasi hanya sekali. Ini membuat perbedaan ketika bawaan adalah objek yang dapat diubah seperti daftar list, kamus dictionary, atau instances dari sebagian besar kelas. Misalnya, fungsi berikut mengakumulasi argumen yang diteruskan pada panggilan berikutnya.

Fungsi juga dapat dipanggil menggunakan keyword argument dari bentuk kwarg=value.
 
Ketika parameter formal terakhir dari bentuk **name ada, ia menerima kamus dictionary yang berisi semua argumen kata kunci keyword argument kecuali yang terkait dengan parameter formal. Ini dapat digabungkan dengan parameter formal dari bentuk *name  yang menerima tuple yang berisi argumen posisi di luar daftar parameter formal. (*name harus ada sebelum **name.) 

Definisi fungsi pertama, standard_arg, bentuk yang paling akrab, tidak menempatkan batasan pada konvensi pemanggilan dan argumen dapat dilewatkan dengan posisi atau kata kunci.
 
Fungsi kedua pos_only_arg dibatasi hanya menggunakan parameter posisi karena ada / dalam definisi fungsi.

Fungsi ketiga kwd_only_args hanya memungkinkan argumen kata kunci keyword argument seperti ditunjukkan oleh * dalam definisi fungsi

Opsi yang paling jarang digunakan adalah menentukan bahwa suatu fungsi dapat dipanggil dengan sejumlah argumen acak arbitrary. Argumen-argumen ini akan dibungkus dalam sebuah tuple. Sebelum jumlah variabel argumen, nol atau lebih argumen normal dapat muncul.
 
Biasanya, argumen variadic ini akan menjadi yang terakhir dalam daftar parameter formal, karena mereka mengambil semua argumen masukan yang tersisa yang diteruskan ke fungsi. Parameter formal apa pun yang muncul setelah parameter *args adalah argumen 'keyword-only', yang berarti bahwa parameter itu hanya dapat digunakan sebagai kata kunci alih-alih argumen posisi
 
Situasi sebaliknya terjadi ketika argumen sudah ada dalam daftar list atau tuple tetapi perlu dibongkar untuk panggilan fungsi yang membutuhkan argumen posisi terpisah. Sebagai contoh, fungsi bawaan range() mengharapkan argumen terpisah start dan stop. Jika tidak tersedia secara terpisah, tulis fungsi panggilan dengan operator-* untuk membongkar argumen dari daftar list atau tuple
 
Dengan cara yang sama, kamus dapat mengirimkan argumen kata kunci dengan operator-**
 
Fungsi kecil anonim dapat dibuat dengan kata kunci lambda. Fungsi ini mengembalikan jumlah dari dua argumennya: lambda a, b: a+b. Fungsi Lambda dapat digunakan di mana pun objek fungsi diperlukan. Mereka secara sintaksis terbatas pada satu ekspresi. Secara semantik, mereka hanya pemanis sintaksis untuk definisi fungsi normal. Seperti definisi fungsi bersarang, fungsi lambda dapat mereferensikan variabel dari cakupan yang mengandung.
 
Berikut adalah beberapa konvensi tentang konten dan format string dokumentasi.
Baris pertama harus selalu berupa ringkasan singkat dan ringkas dari tujuan objek. Untuk singkatnya, itu tidak boleh secara eksplisit menyatakan nama atau jenis objek, karena ini tersedia dengan cara lain (kecuali jika nama tersebut merupakan kata kerja yang menggambarkan operasi fungsi). Baris ini harus dimulai dengan huruf kapital dan diakhiri dengan titik.
Jika ada lebih banyak baris dalam string dokumentasi, baris kedua harus kosong, memisahkan ringkasan secara visual dari sisa deskripsi. Baris berikut harus satu atau lebih paragraf yang menggambarkan konvensi pemanggilan objek, efek sampingnya, dll.
Pengurai Python tidak menghapus lekukan dari string multi-baris literal di Python, jadi alat yang memproses dokumentasi harus menghapus indentasi jika diinginkan. Ini dilakukan dengan menggunakan konvensi berikut. Baris tidak-kosong pertama setelah baris pertama string menentukan jumlah indentasi untuk seluruh string dokumentasi. (Kami tidak dapat menggunakan baris pertama karena umumnya berbatasan dengan tanda kutip pembukaan string sehingga indentasinya tidak terlihat dalam string literal.) Spasi "equivalent" untuk indentasi ini kemudian dihilangkan dari awal semua baris string. Baris yang indentasi lebih sedikit seharusnya tidak terjadi, tetapi jika terjadi semua spasi whitespace utama harus dihilangkan. Kesetaraan spasi harus diuji setelah ekspansi tab (hingga 8 spasi, biasanya).
 
Function annotations informasi metadata yang sepenuhnya opsional tentang jenis yang digunakan oleh fungsi yang ditentukan pengguna. Annotations disimpan dalam atribut __annotations__ dari fungsi sebagai kamus dictionary dan tidak berpengaruh pada bagian fungsi yang lain. Anotasi parameter didefinisikan oleh titik dua setelah nama parameter, diikuti oleh ekspresi yang mengevaluasi nilai anotasi. Anotasi pengembalian didefinisikan oleh literal ->, diikuti oleh ekspresi, antara daftar parameter dan titik dua yang menunjukkan akhir dari pernyataan def. Contoh berikut memiliki argumen posisi, argumen kata kunci keyword argument, dan nilai kembalian yang dianotasi
