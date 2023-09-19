Nama   : Devandra Reswara Arkananta <br>
Kelas  : PBP-F

link app adaptable : [devandra-tugas2](https://devandra-tugas2.adaptable.app/main)

<details>
   <summary>Tugas 2</summary>
   Jawaban Pertanyaan

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
   Jawab : <br>
   Pertama saya akan membuat project django baru di dalam virtual environment, lalu membuat directory baru bernama main di dalamnya, pada url di direktori utama, kita routing main sebagai main dapat berjalan. Di    dalam model kita tambahkan atribut yang dinginkan, lalu views kita tambahkan file html yang akan dikembalikan sebagai template untuk ditampilkan pada pengguna. dari url di dalam main juga kita routing view.      setelah itu aplikasi dapat di deploy.
   <br>
   
3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. <br>
   Jawab : <br>
   ![Bagan Django](https://github.com/DevandraR/Devandra_Tugas2/assets/96380686/b6dd97b0-f46d-4a78-87dd-92b5ef7abb78)
   <br>

4. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>
   Jawab :  <br>
   virtual environment pada python digunakan untuk memisahkan package yang di install pada project dari data lainnya, memisahkan package dan dependency yang diinstall agar tidak terjadi tabrakan antar project.      kita tetap bisa membuat app django tanpa virtual environment, namun package python kemungkinan besar akan menjadi berantakan.
   <br>

6. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. <br>
   Jawab : <br>
   a. MVC (Model-View-Controller) <br>
      Pada MVC, user berinteraksi dengan view, yang meneruskan request kepada controller, lalu controller mengupdate model dan view sesuai dengan modelnya. <br>
   b. MVT (Model-View-Template) <br>
      Pada MVT, biasanya request diterima oleh URL routing, lalu requestnya akan dijalankan ke directory view yang ingin ditampilkan, dan model juga menerima request sesuai ketentuan. Lalu view akan memberikan         template yang berupa file html yang akan ditampilkan ke user. <br>
   c. MVVM (Model-View-ViewModel) <br>
      Pada MVVM, view dikendalikan oleh viewmodel, jadi jika ada perubahan pada model, viewmodel akan langsung merespon dengan mengubah view. jadi perbedaannya adalah dalam interface dengan view dan modelnya MVC       menggunakan controller, MVT menggunakan url, MVVM menggunakan viewmodel.<br>
</details>

<details>
   <summary>Tugas 3</summary>
   Jawaban Pertanyaan
   
1. Apa perbedaan antara form POST dan form GET dalam Django? <br>
   Jawab : <br>
      
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data? <br>
   Jawab : <br>
   
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? <br>
   Jawab : <br>
   
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
   Jawab : <br>
   
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
