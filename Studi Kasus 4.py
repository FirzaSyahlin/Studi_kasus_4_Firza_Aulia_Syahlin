buku = {
    "judul": "Dilan 1990",
    "penulis": "Pidi Baiq",
    "tahun_terbit": 2014
}

while True:
    print("1. Tampilkan data")
    print("2. Tambah penerbit")
    print("3. Ubah penulis")
    print("4. Hapus penerbit")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print(buku)

    elif pilihan == "2":
        buku["penerbit"] = input("Masukkan penerbit: ")
        print(buku)

    elif pilihan == "3":
        buku["penulis"] = input("Masukkan penulis baru: ")
        print(buku)

    elif pilihan == "4":
        del buku["penerbit"]
        print(buku)

    elif pilihan == "5":
        print("Data buku setelah perubahan:")
        print(buku)
        break

    else:
        print("Pilihan tidak tersedia")