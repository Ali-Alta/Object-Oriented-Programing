# tulis solusi code disini
class BangunDatar:
    def __init__(self):
        pass

    def hitung_luas(self):
        pass

    def hitung_keliling(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        super().__init__()
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

    def hitung_keliling(self):
        return 4 * self.sisi

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        super().__init__()
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

    def hitung_keliling(self):
        # Anggap saja segitiga ini siku-siku
        # Jadi, keliling dapat dihitung dengan Pythagoras
        sisi_miring = (self.alas ** 2 + self.tinggi ** 2) ** 0.5
        return self.alas + self.tinggi + sisi_miring

class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        super().__init__()
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

def main():
    # Input
    persegi = Persegi(4)
    segitiga = Segitiga(3, 4)
    persegi_panjang = PersegiPanjang(7, 8)

    # Output
    print("Luas")
    print(f"Persegi : {persegi.hitung_luas()}")
    print(f"Segitiga : {segitiga.hitung_luas()}")
    print(f"Persegi Panjang : {persegi_panjang.hitung_luas()}")

    print("\nKeliling")
    print(f"Persegi : {persegi.hitung_keliling()}")
    print(f"Segitiga : {segitiga.hitung_keliling()}")
    print(f"Persegi Panjang : {persegi_panjang.hitung_keliling()}")

if __name__ == "__main__":
    main()
