# Nama Kelompok
    1. Digra Murtaza Izham - 1313621010
    2. Faizal Rizqi Kholily - 1313621029
    3. Muhammad Ramadhan Putra Pratama - 1313621038
    4. Rasyaad Maulana Khandiyas - 1313621020

# Petunjuk Penggunaan
### Menebak Spesies dari data baru
1. Input data baru disertai dengan width "leaf_width" dan lengthnya "leaf_length"
### Menebak spesies dari data baru tanpa salah satu kolom
1. Pilih kolom yang mau dihapus, disini misal kita pilih kolom "leaf_width"
2. Input data baru disertai dengan width = 0 dan lengthnya "leaf_length"
### Menebak spesies dari data baru dengan satu kolom tambahan
    -

### Menambahkan data baru
1. Input data baru disertai dengan width "leaf_width", lengthnya "leaf_length" dan speciesnya "species"
### Keluar
Selesai menggunakan dan keluar dari program

# Penjelasan Program

| No | Width | Length | Species| 
| ----------- | ----------- | ----------- | ----------- |
| 1 | 2.7 | 4.9 | small-leaf |
| 2 | 3.2 | 5.5 | big-leaf
| 3 | 2.9 | 5.1 | small-leaf
| 4 | 3.4 | 6.8 | big-leaf

### Menebak Spesies dari data baru
1. Input data baru disertai dengan width "leaf_width" dan lengthnya "leaf_length"
2. Width dari data yang sudah tersedia kemudian dihitung rata-ratanya dan disimpan di variabel "mean_width"
3. Length dari data yang sudah tersedia kemudian dihitung rata-ratanya dan disimpan di variabel "mean_length"
4. Dilakukan operasi ("leaf_width" * "mean-width" + "leaf_length" * "mean-length") = "new_score"
5. Setiap row dari data yang sudah ada dilakukan operasi yang sama dengan hasil akhir "score"
6. Setelah mendapatkan hasil "new_score" dan "score" dari setiap row, dilakukan operasi distance = abs("new_score" - "score") yang dilakukan berulang di setiap row yang ada.
7. Selisih paling minimum diantara "new_score" - "score" dijadikan acuan spesies untuk data baru.

### Menebak spesies dari data baru tanpa salah satu kolom
1. Pilih kolom yang mau dihapus, disini misal kita pilih kolom "leaf_width"
2. Input data baru disertai dengan width = 0 dan lengthnya "leaf_length"
3. Length dari data yang sudah tersedia kemudian dihitung rata-ratanya dan disimpan di variabel "mean_length"
4. Dilakukan operasi (0 * "mean-width" + "leaf_length" * "mean-length") = "new_score"
5. Setiap row dari data yang sudah ada dilakukan operasi yang sama dengan hasil akhir "score"
6. Setelah mendapatkan hasil "new_score" dan "score" dari setiap row, dilakukan operasi distance = abs("new_score" - "score") yang dilakukan berulang di setiap row yang ada.
7. Selisih paling minimum diantara "new_score" - "score" dijadikan acuan spesies untuk data baru.

### Menebak spesies dari data baru dengan satu kolom tambahan
    -

### Menambahkan data baru
1. Input data baru disertai dengan width "leaf_width", lengthnya "leaf_length" dan speciesnya "species"