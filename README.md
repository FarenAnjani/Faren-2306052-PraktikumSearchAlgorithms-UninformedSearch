# 📌 Pencarian Jalur dalam Graf (BFS, DFS, UCS)

Repo ini berisi implementasi tiga algoritma pencarian jalur dalam graf: **Breadth-First Search (BFS), Depth-First Search (DFS), dan Uniform Cost Search (UCS)**. Setiap algoritma memiliki cara kerja yang berbeda dalam mencari jalur dari satu simpul ke simpul tujuan.

---

## 🔍 1. Breadth-First Search (BFS)
**➡️ Fungsi utama:**
Mencari jalur **terpendek dalam graf tanpa bobot** menggunakan strategi pencarian **lebar dahulu**.

**📌 Cara kerja:**
- BFS menggunakan **queue (FIFO - First In, First Out)** untuk mengeksplorasi semua tetangga dari suatu simpul sebelum berpindah ke simpul lain.
- Memulai dari **simpul awal**, menandainya sebagai **terkunjungi**, dan memasukkan ke dalam antrean.
- Mengeksplorasi **simpul yang terhubung langsung** satu per satu.
- Jika **simpul tujuan ditemukan**, program akan mencetak jalur yang ditempuh.
- Jika tidak ada jalur, program menampilkan bahwa jalur tidak ditemukan.

**✅ Kapan BFS digunakan?**  
- Saat mencari **jalur terpendek dalam graf tanpa bobot**.
- Saat melakukan **pencarian dalam jaringan atau sistem yang luas** seperti sosial media dan pencarian rute dalam peta.

---

## 🔍 2. Depth-First Search (DFS)
**➡️ Fungsi utama:**
Menelusuri graf secara mendalam sebelum berpindah ke simpul lain.

**📌 Cara kerja:**
- DFS menggunakan **rekursi** atau **stack (LIFO - Last In, First Out)** untuk menelusuri graf.
- Dimulai dari **simpul awal**, menandainya sebagai **terkunjungi**, lalu menelusuri **tetangga pertama** secara rekursif.
- Jika **simpul tujuan ditemukan**, program akan mencetak jalur yang ditempuh.
- Jika tidak ditemukan jalur, program akan kembali dan mencari jalur alternatif.

**✅ Kapan DFS digunakan?**  
- Saat mencari **jalur dalam graf yang sangat luas**.
- Digunakan dalam **pencarian labirin, pencocokan pola, dan analisis struktur jaringan**.

---

## 🔍 3. Uniform Cost Search (UCS)
**➡️ Fungsi utama:**
Mencari jalur dengan **biaya paling rendah dalam graf berbobot**.

**📌 Cara kerja:**
- UCS menggunakan **priority queue (heap)** untuk selalu mengeksplorasi **simpul dengan biaya terendah terlebih dahulu**.
- Dimulai dari **simpul awal** dengan biaya **0**.
- Mengeksplorasi **tetangga simpul saat ini** dan menambahkan biaya perjalanan.
- Jika **simpul tujuan ditemukan**, program akan mencetak jalur dengan biaya paling rendah.
- Jika tidak ditemukan jalur, program akan mengembalikan nilai **tak hingga (inf)**.

**✅ Kapan UCS digunakan?**  
- Saat mencari **jalur dengan biaya minimum dalam graf berbobot**.
- Digunakan dalam **algoritma navigasi GPS, perencanaan rute, dan jaringan komunikasi**.

---

## 📌 Cara Menjalankan Program
1. Clone repositori ini:  
   ```sh
   git clone https://github.com/username/repo-name.git
   ```
2. Masuk ke direktori proyek:  
   ```sh
   cd repo-name
   ```
3. Jalankan masing-masing program sesuai kebutuhan:
   - Untuk BFS:
     ```sh
     python bfs.py
     ```
   - Untuk DFS:
     ```sh
     python dfs.py
     ```
   - Untuk UCS:
     ```sh
     python ucs.py
     ```

---

## 📌 Kesimpulan
- **BFS** cocok untuk pencarian **jalur terpendek dalam graf tanpa bobot**.
- **DFS** cocok untuk **eksplorasi mendalam dalam graf**.
- **UCS** cocok untuk **pencarian jalur dengan biaya minimum dalam graf berbobot**.

🚀 Selamat mencoba algoritma pencarian graf! 🎯

