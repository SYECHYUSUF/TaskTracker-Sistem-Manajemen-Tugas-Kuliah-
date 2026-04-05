# TaskTracker API - Manajemen Tugas Kuliah

Proyek ini adalah implementasi RESTful API berbasis _microservices_ yang dibangun menggunakan FastAPI. Sistem ini berfungsi untuk mencatat dan mengelola daftar tugas perkuliahan mahasiswa dengan menerapkan relasi _One-to-Many_ antara entitas `Mata_Kuliah` dan `Tugas`.

Proyek ini ditujukan untuk memenuhi Ujian Tengah Semester (UTS) mata kuliah Pemrograman Web Lanjutan.

## Fitur Utama

- **Manajemen Mata Kuliah (CRUD):** Tambah, lihat, perbarui, dan hapus data mata kuliah.
- **Manajemen Tugas (CRUD):** Kelola tugas yang terhubung langsung dengan mata kuliah spesifik (_One-to-Many Relationship_).
- **Autentikasi & Otorisasi:** Sistem registrasi dan login menggunakan JSON Web Token (JWT) untuk memproteksi _endpoint_ sensitif.
- **Validasi Otomatis:** Pengecekan _request body_ dan tipe data secara otomatis menggunakan Pydantic.
- **Dokumentasi Interaktif:** Swagger UI terintegrasi untuk pengujian API secara instan.

## Struktur Direktori

Sistem dirancang dengan pendekatan modular untuk memisahkan logika keamanan, konfigurasi database, dan _routing_ domain bisnis.

```text
tasktracker_api/
├── main.py              # Entry point aplikasi FastAPI
├── database.py          # Konfigurasi engine dan session SQLite
├── models/
│   ├── user.py          # SQLAlchemy model untuk User (Autentikasi)
│   ├── mata_kuliah.py   # SQLAlchemy model untuk Mata_Kuliah
│   └── tugas.py         # SQLAlchemy model untuk Tugas
├── schemas/
│   ├── user_schema.py   # Pydantic schema untuk User
│   ├── mk_schema.py     # Pydantic schema untuk Mata_Kuliah
│   └── tugas_schema.py  # Pydantic schema untuk Tugas
├── routers/
│   ├── auth.py          # Endpoint registrasi dan login
│   ├── mata_kuliah.py   # Endpoint CRUD domain Mata_Kuliah
│   └── tugas.py         # Endpoint CRUD domain Tugas
├── auth/
│   └── jwt_handler.py   # Logika enkripsi password dan JWT
├── requirements.txt     # Daftar dependensi Python
└── README.md            # Dokumentasi proyek
```
