Object Oriented Programming
LINK GitHub : https://github.com/aziz23598/workshop-python
Kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama. Membuat kelas baru membuat jenis objek baru, memungkinkan instance baru dari jenis itu dibuat. Setiap instance kelas dapat memiliki atribut yang dilampirkan padanya untuk mempertahankan statusnya. Instance kelas juga dapat memiliki metode (ditentukan oleh kelasnya) untuk mengubah statusnya.
Dibandingkan dengan bahasa pemrograman lain, mekanisme kelas Python menambahkan kelas dengan minimal sintaks dan semantik baru. Ini adalah campuran dari mekanisme kelas yang ditemukan di C ++ dan Modula-3. Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme pewarisan kelas memungkinkan beberapa kelas dasar, kelas turunan dapat menimpa metode apa pun dari kelas atau kelas dasarnya, dan metode dapat memanggil metode kelas dasar dengan nama yang sama . Objek dapat berisi jumlah dan jenis data yang berubah-ubah. Seperti halnya modul, kelas mengambil bagian dari sifat dinamis Python: mereka dibuat saat runtime, dan dapat dimodifikasi lebih lanjut setelah dibuat.
Dalam terminologi C ++, biasanya anggota kelas (termasuk anggota data) adalah publik (kecuali lihat di bawah Variabel Pribadi ), dan semua fungsi anggota adalah virtual . Seperti di Modula-3, tidak ada singkatan untuk mereferensikan anggota objek dari metodenya: fungsi metode dideklarasikan dengan argumen pertama eksplisit yang mewakili objek, yang disediakan secara implisit oleh panggilan. Seperti di Smalltalk, kelas itu sendiri adalah objek. Ini memberikan semantik untuk mengimpor dan mengganti nama. Tidak seperti C ++ dan Modula-3, tipe bawaan dapat digunakan sebagai kelas dasar untuk ekstensi oleh pengguna. Juga, seperti di C ++, sebagian besar operator bawaan dengan sintaks khusus (operator aritmatika, langganan, dll.) Dapat didefinisikan ulang untuk instance kelas.
1.	Nama dan Objek
Objek memiliki individualitas, dan banyak nama (dalam beberapa cakupan) dapat diikat ke objek yang sama. Ini dikenal sebagai aliasing dalam bahasa lain. Ini biasanya tidak dihargai pada pandangan pertama di Python, dan dapat diabaikan dengan aman ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tupel). Namun, aliasing memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang bisa berubah seperti daftar, kamus, dan sebagian besar jenis lainnya. Ini biasanya digunakan untuk kepentingan program, karena alias berperilaku seperti pointer dalam beberapa hal. Misalnya, mengoper sebuah objek itu murah karena hanya sebuah pointer yang dilewatkan oleh implementasi; dan jika suatu fungsi memodifikasi objek yang diteruskan sebagai argumen, pemanggil akan melihat perubahan - ini menghilangkan kebutuhan akan dua mekanisme penerusan argumen yang berbeda seperti di Pascal.

