-- Tambahkan perintah untuk membuat database 'sakila' jika belum ada
CREATE DATABASE IF NOT EXISTS sakila;

-- Masuk ke dalam database sakila
\c sakila;

CREATE TABLE country (
  country_id SERIAL PRIMARY KEY,
  country VARCHAR(50) NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


