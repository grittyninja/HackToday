# HowTo Blog
## Description
Yii2 Mass Assignment exploit. 
Mengubah role `user` menjadi `admin` dengan meng-*intercept* *request* POST saat proses registrasi user baru. Hanya role `admin` yang dapat mengakses flag di halaman utama.

## Installation
- Gunakan [composer](https://getcomposer.org/download/) untuk menginstalasi *dependency* Yii.<br/>
``$ php composer.phar install``

## Database
- SQLite3, lokasi: @webroot/sqlite/mass.db