2.	Lingkup dan Namespaces Python
Sebuah namespace adalah pemetaan dari nama ke objek. Sebagian besar ruang nama saat ini diimplementasikan sebagai kamus Python, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan mungkin berubah di masa mendatang. Contoh ruang nama adalah: kumpulan nama bawaan (berisi fungsi seperti abs(), dan nama pengecualian bawaan); nama global dalam sebuah modul; dan nama lokal dalam pemanggilan fungsi. Dalam arti himpunan atribut dari suatu objek juga membentuk namespace. Hal penting yang perlu diketahui tentang ruang nama adalah bahwa sama sekali tidak ada hubungan antara nama di ruang nama yang berbeda; misalnya, dua modul berbeda dapat mendefinisikan sebuah fungsi maximize tanpa kebingungan - pengguna modul harus mengawalnya dengan nama modul.
Ngomong-ngomong, saya menggunakan atribut kata untuk nama apa pun setelah titik - misalnya, dalam ekspresi z.real, realadalah atribut objek z. Sebenarnya, referensi ke nama dalam modul adalah referensi atribut: dalam ekspresi modname.funcname, modnameadalah objek modul dan funcnamemerupakan atribut darinya. Dalam hal ini, kebetulan ada pemetaan langsung antara atribut modul dan nama global yang ditentukan dalam modul: mereka berbagi namespace yang sama!
Atribut mungkin hanya-baca atau dapat ditulis. Dalam kasus terakhir, penugasan ke atribut dimungkinkan. Atribut modul dapat ditulis: Anda dapat menulis . Atribut yang dapat ditulis juga dapat dihapus dengan pernyataan tersebut. Misalnya, akan menghapus atribut dari objek bernama by .modname.the_answer = 42deldel modname.the_answerthe_answermodname
Ruang nama dibuat pada momen yang berbeda dan memiliki masa hidup yang berbeda. Namespace yang berisi nama bawaan dibuat saat penerjemah Python dijalankan, dan tidak pernah dihapus. Namespace global untuk modul dibuat saat definisi modul dibaca; biasanya, ruang nama modul juga bertahan sampai penerjemah berhenti. Pernyataan yang dieksekusi oleh pemanggilan interpreter tingkat atas, baik dibaca dari file skrip atau secara interaktif, dianggap sebagai bagian dari modul yang dipanggil __main__, sehingga memiliki namespace global sendiri. (Nama built-in sebenarnya juga tinggal dalam modul; ini disebut builtins.)
Namespace lokal untuk suatu fungsi dibuat saat fungsi dipanggil, dan dihapus saat fungsi tersebut mengembalikan atau memunculkan pengecualian yang tidak ditangani di dalam fungsi tersebut. (Sebenarnya, melupakan akan menjadi cara yang lebih baik untuk menggambarkan apa yang sebenarnya terjadi.) Tentu saja, setiap pemanggilan rekursif memiliki namespace lokalnya sendiri.
Sebuah lingkup adalah wilayah tekstual dari program Python di mana namespace secara langsung dapat diakses. “Dapat diakses secara langsung” di sini berarti bahwa referensi yang tidak memenuhi syarat untuk suatu nama mencoba menemukan nama tersebut di namespace.
Meskipun cakupan ditentukan secara statis, cakupan digunakan secara dinamis. Kapan pun selama eksekusi, ada 3 atau 4 cakupan bersarang yang namespace-nya dapat langsung diakses:
•	lingkup paling dalam, yang dicari pertama kali, berisi nama-nama local
•	lingkup fungsi penutup apa pun, yang dicari dimulai dengan cakupan penutup terdekat, berisi nama non-lokal, tetapi juga non-global
•	cakupan berikutnya-ke-terakhir berisi nama global modul saat ini
•	ruang lingkup terluar (dicari terakhir) adalah namespace yang berisi nama bawaan
Jika sebuah nama dideklarasikan global, maka semua referensi dan tugas langsung menuju ke lingkup tengah yang berisi nama global modul. Untuk me-rebind variabel yang ditemukan di luar lingkup terdalam, nonlocalpernyataan dapat digunakan; jika tidak dideklarasikan nonlokal, variabel tersebut hanya-baca (upaya untuk menulis ke variabel seperti itu hanya akan membuat variabel lokal baru dalam cakupan paling dalam, membiarkan variabel luar yang dinamai identik tidak berubah)
Biasanya, lingkup lokal mereferensikan nama lokal dari fungsi (secara tekstual) saat ini. Di luar fungsi, lingkup lokal mereferensikan namespace yang sama dengan cakupan global: namespace modul. Definisi kelas menempatkan namespace lain dalam lingkup lokal.
Penting untuk disadari bahwa cakupan ditentukan secara tekstual: cakupan global dari suatu fungsi yang ditentukan dalam modul adalah namespace modul tersebut, tidak peduli dari mana atau oleh alias apa fungsi tersebut dipanggil. Di sisi lain, pencarian nama sebenarnya dilakukan secara dinamis, pada waktu proses - namun, definisi bahasa berkembang menuju resolusi nama statis, pada waktu "kompilasi", jadi jangan mengandalkan resolusi nama dinamis! (Faktanya, variabel lokal sudah ditentukan secara statis.)
Keunikan khusus Python adalah - jika tidak ada globalatau nonlocal pernyataan berlaku - penugasan ke nama selalu masuk ke cakupan terdalam. Tugas tidak menyalin data - tugas hanya mengikat nama ke objek. Hal yang sama juga berlaku untuk penghapusan: pernyataan tersebut menghapus pengikatan dari namespace yang dirujuk oleh cakupan lokal. Faktanya, semua operasi yang memperkenalkan nama baru menggunakan lingkup lokal: khususnya, pernyataan dan definisi fungsi mengikat nama modul atau fungsi dalam lingkup lokal.del xximport
Pernyataan global dapat digunakan untuk menunjukkan bahwa variabel tertentu hidup dalam lingkup global dan harus pulih di sana; yang nonlocalpernyataan menunjukkan bahwa variabel tertentu hidup di lingkup melampirkan dan harus rebound yang ada.
a.	Contoh Cakupan dan Namespaces
Ini adalah contoh yang menunjukkan cara mereferensikan cakupan dan namespace yang berbeda, dan bagaimana globalserta nonlocalmemengaruhi pengikatan variabel:
 
