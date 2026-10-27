\# NOTES — Pesanwarung Order Bot



\## Status (28 Okt 2026)

Minggu 1 selesai.



\## Sudah jadi

\- Repo GitHub + .gitignore Python + README

\- Virtual environment dan requirements.txt

\- Bot dibuat lewat BotFather, token disimpan di .env (tidak ikut ke GitHub)

\- bot.py membalas /start dan /menu (menu masih teks biasa)



\## Masalah yang ketemu dan solusinya

\- `TimedOut` saat bot jalan: koneksi ke Telegram lambat, diatasi dengan menambah

&#x20; timeout 30 detik di ApplicationBuilder.

\- `NameError: name 'start' is not defined`: fungsi `start` ikut terganti nama

&#x20; saat menambah `menu`. Fungsi harus didefinisikan di atas `add\_handler`.

\- requirements.txt terlihat kosong di commit: di PowerShell, pakai

&#x20; `pip freeze | Out-File -Encoding utf8 requirements.txt`.



\## Pelajaran

\- Commit kecil dan sering.

\- Cek `git status` sebelum commit, pastikan .env dan venv tidak ikut.

\- Kalau edit di GitHub, jalankan `git pull` sebelum kerja lagi di laptop.



\## Target Minggu 2

\- Rancang tabel SQLite: produk dan pesanan

\- Menu diambil dari database, bukan teks biasa

\- Alur pesan: pilih produk, jumlah, konfirmasi, tersimpan

