# tulis solusi code disini
import math

class BangunRuang:
    def __init__(self):
        pass

    def hitung_volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        super().__init__()
        self.sisi = sisi

    def hitung_volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__()
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        super().__init__()
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def hitung_volume(self):
        return math.pi * self.jari_jari**2 * self.tinggi

def main():
    # Input
    kubus = Kubus(10)
    balok = Balok(3, 6, 10)
    tabung = Tabung(7, 10)

    # Output
    print("Volume")
    print(f"Kubus : {kubus.hitung_volume()}")
    print(f"Balok : {balok.hitung_volume()}")
    print(f"Tabung : {tabung.hitung_volume()}")

if __name__ == "__main__":
    main()
