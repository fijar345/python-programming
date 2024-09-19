harga_anak = 30000
harga_dewasa = 50000
harga_lansia = 35000

jumlah_pembeli = int(input("masukan jumlah pembeli tiket"))

total_harga = 0

for i in range(jumlah_pembeli):
    print(f"\npembeli ke-{i+1}:")

    usia = int(input("masukan usia pembeli: "))

    jumlah_tiket = int(input("masukan jumlah tiket yang ingin dibeli: "))

    if usia <12:
        harga = harga_anak
    elif 12 <= usia <=60:
        harga = harga_dewasa
    else:
        harga = harga_lansia

    total_harga_pembeli = harga * jumlah_tiket
    total_harga += total_harga_pembeli

    print(f"harga tiket per orang: Rp {harga}")
    print(f"total harga tiket unutuk pembeli ke-{i+1}: Rp {total_harga_pembeli}")

    print(f"\ntotal harga untuk semua tiket yang di beli: Rp {total_harga}")
