#!/bin/bash

# Menjalankan file SQL pertama
echo "Menjalankan sakila-schema.sql..."
mysql -u root -proot < /docker-entrypoint-initdb.d/sakila-schema.sql

# Menjalankan file SQL kedua
echo "Menjalankan sakila-data.sql..."
mysql -u root -proot < /docker-entrypoint-initdb.d/sakila-data.sql
