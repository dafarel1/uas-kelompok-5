Program ini dirancang untuk mencatat kehadiran mahasiswa secara digital. Sistem menggunakan Struktur Kontrol (percabangan dan perulangan), Modularisasi (fungsi), serta Penyimpanan Data (List dan CSV) untuk mengelola informasi mata kuliah, dosen, kelas, serta identitas mahasiswa secara real-time.

MULAI

1. INISIALISASI:
   - Impor library: csv, os, datetime.
   - Siapkan list kosong 'sesi_data' untuk menampung input.

2. FUNGSI LOGIN:
   - INPUT username dan password.
   - JIKA username == "admin" DAN password == "uas123" MAKA lanjut ke Menu Utama.
   - JIKA SALAH, ulangi proses login.

3. PERULANGAN MENU UTAMA (WHILE TRUE):
   - TAMPILKAN pilihan menu (1-4).
   - INPUT pilihan_user.

   A. JIKA pilihan == '1' (TAMBAH DATA):
      - INPUT detail akademik: Mata Kuliah, Dosen, Kelas.
      - INPUT detail mahasiswa: NIM, Nama.
      - INPUT kode status: (H/I/S/A).
      - PROSES: Tentukan keterangan otomatis (Contoh: H = Hadir - Tepat Waktu).
      - PROSES: Ambil waktu dan tanggal dari sistem secara otomatis.
      - SIMPAN semua data ke dalam list 'sesi_data'.

   B. JIKA pilihan == '2' (REKAP & CARI):
      - TAMPILKAN semua data yang ada di list 'sesi_data' dalam bentuk tabel.
      - INPUT NIM untuk pencarian detail.
      - JIKA NIM ditemukan, tampilkan seluruh informasi (Matkul, Dosen, Jam, dll).

   C. JIKA pilihan == '3' (HAPUS DATA):
      - JIKA list tidak kosong, hapus entri terakhir menggunakan fungsi pop().

   D. JIKA pilihan == '4' (SIMPAN & KELUAR):
      - JIKA 'sesi_data' berisi data, simpan ke file "database_presensi_lengkap.csv".
      - KELUAR dari program.

4. SELESAI
