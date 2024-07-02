def sequential_search(arr, x):
    """Sequential search function"""
    for i, book in enumerate(arr):
        if book['title'] == x:
            return i
    return -1

def main():
    """Main program"""
    book_data = []

    while True:
        print("\nMenu:")
        print("1. Input data buku")
        print("2. Hapus data buku")
        print("3. Cari data buku")
        print("4. Lihat data buku")
        print("5. Keluar")

        choice = input("Masukkan no pilihan: ")

        if choice == '1':
            x = input("Masukkan judul buku: ")
            tahun = input("Masukkan tahun terbit: ")
            book = {
                'title': x,
                'tahun': tahun
            }
            book_data.append(book)
            book_data.sort(key=lambda x: x['title'])  # Sort the array by book title
            print(f"Buku '{x}' telah ditambahkan ke dalam array")

        elif choice == '2':
            if not book_data:
                print("Data kosong, tidak ada buku untuk dihapus.")
            else:
                x = input("Masukkan judul buku yang akan dihapus: ")
                index = sequential_search(book_data, x)
                if index != -1:
                    removed_book = book_data.pop(index)
                    print(f"Buku '{removed_book['title']}' telah dihapus dari array")
                else:
                    print(f"Buku '{x}' tidak ditemukan dalam array")

        elif choice == '3':
            if not book_data:
                print("Data kosong, tidak ada buku untuk dicari.")
            else:
                x = input("Masukkan judul buku yang akan dicari: ")
                index = sequential_search(book_data, x)
                if index != -1:
                    book = book_data[index]
                    print(f"Buku '{book['title']}' ditemukan pada indeks ke {index}.")
                    print(f"Tahun Terbit: {book['tahun']}")
                else:
                    print(f"Buku '{x}' tidak ditemukan dalam data")

        elif choice == '4':
            if not book_data:
                print("Data kosong, tidak ada data untuk ditampilkan")
            else:
                print("Isi data saat ini: ")
                for i, book in enumerate(book_data):
                    print(f"{i}. Judul: {book['title']}, Tahun Terbit: {book['tahun']}")

        elif choice == '5':
            print("Anda telah keluar dari program")
            break

        else:
            print("Pilihan tidak valid. Masukkan no pilihan 1 sampai 5")

if __name__ == "__main__":
    main()