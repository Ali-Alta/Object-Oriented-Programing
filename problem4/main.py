def hitung_harga_pengiriman(panjang, lebar, tinggi, berat):
    # Hitung volume dalam cm^3
    volume = panjang * lebar * tinggi

    # Bulatkan berat ke bilangan bulat terdekat
    berat_bulat = round(berat)

    # Harga standar
    harga_standar = 5000

    # Periksa apakah memenuhi syarat pengiriman
    if volume >= 50 and berat_bulat >= 1:
        return f"Harga : Rp {harga_standar}"
    else:
        return "Barang tidak memenuhi syarat untuk dikirim."

# Input
panjang = 5
lebar = 2
tinggi = 4
berat = 1

# Operasi
hasil_harga = hitung_harga_pengiriman(panjang, lebar, tinggi, berat)

# Output
print(hasil_harga)