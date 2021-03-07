Modul
LINK GitHub : https://github.com/aziz23598/workshop-python 
Modul adalah sebuah file yang berisi kode pemrograman python. Sebuah file yang berisi kode python, misalnya : fibo.py, disebut modul dan nama modulnya adalah fibo.
Modul digunakan untuk memecah sebuah program besar menjadi file-file yang lebih kecil agar lebih mudah dimanage dan diorganisir. Modul membuat kode bersifat reusable, artinya satu modul bisa dipakai berulang dimana saja diperlukan.
Modul tidak lain adalah program python biasa. Berikut ini kita mencoba membuat sebuah modul. Kita akan simpan dengan nama fibo.py
 

Kita bisa mengimpor modul python ke dalam program yang kita buat. Dengan mengimpor modul, maka definisi, variabel, fungsi dan yang lainnya yang ada di dalam modul itu bisa kita pergunakan.
Kita mengimpor modul dengan menggunakan kata kunci import. Misalnya, kita akan mengimpor modul fibo yang sudah kita buat di atas, maka kita bisa mengetikkan perintah berikut di IDLE maupun di command prompt.
 
Setelah kita import, maka kita bisa mengakses isi dari modul fibo. Kita bisa mengakses fungsi maupun variabel global di dalam modul dengan menggunakan operasi titik (.). Misalnya adalah sebagai berikut:
 

1.	Lebih lanjut tentang modul
Ada tipe import yang mengimport salah satu fungsi dengan memanggil nama variable dari sebuah modul. Perintahnya from nama_modul import nama_fungsi
 
Kemudian kita bisa juga mengimport seluruh fungsi yang ada di modul dengan perintah from nama_modul import *.
 

Kemudian ada cara import dengan rename(alias), perintahnya import nama_modul as alias. Atau juga bisa from nama_modul import nama_fungsi as alias.
 

Saat kita menjalankan modul python dengan perintah python fibo.py <arguments>, maka kode didalam modul akan dijalankan. Sama seperti ketika kita mengimportnya, tetapi dengan __name__ di set ke “__main__”. Itu berarti dengan menambahkan kode ini di akhir modul kita.
 

Kita dapat membuat file menggunkan sebuah script serta modul yang dapat diimpor, karena kode yang mengurai baris perintah hanya berjalan jika modul dijalankan sebagai file “utama”.
 

Ketika sebuah modul bernama spam diimpor, penerjemah pertama-tama mencari modul bawaan dengan nama itu. Jika tidak ditemukan, kemudian mencari file bernama spam.py dalam daftar direktori yang diberikan oleh variabel sys.path. sys.path diinisialisasi dari lokasi berikut:
•	Direktori yang berisi skrip input (atau direktori saat ini jika tidak ada file yang ditentukan).
•	PYTHONPATH (daftar nama direktori, dengan sintaks yang sama dengan variabel shell PATH).
•	Default yang bergantung pada penginstalan.
Setelah inisialisasi, program Python dapat memodifikasi sys.path. Direktori yang berisi skrip yang sedang dijalankan ditempatkan di awal jalur pencarian, di depan jalur pustaka standar. Ini berarti bahwa skrip di direktori itu akan dimuat alih-alih modul dengan nama yang sama di direktori perpustakaan. Ini adalah kesalahan kecuali penggantinya memang dimaksudkan.
Untuk mempercepat pemuatan modul, Python menyimpan cache versi terkompilasi dari setiap modul dalam __pycache__direktori di bawah nama , di mana versi tersebut mengkodekan format file yang dikompilasi; itu biasanya berisi nomor versi Python. Misalnya, dalam rilis CPython 3.3 versi terkompilasi dari spam.py akan di-cache sebagai . Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis berbeda dan versi berbeda dari Python untuk hidup berdampingan.module.version.pyc__pycache__/spam.cpython-33.pyc
Python memeriksa tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat apakah itu sudah kadaluwarsa dan perlu dikompilasi ulang. Ini adalah proses yang sepenuhnya otomatis. Selain itu, modul yang dikompilasi tidak bergantung pada platform, sehingga pustaka yang sama dapat dibagikan di antara sistem dengan arsitektur berbeda.
Python tidak memeriksa cache dalam dua keadaan. Pertama, ini selalu mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah. Kedua, tidak memeriksa cache jika tidak ada modul sumber. Untuk mendukung distribusi non-sumber (hanya yang dikompilasi), modul yang dikompilasi harus berada dalam direktori sumber, dan tidak boleh ada modul sumber.
Beberapa tips untuk para ahli:
•	Anda dapat menggunakan sakelar -Oatau -OOpada perintah Python untuk mengurangi ukuran modul yang dikompilasi. The -Oberalih Menghapus menegaskan pernyataan, yang -OOberalih menghilangkan kedua pernyataan menegaskan dan __doc__ string. Karena beberapa program mungkin mengandalkan ketersediaan ini, Anda sebaiknya hanya menggunakan opsi ini jika Anda tahu apa yang Anda lakukan. Modul "Dioptimalkan" memiliki opt-tag dan biasanya lebih kecil. Rilis di masa mendatang dapat mengubah efek pengoptimalan.
•	Sebuah program tidak berjalan lebih cepat saat dibaca dari .pyc file daripada saat dibaca dari .pyfile; satu-satunya hal yang lebih cepat tentang .pycfile adalah kecepatan pemuatannya.
•	Modul ini compilealldapat membuat file .pyc untuk semua modul dalam sebuah direktori.
•	Ada lebih banyak detail tentang proses ini, termasuk diagram alir keputusan, di PEP 3147 .

