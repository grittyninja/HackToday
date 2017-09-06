# Musicality_icon
## Description
Setiap user yang terdaftar dapat memperbarui avatarnya dengan menyisipkan URL gambar ke *field* yang disediakan. URL tersebut kemudian di cURL dan disimpan di dalam server dalam bentuk `md5(*string_random*).jpg`.

## Exploit
cURL tidak difilter, sehingga user bisa memasukkan `file:///etc/passwd` untuk mendapatkan flag

## Database
- SQLite3, lokasi: @webroot/sqlite/data.db