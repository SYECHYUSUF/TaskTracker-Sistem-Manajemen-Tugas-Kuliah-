# TaskTracker API - Manajemen Tugas Kuliah

**Proyek Ujian Tengah Semester (UTS)**

- **Mata Kuliah:** Pemrograman Web Lanjutan
- **Nama:** MOCH SYECH YUSUF M
- **NIM:** H071241093

---

## Deskripsi Proyek

TaskTracker API adalah implementasi layanan _backend_ RESTful API berbasis _microservices_ modular yang dibangun menggunakan _framework_ FastAPI. Sistem ini dirancang untuk mempermudah pencatatan dan pengelolaan tugas perkuliahan dengan menerapkan relasi database _One-to-Many_ antara entitas `Mata_Kuliah` dan `Tugas`.

Proyek ini telah memenuhi seluruh kriteria kompetensi dasar, mencakup pemisahan domain layanan, operasi CRUD, ORM SQLAlchemy, dan proteksi _endpoint_ menggunakan JSON Web Token (JWT).

## Fitur Utama

- **Manajemen Mata Kuliah (CRUD):** Tambah, lihat, dan hapus data mata kuliah.
- **Manajemen Tugas (CRUD):** Tambah tugas yang terhubung langsung dengan ID mata kuliah spesifik, lihat daftar tugas, dan perbarui status penyelesaian tugas.
- **Keamanan JWT:** Sistem registrasi dan _login_ _user_, di mana operasi penambahan dan modifikasi data (POST, PUT, DELETE) dilindungi dan mewajibkan token otorisasi.
- **Validasi Pydantic:** Pengecekan otomatis terhadap tipe data dan struktur _request body_.
- **Dokumentasi Interaktif:** Swagger UI aktif secara otomatis di rute `/docs` untuk pengujian API secara instan.

## Struktur Direktori

Sistem dirancang menggunakan arsitektur modular untuk memisahkan domain layanan:

```text
tasktracker_api/
├── main.py              # Entry point aplikasi FastAPI
├── database.py          # Konfigurasi engine dan session database SQLite
├── models/
│   ├── user.py          # ORM SQLAlchemy untuk entitas User
│   ├── mata_kuliah.py   # ORM SQLAlchemy untuk entitas Mata_Kuliah
│   └── tugas.py         # ORM SQLAlchemy untuk entitas Tugas
├── schemas/
│   ├── user_schema.py   # Skema Pydantic untuk validasi User
│   ├── mk_schema.py     # Skema Pydantic untuk validasi Mata_Kuliah
│   └── tugas_schema.py  # Skema Pydantic untuk validasi Tugas
├── routers/
│   ├── auth.py          # Router domain autentikasi (Register/Login)
│   ├── mata_kuliah.py   # Router domain CRUD Mata Kuliah
│   └── tugas.py         # Router domain CRUD Tugas
├── auth/
│   └── jwt_handler.py   # Logika enkripsi password dan token JWT
├── requirements.txt     # Daftar pustaka/library Python
└── README.md            # Dokumentasi proyek
```

## Instalasi dan Setup

1. **Clone Repositori**

   ```bash
   git clone <url-repositori-anda>
   cd tasktracker_api
   ```

2. **Buat Virtual Environment**

   ```bash
   python3 -m venv venv
   ```

3. **Aktifkan Virtual Environment**

   ```bash
   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

4. **Instal Dependensi**

   ```bash
   pip install -r requirements.txt
   ```

5. **Jalankan Aplikasi**

   ```bash
   uvicorn main:app --reload
   ```

6. **Akses Dokumentasi**
   ```bash
   http://localhost:8000/docs
   ```