2.	Modul standar
Python hadir dengan perpustakaan modul standar, dijelaskan dalam dokumen terpisah, Referensi Perpustakaan Python ("Referensi Perpustakaan" selanjutnya). Beberapa modul dibangun ke dalam interpreter; ini menyediakan akses ke operasi yang bukan merupakan bagian dari inti bahasa tetapi tetap ada di dalamnya, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti panggilan sistem. Kumpulan modul semacam itu adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. Misalnya, winregmodul hanya tersedia di sistem Windows. Satu modul tertentu membutuhkan perhatian:, sysyang dibangun ke dalam setiap interpreter Python. Variabel sys.ps1dan sys.ps2tentukan string yang digunakan sebagai petunjuk utama dan sekunder:
 

Kedua variabel ini hanya ditentukan jika interpreter dalam mode interaktif.

Variabel sys.pathadalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkunganPYTHONPATH, atau dari bawaan bawaan if PYTHONPATHtidak disetel. Anda dapat memodifikasinya menggunakan operasi daftar standar:
 

3.	Fungsi dir()
Fungsi built-in dir()digunakan untuk mencari tahu nama mana yang didefinisikan oleh modul. Ini mengembalikan daftar string yang diurutkan:
 

Tanpa argumen, dir()daftar nama yang telah Anda tentukan saat ini:
 

Perhatikan bahwa ini mencantumkan semua jenis nama: variabel, modul, fungsi, dll.

dir()tidak mencantumkan nama fungsi dan variabel bawaan. Jika Anda menginginkan daftarnya, mereka ditentukan dalam modul standar builtins:
 

4.	Paket
Paket adalah cara untuk menyusun namespace modul Python dengan menggunakan "nama modul bertitik". Misalnya, nama modul A.Bmenunjukkan submodul yang diberi nama Bdalam paket bernama A. Sama seperti penggunaan modul, pembuat modul yang berbeda tidak perlu khawatir tentang nama variabel global satu sama lain, penggunaan nama modul bertitik membuat penulis paket multi-modul seperti NumPy atau Pillow tidak perlu khawatir tentang nama modul satu sama lain. .
Misalkan Anda ingin mendesain kumpulan modul ("paket") untuk penanganan file suara dan data suara yang seragam. Ada berbagai format file suara (biasanya diakui oleh ekstensi mereka, misalnya: .wav, .aiff, .au), sehingga Anda mungkin perlu untuk membuat dan memelihara koleksi tumbuh modul untuk konversi antara berbagai format file. Ada juga banyak operasi berbeda yang mungkin ingin Anda lakukan pada data suara (seperti mencampur, menambahkan gema, menerapkan fungsi equalizer, membuat efek stereo buatan), jadi selain itu Anda akan menulis aliran modul yang tidak pernah berakhir untuk dilakukan. operasi ini. Berikut adalah struktur yang mungkin untuk paket Anda (dinyatakan dalam sistem file hierarki):
 
Saat mengimpor paket, Python mencari melalui direktori untuk sys.pathmencari subdirektori package.
The __init__.pyfile yang diperlukan untuk membuat Python memperlakukan direktori yang berisi file seperti paket. Ini mencegah direktori dengan nama umum, seperti string, secara tidak sengaja menyembunyikan modul valid yang muncul kemudian di jalur pencarian modul. Dalam kasus yang paling sederhana, __init__.pydapat berupa file kosong, tetapi juga dapat menjalankan kode inisialisasi untuk paket atau mengatur __all__variabel, dijelaskan nanti.
Pengguna paket dapat mengimpor modul individu dari paket, misalnya:
 

Ini memuat submodul sound.effects.echo. Itu harus direferensikan dengan nama lengkapnya.
 

Cara alternatif untuk mengimpor submodul adalah:
 

Ini juga memuat submodul echo, dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan sebagai berikut:
 

