Nama   : Devandra Reswara Arkananta <br>
Kelas  : PBP-F

link app adaptable : [devandra-tugas2](https://devandra-tugas2.adaptable.app/main)

<details>
   <summary>Tugas 2</summary>
   Jawaban Pertanyaan

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
   Jawab : <br>
   Pertama saya akan membuat project django baru di dalam virtual environment, lalu membuat directory baru bernama main di dalamnya, pada url di direktori utama, kita routing main sebagai main dapat berjalan. Di dalam model kita tambahkan atribut yang dinginkan, lalu views kita tambahkan file html yang akan dikembalikan sebagai template untuk ditampilkan pada pengguna. dari url di dalam main juga kita routing view. setelah itu aplikasi dapat di deploy.
   <br>
   
3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. <br>
   Jawab : <br>
   ![Bagan Django](https://github.com/DevandraR/Devandra_Tugas2/assets/96380686/b6dd97b0-f46d-4a78-87dd-92b5ef7abb78)
   <br>

4. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>
   Jawab :  <br>
   virtual environment pada python digunakan untuk memisahkan package yang di install pada project dari data lainnya, memisahkan package dan dependency yang diinstall agar tidak terjadi tabrakan antar project. kita tetap bisa membuat app django tanpa virtual environment, namun package python kemungkinan besar akan menjadi berantakan.
   <br>

6. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. <br>
   Jawab : <br>
   a. MVC (Model-View-Controller) <br>
      Pada MVC, user berinteraksi dengan view, yang meneruskan request kepada controller, lalu controller mengupdate model dan view sesuai dengan modelnya. <br>
   b. MVT (Model-View-Template) <br>
      Pada MVT, biasanya request diterima oleh URL routing, lalu requestnya akan dijalankan ke directory view yang ingin ditampilkan, dan model juga menerima request sesuai ketentuan. Lalu view akan memberikan template yang berupa file html yang akan ditampilkan ke user. <br>
   c. MVVM (Model-View-ViewModel) <br>
      Pada MVVM, view dikendalikan oleh viewmodel, jadi jika ada perubahan pada model, viewmodel akan langsung merespon dengan mengubah view. jadi perbedaannya adalah dalam interface dengan view dan modelnya MVC menggunakan controller, MVT menggunakan url, MVVM menggunakan viewmodel.<br>
</details>

<details>
   <summary>Tugas 3</summary>
   Jawaban Pertanyaan
   
1. Apa perbedaan antara form POST dan form GET dalam Django? <br>
   Jawab : <br>
   form POST digunakan saat kita ingin mengirim sesuatu ke dalam server yang akan mengubah status sebuah server atau melakukan sesuatu, seperti menyimpan data ke database. form GET digunakan saat kita ingin mengirim data ke server sebagai suatu input untuk parameter, jadi GET tidak akan mengubah status pada server. <br>
   
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data? <br>
   Jawab : <br>
   HTML digunakan untuk mendeskripsikan bagaimana data akan ditampilkan di dalam aplikasi karena HTML dirancang untuk dirender di dalam browser web, JSON digunakan untuk penukaran data antara server dan client, dan XML digunakan untuk menentukan hierarki dan struktur data. <br>
   
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? <br>
   Jawab : <br>
   JSON sering digunakan karena ukurannya datanya yang ringan dan struktur key-valuenya yang mudah dibaca dan ditulis oleh manusia, JSON juga sangatlah cocok dengan JavaScript, bahasa pemrograman yang menguasai hampir seluruh hal di web, karena JavaScript sudah ada fungsi bawaan untuk parsing dan generate JSON. <br>
   
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
   Jawab : <br>
   Pertama, kita buat sebuah file HTML untuk menjadi template tampilan pada aplikasi. lalu kita membuat form untuk menerima input data, lalu pada views, kita akan membuat fungsi baru yang dapat menerima request dan menambahkan input data. lalu kita tambahkan fungsi yang kita buat ke url agar dapat diakses. untuk HTML kita akan membuat file HTML baru untuk menampung seluruh input dan menampilkannya, dan untuk JSON dan XML kita dapat membuat fungsi yang khusus di views lalu menambahkan ke url. <br>
   
   Postman HTML <br>
   ![Postman_HTML_Tugas3](https://github.com/DevandraR/Devandra_Tugas2/assets/96380686/1f43d95f-2d73-4b0e-aa19-e43ff8a04c23) <br>

   Postman XML <br>
   ![Postman_XML_Tugas3](https://github.com/DevandraR/Devandra_Tugas2/assets/96380686/33410498-edd1-49aa-9e51-054c0637a921) <br>

   Postman JSON <br>
   ![Postman_JSON_Tugas3](https://github.com/DevandraR/Devandra_Tugas2/assets/96380686/dbf967d2-9807-4375-9074-e3228938dd4a) <br>

   Postman XML id <br>
   ![Postman_XML_id_Tugas3](https://github.com/DevandraR/Devandra_Tugas2/assets/96380686/aaff5ee4-d221-439a-8996-e318ef03542d) <br>

   Postman JSON id <br>
   ![Postman_JSON_id_Tugas3](https://github.com/DevandraR/Devandra_Tugas2/assets/96380686/bae3c038-0909-4f6b-bb58-8703bca9eb5d) <br>

</details>

<details>
   <summary>Tugas 4</summary>
   Jawaban Pertanyaan
   
1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya? <br>
   Jawab : <br>
   UserCreationForm adalah form input untuk pendaftaran user di web, dan sudah menjadi bawaan di django. UserCreationForm memiliki fungsi bawaan seperti validasi password untuk menentukan password yang aman. Kelebihan dari UserCreationForm adalah seperti yang disebutkan tadi, yaitu lebih praktis karena sudah ada fitur bawaan yang sudah bisa kita langsung pakai tanpa harus ngoding ulang. Kekurangannya adalah UserCreationForm hanya bisa dipakai pada kasus umum saja, jika ingin mengubah format atau tampilan, maka harus membuat form manual, ditambah lagi jika ingin membuat validasi khusus, lebih baik cara lain. <br>
   
2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting? <br>
   Jawab : <br>
   Autentikasi adalah proses menentukan identitas pengguna apakah mereka adalah orang yang sama dengan orang yang awal mendaftar, jadi autentikasi memeriksa apakah pengguna asli atau tidak. Sementara itu, Otorisasi adalah penentuan daerah akses oleh setiap pengguna, jadi menentukan bagian mana saja pada aplikasi yang dapat diakses oleh pengguna. Keduanya harus diimplementasikan secara baik untuk menjadi keamanan dan kenyamanan pengguna aplikasi. <br>
   
3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna? <br>
   Jawab : <br>
   cookies adalah data yang dikirim dari server ke lokal, contohnya seperti, kita dapat login otomatis di sebuah aplikasi tanpa memasukkan kembali username dan password. Pada sesi pengguna, saat terakhir login, Django akan menyimpan waktu login dengan fungsi set_cookies, lalu dapat ditampiklkan kembali menggunakan fungsi get
   
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? <br>
   Jawab : <br>
   resiko pada penggunaan cookies contohnya adalah salah satunya adalah penyadapan data, karena cookies yang dikirim tidak ada enkripsi, ini membuatnya rentan jika ada dalam koneksi yang tidak aman, lalu ada cross site scripting, ini adalah serangan berbahaya yang serangannya adalah memmasukkan skrip berbahaya ke dalam cookies pengguna, lalu dapat dijalankan oleh pengguna.
   
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
   Jawab : <br>
   yang pertama, kita buat bagian registrasi dan loginnyanya dengan menambahkan fungsi registrasi dan login di views, membuat template registrasi dan login lalu routing di url. Yang kedua, kita juga buat fungsi logout dengan menambahkan fungsi di views dan menambah tombol logout di templatenya, lalu routing di url. Yang ketiga kita dapat merestriksi akses pada main dengan menambahkan login_required. Yang keempat, kita akan menyimpan data waktu saat login dan menampilkannya saat selanjutnya menggunakan cookies. Dan yang terakhir kita dapat menghubungkan user dengan item yang ada.
   
</details>
