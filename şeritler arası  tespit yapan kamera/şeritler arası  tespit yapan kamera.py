import matplotlib.pyplot as plt
import random

class Araba:
    def __init__(self, konum, şerit):
        self.konum = konum
        self.şerit = şerit

    def şerit_değiştir(self, yeni_şerit):
        self.şerit = yeni_şerit

def karşı_şeride_geçti_mi(araba_konumu, yeşil_kutu_sınırları):
    x, y = araba_konumu
    x_min, x_max, y_min, y_max = yeşil_kutu_sınırları
    return x_min <= x <= x_max and y_min <= y <= y_max

def main():
    # Araba nesnelerini oluşturun (örneğin, konumlarını (x, y) koordinatları olarak belirtin)
    arabalar = [Araba((random.uniform(0, 15), random.uniform(0, 15)), random.randint(1, 3)) for _ in range(10)]

    # Yeşil kutunun sınırlarını belirtin (örneğin, (x_min, x_max, y_min, y_max) olarak)
    yeşil_kutu_sınırları = (5, 10, 5, 10)

    # Grafik penceresini oluştur
    fig, ax = plt.subplots()

    # Her adımda arabaları kontrol edin ve gerekirse şerit değiştirin
    for araba in arabalar:
        # Her adımda arabaların yeni şeritleri ve konumları belirlenir
        yeni_şerit = random.randint(1, 3)
        araba.şerit_değiştir(yeni_şerit)
        araba.konum = (araba.konum[0], random.uniform(0, 15))

        if karşı_şeride_geçti_mi(araba.konum, yeşil_kutu_sınırları):
            ax.plot(araba.konum[0], araba.konum[1], 'go')  # Yeşil kutuya giren arabaları yeşil renkte göster
        else:
            ax.plot(araba.konum[0], araba.konum[1], 'ro')  # Yeşil kutuda olmayan arabaları kırmızı renkte göster

    # Yeşil kutuyu göster
    x_green = [yeşil_kutu_sınırları[0], yeşil_kutu_sınırları[1], yeşil_kutu_sınırları[1], yeşil_kutu_sınırları[0], yeşil_kutu_sınırları[0]]
    y_green = [yeşil_kutu_sınırları[2], yeşil_kutu_sınırları[2], yeşil_kutu_sınırları[3], yeşil_kutu_sınırları[3], yeşil_kutu_sınırları[2]]
    ax.plot(x_green, y_green, 'g-')

    ax.set_xlim(0, 15)  # X ekseninin sınırlarını belirle
    ax.set_ylim(0, 15)  # Y ekseninin sınırlarını belirle
    ax.set_aspect('equal')  # Eksenlerin oranını eşit yap

    plt.show()  # Grafiği göster

if __name__ == "__main__":
    main()