Perhatikan bagaimana penetapan lokal (yang default) tidak mengubah pengikatan spam scope_test . The tugas berubah scope_test ‘s pengikatan spam yang , dan tugas mengubah modul-tingkat mengikat.nonlocalglobal
Anda juga dapat melihat bahwa tidak ada pengikatan sebelumnya untuk spam sebelum globalpenetapan.

3.	Pandangan Pertama di Kelas
Kelas memperkenalkan sedikit sintaks baru, tiga tipe objek baru, dan beberapa semantik baru.
a.	Sintaks Definisi Kelas
Bentuk definisi kelas yang paling sederhana terlihat seperti ini:
 
Definisi kelas, seperti definisi fungsi ( defpernyataan) harus dijalankan sebelum memiliki efek apa pun. (Anda bisa menempatkan definisi kelas di cabang ifpernyataan, atau di dalam fungsi.)
Dalam praktiknya, pernyataan di dalam definisi kelas biasanya akan menjadi definisi fungsi, tetapi pernyataan lain diizinkan, dan terkadang berguna - kita akan kembali ke ini nanti. Definisi fungsi di dalam kelas biasanya memiliki bentuk daftar argumen yang khas, yang ditentukan oleh konvensi pemanggilan untuk metode - sekali lagi, ini akan dijelaskan nanti.
Saat definisi kelas dimasukkan, namespace baru dibuat, dan digunakan sebagai cakupan lokal - dengan demikian, semua tugas ke variabel lokal masuk ke namespace baru ini. Secara khusus, definisi fungsi mengikat nama fungsi baru di sini.
Ketika definisi kelas dibiarkan normal (melalui akhir), objek kelas dibuat. Ini pada dasarnya adalah pembungkus di sekitar konten namespace yang dibuat oleh definisi kelas; kita akan belajar lebih banyak tentang objek kelas di bagian selanjutnya. Cakupan lokal asli (yang berlaku tepat sebelum definisi kelas dimasukkan) dipulihkan, dan objek kelas di sini terikat ke nama kelas yang diberikan di header definisi kelas ( ClassNamedalam contoh).

b.	Objek Kelas
Objek kelas mendukung dua jenis operasi: referensi atribut dan instantiation.
Referensi atribut menggunakan sintaks standar yang digunakan untuk semua referensi atribut dengan Python: obj.name. Nama atribut yang valid adalah semua nama yang ada di namespace kelas saat objek kelas dibuat. Jadi, jika definisi kelas terlihat seperti ini:
 
