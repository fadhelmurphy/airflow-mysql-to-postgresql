
## Panduan Menjalankan Docker Compose

### Prasyarat

Pastikan Anda telah menginstal Docker dan Docker Compose di komputer Anda.

### Langkah 1: Clone Repository

Clone repositori ini ke komputer Anda:

`git clone https://github.com/fadhelmurphy/airflow-mysql-to-postgresql.git
cd airflow-mysql-to-postgresql` 

### Langkah 2: Menjalankan Docker Compose

Jalankan Docker Compose dengan file konfigurasi yang ada:

`docker-compose up -d` 

### Langkah 3: Menghentikan Docker Compose

Untuk mematikan semua container yang dijalankan melalui Docker Compose:

`docker-compose down` 

### Akses Aplikasi

Setelah menjalankan Docker Compose, Anda dapat mengakses aplikasi yang berjalan di kontainer melalui browser Anda:

-   **PHPMyAdmin**
    -   URL: http://localhost/mysql-admin
-   **PgAdmin**
    -   URL: http://localhost:8081/pg-admin
-   **Airflow**
    -   URL: http://localhost:8080

Pastikan Docker Desktop atau Docker Engine sedang berjalan sebelum menjalankan perintah `docker-compose`. Untuk mematikan container, gunakan perintah `docker-compose down`.