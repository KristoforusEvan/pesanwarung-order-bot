# Pesanwarung Order Bot

Bot Telegram untuk mencatat pesanan usaha kecil (warung, toko online, dan sejenisnya). Pelanggan bisa melihat menu lewat chat, dan pesanan nantinya tersimpan di database.

> Status: **dalam pengembangan** (proyek belajar, rencana 4 minggu).

## Fitur

- [x] `/start` — sapaan awal
- [x] `/menu` — menampilkan daftar barang
- [ ] Pilih produk dan jumlah pesanan
- [ ] Simpan pesanan ke database SQLite
- [ ] Notifikasi pesanan baru ke pemilik usaha
- [ ] Rekap pesanan harian

## Teknologi

- Python 3
- [python-telegram-bot](https://python-telegram-bot.org/)
- SQLite (rencana)

## Cara menjalankan

1. Clone repo ini:
   ```
   git clone https://github.com/KristoforusEvan/pesanwarung-order-bot.git
   cd pesanwarung-order-bot
   ```
2. Buat dan aktifkan virtual environment:
   ```
   python -m venv venv
   venv\Scripts\Activate.ps1
   ```
   (Mac/Linux: `source venv/bin/activate`)
3. Pasang library:
   ```
   pip install -r requirements.txt
   ```
4. Buat bot lewat [@BotFather](https://t.me/BotFather) di Telegram untuk mendapat token.
5. Buat file `.env` di folder proyek, isinya:
   ```
   BOT_TOKEN=token_dari_botfather
   ```
6. Jalankan bot:
   ```
   python bot.py
   ```

## Catatan keamanan

Token bot disimpan di file `.env` yang tidak ikut ke GitHub. Jangan pernah membagikan token ke siapa pun.