lalu MyClass.idan MyClass.fmerupakan referensi atribut yang valid, masing-masing mengembalikan bilangan bulat dan objek fungsi. Atribut kelas juga dapat ditetapkan, sehingga Anda dapat mengubah nilai MyClass.iberdasarkan tugas. __doc__juga merupakan atribut yang valid, mengembalikan docstring milik kelas: ."A simple example class"
Instansiasi kelas menggunakan notasi fungsi. Anggap saja objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas. Misalnya (dengan asumsi kelas di atas):
 
membuat instance baru dari kelas dan menugaskan objek ini ke variabel lokal x.
Operasi instantiation ("memanggil" objek kelas) membuat objek kosong. Banyak kelas suka membuat objek dengan contoh yang disesuaikan dengan keadaan awal tertentu. Oleh karena itu kelas dapat mendefinisikan metode khusus bernama __init__(), seperti ini:
 
Ketika sebuah kelas mendefinisikan sebuah __init__()metode, __init__()pembuatan instance kelas secara otomatis memanggil instance kelas yang baru dibuat. Jadi dalam contoh ini, instance baru yang diinisialisasi dapat diperoleh dengan:
 
Tentu saja, __init__()metode tersebut mungkin memiliki argumen untuk fleksibilitas yang lebih besar. Dalam hal ini, argumen yang diberikan ke operator instance kelas diteruskan ke __init__(). Sebagai contoh,
 

c.	Objek Instance
Sekarang apa yang dapat kita lakukan dengan objek instance? Satu-satunya operasi yang dipahami oleh objek contoh adalah referensi atribut. Ada dua jenis nama atribut yang valid: atribut data dan metode.
atribut data sesuai dengan "variabel instan" di Smalltalk, dan "anggota data" di C ++. Atribut data tidak perlu dideklarasikan; seperti variabel lokal, variabel tersebut muncul saat pertama kali ditetapkan. Misalnya, jika xinstance MyClassdibuat di atas, potongan kode berikut akan mencetak nilai 16, tanpa meninggalkan jejak:
 
Jenis referensi atribut instance lainnya adalah metode . Metode adalah fungsi yang "dimiliki" suatu objek. (Dalam Python, istilah metode tidak unik untuk instance kelas: tipe objek lain juga dapat memiliki metode. Misalnya, objek daftar memiliki metode yang disebut append, insert, remove, sort, dan sebagainya. Namun, dalam pembahasan berikut, kita akan menggunakan istilah metode secara eksklusif untuk mengartikan metode objek instance kelas, kecuali secara eksplisit dinyatakan lain.)
Nama metode yang valid dari objek instance bergantung pada kelasnya. Menurut definisi, semua atribut kelas yang merupakan objek fungsi menentukan metode terkait dari instance-nya. Jadi dalam contoh kita, x.fadalah referensi metode yang valid, karena MyClass.fmerupakan fungsi, tetapi x.itidak, karena MyClass.ibukan. Tetapi x.ftidak sama dengan MyClass.f- ini adalah objek metode , bukan objek fungsi.


d.	Objek Metode
Biasanya, metode dipanggil tepat setelah terikat:
 
Dalam MyClasscontoh, ini akan mengembalikan string . Namun, tidak perlu langsung memanggil metode: merupakan objek metode, dan dapat disimpan dan dipanggil di lain waktu. Sebagai contoh:'hello world'x.f
 