Variasi lain adalah mengimpor fungsi atau variabel yang diinginkan secara langsung:
 

Sekali lagi, ini memuat submodul echo, tetapi ini membuat fungsinya echofilter()langsung tersedia:
 

Perhatikan bahwa saat menggunakan , item dapat berupa submodul (atau subpaket) dari paket, atau nama lain yang ditentukan dalam paket, seperti fungsi, kelas, atau variabel. The Pernyataan pertama menguji apakah item tersebut didefinisikan dalam paket; jika tidak, ia menganggap itu adalah modul dan mencoba memuatnya. Jika gagal menemukannya, pengecualian akan dimunculkan.from package import itemimportImportError
Sebaliknya, saat menggunakan sintaks seperti , setiap item kecuali yang terakhir harus berupa paket; item terakhir dapat berupa modul atau paket tetapi tidak dapat berupa kelas atau fungsi atau variabel yang ditentukan dalam item sebelumnya.import item.subitem.subsubitem
Sekarang apa yang terjadi saat pengguna menulis ? Idealnya, orang akan berharap bahwa ini entah bagaimana keluar ke sistem file, menemukan submodul mana yang ada dalam paket, dan mengimpor semuanya. Ini bisa memakan waktu lama dan mengimpor sub-modul mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika sub-modul diimpor secara eksplisit.from sound.effects import *
Satu-satunya solusi adalah pembuat paket menyediakan indeks paket secara eksplisit. The importpernyataan menggunakan konvensi berikut: jika paket ini __init__.pykode mendefinisikan daftar nama __all__, itu diambil untuk menjadi daftar nama modul yang harus diimpor saat ditemui. Terserah pembuat paket untuk membuat daftar ini tetap mutakhir ketika versi baru dari paket dirilis. Pembuat paket juga dapat memutuskan untuk tidak mendukungnya, jika mereka tidak melihat penggunaan untuk mengimpor * dari paket mereka. Misalnya, file dapat berisi kode berikut:from package import *sound/effects/__init__.py
 

Ini berarti itu akan mengimpor tiga submodul bernama dari paket.from sound.effects import *sound
Jika __all__tidak ditentukan, pernyataan tersebut tidak mengimpor semua submodul dari paket ke dalam namespace saat ini; itu hanya memastikan bahwa paket telah diimpor (mungkin menjalankan kode inisialisasi apa pun ) dan kemudian mengimpor nama apa pun yang ditentukan dalam paket. Ini termasuk nama apa pun yang ditentukan (dan submodul dimuat secara eksplisit) oleh . Ini juga mencakup semua submodul dari paket yang secara eksplisit dimuat oleh pernyataan sebelumnya . Pertimbangkan kode ini: from sound.effects import *sound.effectssound.effects__init__.py__init__.py import
 

Dalam contoh ini, modul echodan surrounddiimpor di namespace saat ini karena ditentukan dalam sound.effectspaket saat from...importpernyataan dijalankan. (Ini juga berfungsi saat __all__ditentukan.)
Meskipun modul tertentu dirancang untuk mengekspor hanya nama yang mengikuti pola tertentu saat Anda menggunakannya , ini masih dianggap praktik yang buruk dalam kode produksi.import *
Ingat, tidak ada salahnya menggunakan ! Nyatanya, ini adalah notasi yang direkomendasikan kecuali modul importing perlu menggunakan submodul dengan nama yang sama dari paket yang berbeda.from package import specific_submodule
Saat paket disusun menjadi subpaket (seperti soundpaket dalam contoh), Anda bisa menggunakan impor absolut untuk merujuk ke submodul paket saudara. Misalnya, jika modul sound.filters.vocoderperlu menggunakan echomodul dalam sound.effectspaket, ia dapat menggunakan .from sound.effects import echo

Anda juga dapat menulis impor relatif, dengan bentuk pernyataan impor. Impor ini menggunakan titik-titik terdepan untuk menunjukkan paket saat ini dan induk yang terlibat dalam impor relatif. Dari modul misalnya, Anda dapat menggunakan:from module import namesurround
 

Perhatikan bahwa impor relatif didasarkan pada nama modul saat ini. Karena nama modul utama selalu "__main__", modul yang dimaksudkan untuk digunakan sebagai modul utama aplikasi Python harus selalu menggunakan impor absolut.
Paket mendukung satu atribut khusus lagi __path__,. Ini diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan paket __init__.pysebelum kode dalam file itu dijalankan. Variabel ini dapat dimodifikasi; hal itu memengaruhi pencarian modul dan sub-paket di masa mendatang yang terdapat dalam paket.
Meskipun fitur ini tidak sering dibutuhkan, fitur ini dapat digunakan untuk memperluas kumpulan modul yang ditemukan dalam sebuah paket.
