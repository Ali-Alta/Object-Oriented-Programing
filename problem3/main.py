# tulis solusi code disini
class Kalkulator:
    def __init__(self):
        pass

    def penjumlahan(self, a, b):
        return a + b

    def pengurangan(self, a, b):
        return a - b

    def perkalian(self, a, b):
        return a * b

    def pembagian(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Pembagian oleh nol!"

def main():
    # Input
    kalkulator = Kalkulator()

    # Operasi
    hasil_penjumlahan = kalkulator.penjumlahan(3, 4)
    hasil_pengurangan = kalkulator.pengurangan(15, 4)
    hasil_perkalian = kalkulator.perkalian(10, 10)
    hasil_pembagian = kalkulator.pembagian(12, 3)

    # Output
    print(f"Penjumlahan : {hasil_penjumlahan}")
    print(f"Pengurangan : {hasil_pengurangan}")
    print(f"Perkalian : {hasil_perkalian}")
    print(f"Pembagian : {hasil_pembagian}")

if __name__ == "__main__":
    main()