akan terus mencetak hingga akhir waktu.hello world
Apa yang sebenarnya terjadi ketika sebuah metode dipanggil? Anda mungkin telah memperhatikan bahwa x.f()dipanggil tanpa argumen di atas, meskipun definisi fungsi untuk f()argumen yang ditentukan. Apa yang terjadi dengan argumen itu? Tentunya Python memunculkan pengecualian ketika fungsi yang membutuhkan argumen dipanggil tanpa ada - bahkan jika argumen sebenarnya tidak digunakan
Sebenarnya, Anda mungkin sudah menebak jawabannya: hal khusus tentang metode adalah bahwa objek instance dilewatkan sebagai argumen pertama dari fungsi tersebut. Dalam contoh kita, panggilan x.f()itu sama persis dengan MyClass.f(x). Secara umum, memanggil metode dengan daftar n argumen sama dengan memanggil fungsi terkait dengan daftar argumen yang dibuat dengan memasukkan objek instance metode sebelum argumen pertama.
Jika Anda masih tidak memahami cara kerja metode, melihat penerapannya mungkin dapat memperjelas masalah. Ketika atribut non-data dari sebuah instance direferensikan, kelas dari instance tersebut dicari. Jika nama menunjukkan atribut kelas yang valid yang merupakan objek fungsi, objek metode dibuat dengan mengemas (menunjuk ke) objek instance dan objek fungsi yang baru saja ditemukan bersama dalam objek abstrak: ini adalah objek metode. Ketika objek metode dipanggil dengan daftar argumen, daftar argumen baru dibuat dari objek contoh dan daftar argumen, dan objek fungsi dipanggil dengan daftar argumen baru ini.

e.	Variabel Kelas dan Instans
Secara umum, variabel instance adalah untuk data unik untuk setiap instance dan variabel kelas untuk atribut dan metode yang digunakan bersama oleh semua instance kelas:
 
Seperti yang dibahas dalam Kata Tentang Nama dan Objek , data bersama dapat memiliki efek yang mengejutkan dengan melibatkan objek yang bisa berubah seperti daftar dan kamus. Misalnya, daftar trik dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua instance Dog :
 
Desain kelas yang benar harus menggunakan variabel contoh sebagai gantinya:
 

4.	Komentar Acak
Jika nama atribut yang sama muncul di instance dan di kelas, maka pencarian atribut memprioritaskan instance tersebut:
 
Atribut data dapat dirujuk oleh metode serta oleh pengguna biasa ("klien") dari suatu objek. Dengan kata lain, kelas tidak dapat digunakan untuk mengimplementasikan tipe data abstrak murni. Faktanya, tidak ada dalam Python yang memungkinkan untuk memaksakan penyembunyian data - semuanya berdasarkan konvensi. (Di sisi lain, implementasi Python, yang ditulis dalam C, dapat sepenuhnya menyembunyikan detail implementasi dan mengontrol akses ke suatu objek jika perlu; ini dapat digunakan oleh ekstensi ke Python yang ditulis dalam C.)
Klien harus menggunakan atribut data dengan hati-hati - klien dapat mengacaukan invarian yang dipertahankan oleh metode dengan memberi cap pada atribut data mereka. Perhatikan bahwa klien dapat menambahkan atribut datanya sendiri ke objek instance tanpa memengaruhi validitas metode, selama konflik nama dihindari - sekali lagi, konvensi penamaan dapat menghemat banyak masalah di sini.
Tidak ada singkatan untuk mereferensikan atribut data (atau metode lain!) Dari dalam metode. Saya menemukan bahwa ini benar-benar meningkatkan keterbacaan metode: tidak ada kemungkinan membingungkan variabel lokal dan variabel instan saat melihat sekilas melalui suatu metode.
Seringkali, argumen pertama dari suatu metode dipanggil self. Ini tidak lebih dari sebuah konvensi: namanya selfsama sekali tidak memiliki arti khusus untuk Python. Namun, perhatikan bahwa dengan tidak mengikuti konvensi, kode Anda mungkin kurang dapat dibaca oleh programmer Python lain, dan juga dapat dibayangkan bahwa program browser kelas mungkin ditulis yang bergantung pada konvensi semacam itu.
Objek fungsi apa pun yang merupakan atribut kelas mendefinisikan metode untuk instance kelas itu. Definisi fungsi tidak perlu disertakan secara tekstual dalam definisi kelas: menetapkan objek fungsi ke variabel lokal di kelas juga diperbolehkan. Sebagai contoh:
 
