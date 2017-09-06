# HowTo Blog
## Description
Yii2 Mass Assignment exploit. 
Mengubah role `user` menjadi `admin` dengan meng-*intercept* *request* POST saat proses registrasi user baru. Hanya role `admin` dapat mengakses flag di halaman utama.

## Installation
- Gunakan [composer](https://getcomposer.org/download/) untuk menginstalasi *depedency* Yii.
``$ php composer.phar update``

## Database
- SQLite3, lokasi: @app/sqlite/mass.db