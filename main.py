import csv
import os
from datetime import datetime

# --- 1. MODULARISASI (FUNGSI) ---

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def cetak_garis(karakter="=", panjang=75):
    print(karakter * panjang)

def login():
    bersihkan_layar()
    cetak_garis()
    print(f"{'LOGIN ADMIN AKADEMIK':^75}")
    cetak_garis()
    username = input("Username: ")
    password = input("Password: ")
    return username == "admin" and password == "uas123"

def simpan_ke_csv(data_list):
    nama_file = 'database_presensi_lengkap.csv'
    file_ada = os.path.isfile(nama_file)
    try:
        with open(nama_file, mode='a', newline='') as file:
            kolom = ['Tanggal', 'Jam_Input', 'NIM', 'Nama', 'Matkul', 'Dosen', 'Kelas', 'Status', 'Ket']
            writer = csv.DictWriter(file, fieldnames=kolom)
            if not file_ada:
                writer.writeheader()
            writer.writerows(data_list)
        return True
    except:
        return False

# --- 2. LOGIKA UTAMA ---

def main():
    if not login():
        print("\n[!] Login Gagal!")
        return

    sesi_data = []
    
    while True:
        bersihkan_layar()
        cetak_garis()
        print(f"{'SISTEM PRESENSI MAHASISWA (DETAIL AKADEMIK)':^75}")
        print(f"{'Admin: Online | Tanggal: ' + datetime.now().strftime('%d/%m/%Y'):^75}")
        cetak_garis()
        print("1. Input Presensi Siswa (Detail)")
        print("2. Lihat Rekap Sesi Ini & Pencarian")
        print("3. Hapus Data Terakhir")
        print("4. Simpan ke CSV & Keluar")
        cetak_garis()
        
        pilihan = input("Pilih Menu (1-4): ")

        if pilihan == '1':
            print("\n[ INPUT DATA AKADEMIK ]")
            matkul = input("Mata Kuliah    : ")
            dosen  = input("Nama Dosen     : ")
            kelas  = input("Ruang/Kelas    : ")
            cetak_garis("-", 30)
            nim    = input("NIM Mahasiswa  : ")
            nama   = input("Nama Lengkap   : ")
            
            print("Status         : [H]adir, [I]zin, [S]akit, [A]lpha")
            kode = input("Pilih Status   : ").upper()
            
            if kode == 'H': status, ket = "Hadir", "Tepat Waktu"
            elif kode == 'I': status, ket = "Izin", input("Alasan Izin: ")
            elif kode == 'S': status, ket = "Sakit", "Surat Dokter"
            else: status, ket = "Alpha", "Tanpa Keterangan"

            # Ambil Tanggal dan Jam Otomatis
            skrg = datetime.now()
            
            sesi_data.append({
                'Tanggal': skrg.strftime("%Y-%m-%d"),
                'Jam_Input': skrg.strftime("%H:%M:%S"),
                'NIM': nim,
                'Nama': nama,
                'Matkul': matkul,
                'Dosen': dosen,
                'Kelas': kelas,
                'Status': status,
                'Ket': ket
            })
            print(f"\n✅ Data {nama} untuk Matkul {matkul} berhasil dicatat!")
            input("Tekan Enter...")

        elif pilihan == '2':
            bersihkan_layar()
            cetak_garis()
            print(f"{'REKAP PRESENSI DETAIL':^75}")
            cetak_garis()
            if not sesi_data:
                print(" Data masih kosong.")
            else:
                # Header Tabel yang lebih lengkap
                print(f"{'NIM':<10} | {'Nama':<15} | {'Matkul':<15} | {'Kelas':<7} | {'Status'}")
                print("-" * 75)
                for s in sesi_data:
                    print(f"{s['NIM']:<10} | {s['Nama']:<15} | {s['Matkul']:<15} | {s['Kelas']:<7} | {s['Status']}")
                
                # Fitur Cari berdasarkan NIM
                cari = input("\nCari NIM untuk detail lengkap (atau Enter): ")
                if cari:
                    hasil = [d for d in sesi_data if d['NIM'] == cari]
                    if hasil:
                        h = hasil[0]
                        print("\n--- DETAIL LENGKAP ---")
                        print(f"Nama     : {h['Nama']}")
                        print(f"Matkul   : {h['Matkul']}")
                        print(f"Dosen    : {h['Dosen']}")
                        print(f"Kelas    : {h['Kelas']}")
                        print(f"Waktu    : {h['Jam_Input']}")
                        print(f"Status   : {h['Status']} ({h['Ket']})")
                    else:
                        print("Data tidak ditemukan.")
            input("\nTekan Enter...")

        elif pilihan == '3':
            if sesi_data:
                buang = sesi_data.pop()
                print(f"\n[!] Data {buang['Nama']} berhasil dihapus.")
            else:
                print("\n[!] Kosong.")
            input("Tekan Enter...")

        elif pilihan == '4':
            if sesi_data:
                if simpan_ke_csv(sesi_data):
                    print(f"\n[✔] Berhasil simpan ke database_presensi_lengkap.csv")
            print("Keluar dari sistem...")
            break

if __name__ == "__main__":
    main()