Sekarang f, gdan hsemua atribut kelas Cyang merujuk ke objek fungsi, dan akibatnya mereka semua adalah metode instance C- hyang sama persis dengan g. Perhatikan bahwa praktik ini biasanya hanya berfungsi untuk membingungkan pembaca program.
Metode dapat memanggil metode lain dengan menggunakan atribut metode dari self argumen:
 
Metode dapat merujuk nama global dengan cara yang sama seperti fungsi biasa. Cakupan global yang terkait dengan metode adalah modul yang berisi definisinya. (Kelas tidak pernah digunakan sebagai cakupan global.) Meskipun orang jarang menemukan alasan yang baik untuk menggunakan data global dalam suatu metode, ada banyak penggunaan yang sah dari cakupan global: untuk satu hal, fungsi dan modul yang diimpor ke dalam cakupan global dapat digunakan oleh metode, serta fungsi dan kelas yang ditentukan di dalamnya. Biasanya, kelas yang berisi metode itu sendiri didefinisikan dalam cakupan global ini, dan di bagian selanjutnya kita akan menemukan beberapa alasan bagus mengapa metode ingin mereferensikan kelasnya sendiri.
Setiap nilai adalah objek, dan oleh karena itu memiliki kelas (juga disebut tipenya ). Itu disimpan sebagai object.__class__.

5.	Warisan / Inheritance
Tentu saja, fitur bahasa tidak akan layak disebut "kelas" tanpa mendukung pewarisan. Sintaks untuk definisi kelas turunan terlihat seperti ini:
 
Nama BaseClassNameharus ditentukan dalam lingkup yang berisi definisi kelas turunan. Sebagai pengganti nama kelas dasar, ekspresi arbitrer lainnya juga diperbolehkan. Ini dapat berguna, misalnya, ketika kelas dasar ditentukan di modul lain:
 
Eksekusi definisi kelas turunan hasil yang sama seperti untuk kelas dasar. Ketika objek kelas dibangun, kelas dasar akan diingat. Ini digunakan untuk menyelesaikan referensi atribut: jika atribut yang diminta tidak ditemukan di kelas, pencarian dilanjutkan untuk mencari di kelas dasar. Aturan ini diterapkan secara rekursif jika kelas dasar itu sendiri diturunkan dari kelas lain.
Tidak ada yang istimewa tentang instansiasi kelas turunan: DerivedClassName()membuat instance kelas baru. Referensi metode diselesaikan sebagai berikut: atribut kelas yang sesuai dicari, menuruni rantai kelas dasar jika perlu, dan referensi metode valid jika ini menghasilkan objek fungsi.
Kelas turunan dapat mengganti metode kelas dasarnya. Karena metode tidak memiliki hak istimewa khusus saat memanggil metode lain dari objek yang sama, metode kelas dasar yang memanggil metode lain yang ditentukan dalam kelas dasar yang sama mungkin akan memanggil metode kelas turunan yang menimpanya. (Untuk programmer C ++: semua metode dengan Python secara efektif virtual.)
Metode overriding dalam kelas turunan sebenarnya mungkin ingin memperluas daripada hanya mengganti metode kelas dasar dengan nama yang sama. Ada cara sederhana untuk memanggil metode kelas dasar secara langsung: panggil saja . Ini terkadang berguna untuk klien juga. (Perhatikan bahwa ini hanya berfungsi jika kelas dasar dapat diakses seperti dalam cakupan global.)BaseClassName.methodname(self, arguments)BaseClassName
Python memiliki dua fungsi bawaan yang bekerja dengan pewarisan:
•	Gunakan isinstance()untuk memeriksa tipe instance: akan menjadi hanya jika adalah atau beberapa kelas turunan dari .isinstance(obj, int)Trueobj.__class__intint
•	Gunakan issubclass()untuk memeriksa warisan kelas: adalah karena merupakan subkelas dari . Namun, adalah karena tidak subclass dari .issubclass(bool, int)Trueboolintissubclass(float, int)Falsefloatint

