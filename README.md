# Template Proyek Django PBP
Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023


## Pendahuluan
Proyek ini dibuat dalam memenuhi tugas Proyek Tengah Semester (PTS) pada mata kuliah Pemrograman Berbasis Platform (CSGE602022) yang diselenggarakan oleh Fakultas Ilmu Komputer, Universitas Indonesia pada Semester Gasal, Tahun Ajaran 2022/2023.

## Nama-nama Anggota Kelompok
1. [Amanda Nurul Izzah - 2106634080](https://github.com/amrul-hzz)
2. [Fadlan Ariel Fathurrahman - 2106750673](https://github.com/fadlanariel)
3. [James Smith Wigglesworth - 2106750225](https://github.com/jamessmith404)
4. [Maysha Haliza Kirana - 2106751202](https://github.com/mayshahaliza)
5. [Michael Christlambert Sinanta - 2106750414](https://github.com/michaelsinanta)
6. [Yeira Putri Nandika - 2106751726](https://github.com/yeiraputri)

## Tautan Aplikasi Heroku
https://github.com/amrul-hzz/tugas-kelompok-c03 

## Cerita Aplikasi
Masalah lingkungan sudah sangat parah belakangan ini. Di Indonesia, penumpukan sampah serta pembuangan sampah sembarangan menjadi permasalahan utama yang terjadi. Berdasarkan data Indonesia National Plastic Action Partnership yang dirilis April 2020, sebanyak 67,2 juta ton sampah Indonesia masih menumpuk setiap tahunnya, dan 9 persennya atau sekitar 620 ribu ton masuk ke sungai, danau dan laut. Hal tersebut pasti akan membawa dampak buruk kepada makhluk hidup. Maka dari itu isu tersebut difokuskan ke dalam G20 yang membahas mengenai Sustainability.<br>
Masalah sampah tidak kunjung selesai akibat dari minimnya rasa tanggung jawab dan kesadaran diri masing-masing. Dalam mencoba untuk meningkatkan rasa tersebut, kelompok kami memfokuskan dalam membersihkan sampah di sungai maupun pantai dengan cara yang menyenangkan. Kelompok kami ingin membuat web yang di dalamnya berisikan jadwal dan tempat dari event pembersihan sampah disertai achievements ketika pengguna mengikuti event yang ada. Di web kami juga akan terdapat forum dimana para pengguna dapat mengekspresikan diri mereka saat mengikuti event tersebut. Diharapkan web ini akan menumbuhkan rasa ingin masyarakat dalam berkontribusi dalam memelihara lingkungan hidup.

## Daftar Modul yang Akan Diimplementasikan
1. Landing Page\
Modul ini merupakan tampilan pertama yang dilihat oleh user saat membuka website. User dapat melihat profil dari perusahaan kita, visi dan misi perusahaan, serta event-event pembersihan pantai yang sedang berjalan. Lalu, terdapat button untuk login dan register akun.
2. Login + Register\
Modul ini berisi login yang meminta user untuk memberikan username dan password yang telah didaftarkan sebelumnya pada saat register. Register akan meminta calon user untuk mengisi informasi seperti nama, alamat email, nomor telepon, dan alamat tinggal.
3. Timeline\
Modul ini akan menampilkan event-event apa saja yang akan berlangsung. Event tersebut akan menjelaskan pantai apa yang akan dibersihkan, alamat pantai, tanggal mulai hingga tanggal penutupan acara, serta kapasitas orang yang dibutuhkan untuk membantu pembersihan pantai.
4. Create Event\
Modul ini digunakan admin untuk mengunggah event pembersihan pantai dengan mengisi form yang terdiri dari nama pantai, alamat pantai, foto kondisi pantai, penjelasan mengapa pantai pantas untuk dibersihkan, tanggal mulai hingga tanggal penutupan acara, serta kapasitas orang yang dibutuhkan untuk membantu pembersihan pantai. Event yang diunggah akan muncul di Timeline.
5. Forum\
Modul yang berisi forum pembicaraan dan diskusi antara user. User dapat mengunggah komentar berisi teks maupun foto sehingga membuat sebuah forum baru. User lain dapat membalas forum tersebut serta saling membalas satu sama lain. 
6. My Account\
Modul ini akan menampilkan profil user yang berisi thread yang mereka sebelumnya buat, pencapaian-pencapaian saat mereka menyelesaikan event (jika admin memberikan badge), dan event-event yang telah mereka tempuh sebelumnya.
7. Leaderboard\
Modul ini berisi halaman papan peringkat yang akan menampilkan user dengan point tertinggi. Point diberikan oleh admin jika admin merasa bahwa user secara valid menjalani event sesuai dengan aturan yang berlaku. 

## Role atau peran pengguna beserta deskripsinya
1. Role Admin
- Semua modul yang dapat diakses guest user dan logged-in user dapat diakses oleh admin.
- Mengakses modul Create Event.
- Memberikan point untuk logged-in user.
2. Role Guest User (Non Logged In)
- Mengakses modul Landing Page.
- Mengakses modul Register dan Login.
- Mengakses modul TimeLine dan jika meng-klik timeline tersebut, user akan di-redirect ke modul Register dan Login.
- Mengakses modul Leaderboard.
3. Role Logged In User
- Semua modul yang dapat diakses guest user dapat diakses oleh logged-in user.
- Mengakses modul My Account.
- Mengakses modul Forum dan memberikan komentar.
- Dapat mendaftarkan diri ke event di modul TimeLine.

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
