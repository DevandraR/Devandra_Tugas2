Nama   : Devandra Reswara Arkananta <br>
Kelas  : PBP-F

link app adaptable : [devandra-tugas2](https://devandra-tugas2.adaptable.app/main)

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