a.	Multiple Inheritance
Python mendukung bentuk multiple inheritance juga. Definisi kelas dengan beberapa kelas dasar terlihat seperti ini:
 
Untuk sebagian besar tujuan, dalam kasus yang paling sederhana, Anda dapat menganggap pencarian atribut yang diwarisi dari kelas induk sebagai kedalaman-pertama, kiri-ke-kanan, tidak mencari dua kali di kelas yang sama di mana ada tumpang tindih dalam hierarki. Jadi, jika atribut tidak ditemukan di DerivedClassName, itu dicari di Base1, kemudian (secara rekursif) di kelas dasar Base1, dan jika tidak ditemukan di sana, itu dicari di Base2, dan seterusnya.
Sebenarnya, ini sedikit lebih kompleks dari itu; urutan resolusi metode berubah secara dinamis untuk mendukung panggilan kooperatif super(). Pendekatan ini dikenal di beberapa bahasa pewarisan ganda lainnya sebagai metode panggilan-berikutnya dan lebih kuat daripada panggilan super yang ditemukan dalam bahasa pewarisan tunggal.
Pengurutan dinamis diperlukan karena semua kasus beberapa pewarisan menunjukkan satu atau beberapa hubungan berlian (di mana setidaknya satu kelas induk dapat diakses melalui beberapa jalur dari kelas paling bawah). Misalnya, semua kelas objectditurunkan dari , jadi setiap kasus beberapa warisan menyediakan lebih dari satu jalur untuk dijangkau object. Untuk menjaga agar kelas dasar tidak diakses lebih dari sekali, algoritme dinamis menyusun urutan pencarian dengan cara yang mempertahankan pengurutan kiri-ke-kanan yang ditentukan di setiap kelas, yang memanggil setiap induk hanya sekali, dan itu monotonik (artinya kelas dapat disubkelas tanpa mempengaruhi urutan prioritas dari orang tuanya). Secara keseluruhan, properti ini memungkinkan untuk mendesain kelas yang andal dan dapat diperluas dengan beberapa pewarisan.

6.	Variabel Pribadi
Variabel instance "Private" yang tidak dapat diakses kecuali dari dalam objek tidak ada di Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama yang diawali dengan garis bawah (misalnya _spam) harus diperlakukan sebagai bagian non-publik dari API (apakah itu fungsi, metode, atau anggota data). Ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.
Karena ada kasus penggunaan yang valid untuk anggota kelas-pribadi (yaitu untuk menghindari benturan nama nama dengan nama yang ditentukan oleh subkelas), ada dukungan terbatas untuk mekanisme seperti itu, yang disebut mangling nama . Setiap pengenal formulir __spam(setidaknya dua garis bawah di depan, paling banyak satu garis bawah) diganti secara tekstual dengan _classname__spam, di mana classnamenama kelas saat ini dengan garis bawah di depan dihilangkan. Mangling ini dilakukan tanpa memperhatikan posisi sintaksis pengenal, selama itu terjadi dalam definisi kelas.
Name mangling berguna untuk membiarkan subclass mengganti metode tanpa memutus panggilan metode intraclass. Sebagai contoh:
 
Contoh di atas akan berfungsi bahkan jika MappingSubclasskita memperkenalkan __updatepengenal karena diganti dengan _Mapping__updatedi Mappingkelas dan _MappingSubclass__updatedi MappingSubclass kelas masing-masing.
Perhatikan bahwa aturan pengrusakan sebagian besar dirancang untuk menghindari kecelakaan; masih memungkinkan untuk mengakses atau memodifikasi variabel yang dianggap privat. Ini bahkan bisa berguna dalam keadaan khusus, seperti di debugger.
Perhatikan bahwa kode yang diteruskan ke exec()atau eval()tidak menganggap nama kelas dari kelas pemanggilan menjadi kelas saat ini; ini mirip dengan efek dari globalpernyataan tersebut, yang efeknya juga terbatas pada kode yang dikompilasi bersama-sama. Pembatasan yang sama berlaku untuk getattr(), setattr()dan delattr(), serta saat merujuk __dict__secara langsung.

