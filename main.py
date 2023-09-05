# Data awal
tabel = [
    {"leaf_width": 2.7, "leaf_length": 4.9, "species": "small-leaf"},
    {"leaf_width": 3.2, "leaf_length": 5.5, "species": "big-leaf"},
    {"leaf_width": 2.9, "leaf_length": 5.1, "species": "small-leaf"},
    {"leaf_width": 3.4, "leaf_length": 6.8, "species": "big-leaf"}
]

# Menghitung rata-rata untuk setiap kolom
mean_width = sum([row['leaf_width'] for row in tabel]) / len(tabel)
mean_length = sum([row['leaf_length'] for row in tabel]) / len(tabel)

# Fungsi untuk menampilkan data dalam bentuk tabel
def display_data(data):
    print("\nCurrent Data Table:")
    print("Leaf Width | Leaf Length | Species")
    print("-" * 31)
    for row in data:
        print(f"{row['leaf_width']:^11.1f} | {row['leaf_length']:^12.1f} | {row['species']:^8}")

# Fungsi untuk menebak spesies dari data baru
def guess_species(new_data, existing_data):
    new_score = new_data['leaf_width'] * mean_width + new_data['leaf_length'] * mean_length
    closest_distance = float('inf')
    nearest_species = None

    for row in existing_data:
        score = row['leaf_width'] * mean_width + row['leaf_length'] * mean_length
        distance = abs(new_score - score)
        if distance < closest_distance:
            closest_distance = distance
            nearest_species = row['species']
    
    return nearest_species

# Program Utama
while True:
    print("\nPilih tindakan yang ingin dilakukan:")
    print("1. Menebak spesies dari data baru")
    print("2. Menebak spesies dari data baru tanpa salah satu kolom")
    print("3. Menebak spesies dari data baru dengan satu kolom tambahan")
    print("4. Menambahkan data baru")
    print("5. Keluar")
    
    choice = input("Pilihan Anda: ")

    if choice == '1':
        new_data = {
            "leaf_width": float(input("Masukkan leaf width: ")),
            "leaf_length": float(input("Masukkan leaf length: "))
        }
        species = guess_species(new_data, tabel)
        new_data["species"] = species
        tabel.append(new_data)
        display_data(tabel)

    elif choice == '2':
        erase_col = input("Masukkan nama kolom yang akan dihilangkan (leaf_width/leaf_length): ")
        new_data = {
            "leaf_width": 0,  # Kolom yang dihilangkan dianggap sebagai 0
            "leaf_length": 0
        }
        if erase_col == "leaf_width":
            new_data["leaf_length"] = float(input("Masukkan leaf length: "))
        elif erase_col == "leaf_length":
            new_data["leaf_width"] = float(input("Masukkan leaf width: "))
        species = guess_species(new_data, tabel)
        new_data["species"] = species
        tabel.append(new_data)
        display_data(tabel)

    elif choice == '3':
        col_name = input("Masukkan nama kolom tambahan: ")
        col_value = float(input(f"Masukkan nilai {col_name}: "))
        new_data = {
            "leaf_width": 0,  # Kolom tambahan dianggap sebagai 0
            "leaf_length": 0
        }
        if col_name == "leaf_width":
            new_data["leaf_length"] = float(input("Masukkan leaf length: "))
        elif col_name == "leaf_length":
            new_data["leaf_width"] = float(input("Masukkan leaf width: "))
        new_data[col_name] = col_value
        species = guess_species(new_data, tabel)
        new_data["species"] = species
        tabel.append(new_data)
        display_data(tabel)

    elif choice == '4':
        new_data = {
            "leaf_width": float(input("Masukkan leaf width: ")),
            "leaf_length": float(input("Masukkan leaf length: ")),
            "species": input("Masukkan spesies: ")
        }
        tabel.append(new_data)
        display_data(tabel)

    elif choice == '5':
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")