7.	Odds and Ends
Terkadang berguna untuk memiliki tipe data yang mirip dengan “record” Pascal atau “struct” C, menggabungkan beberapa item data bernama. Definisi kelas kosong akan bekerja dengan baik:
 
Sepotong kode Python yang mengharapkan tipe data abstrak tertentu sering kali dapat melewati kelas yang mengemulasi metode tipe data itu sebagai gantinya. Misalnya, jika Anda memiliki fungsi yang memformat beberapa data dari objek file, Anda dapat mendefinisikan kelas dengan metode read()dan readline()yang mendapatkan data dari buffer string sebagai gantinya, dan meneruskannya sebagai argumen.
Objek metode m.__self__instance juga memiliki atribut: adalah objek instance dengan metode tersebut m(), dan m.__func__merupakan objek fungsi yang sesuai dengan metode tersebut.

8.	Iterator
Sekarang Anda mungkin telah memperhatikan bahwa sebagian besar objek kontainer dapat diulang menggunakan forpernyataan:
 
Gaya akses ini jelas, ringkas, dan nyaman. Penggunaan iterator meliputi dan menyatukan Python. Di belakang layar, forpernyataan tersebut memanggil iter()objek kontainer. Fungsi mengembalikan objek iterator yang mendefinisikan metode __next__()yang mengakses elemen dalam penampung satu per satu. Ketika tidak ada lagi elemen, __next__()memunculkan StopIterationpengecualian yang memberitahu forloop untuk berhenti. Anda dapat memanggil __next__()metode menggunakan fungsi next()built-in; contoh ini menunjukkan bagaimana semuanya bekerja:
 
Setelah melihat mekanisme di balik protokol iterator, mudah untuk menambahkan perilaku iterator ke kelas Anda. Tentukan __iter__()metode yang mengembalikan objek dengan __next__()metode. Jika kelas mendefinisikan __next__(), maka __iter__()dapat mengembalikan self:
 

9.	Generators
Generator adalah alat sederhana dan kuat untuk membuat iterator. Mereka ditulis seperti fungsi biasa tetapi menggunakanyieldpernyataan kapan pun mereka ingin mengembalikan data. Setiap kalinext()dipanggil, generator melanjutkan di mana ia tinggalkan (ia mengingat semua nilai data dan pernyataan mana yang terakhir dieksekusi). Sebuah contoh menunjukkan bahwa generator dapat dibuat dengan sangat mudah:
 
Apa pun yang bisa dilakukan dengan generator juga bisa dilakukan dengan iterator berbasis kelas seperti yang dijelaskan di bagian sebelumnya. Apa yang membuat generator begitu kompak adalah metode __iter__()dan __next__()dibuat secara otomatis.
Fitur utama lainnya adalah variabel lokal dan status eksekusi secara otomatis disimpan di antara panggilan. Ini membuat fungsi lebih mudah untuk ditulis dan lebih jelas daripada pendekatan yang menggunakan variabel instan seperti self.index dan self.data.
Selain pembuatan metode otomatis dan status program penyimpanan, ketika generator dihentikan, mereka secara otomatis naik StopIteration. Dalam kombinasi, fitur-fitur ini memudahkan pembuatan iterator tanpa perlu lebih banyak usaha daripada menulis fungsi biasa.

10.	Generator Expressions
Beberapa generator sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaks yang mirip dengan pemahaman daftar tetapi dengan tanda kurung, bukan tanda kurung siku. Ekspresi ini dirancang untuk situasi di mana generator digunakan langsung oleh fungsi penutup. Ekspresi generator lebih kompak tetapi kurang fleksibel dibandingkan definisi generator lengkap dan cenderung lebih ramah memori daripada pemahaman daftar yang setara.
