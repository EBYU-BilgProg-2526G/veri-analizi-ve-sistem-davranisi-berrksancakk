#"""
#Ana çalışma dosyası
#Öğrenciler bu dosyayı çalıştıracaktır.
#"""

#def main():
    # TODO:
    # 1. CSV dosyasını oku
    # 2. örnekleme frekansını hesapla
    # 3. temel istatistikleri yazdır
    # 4. hareketli ortalama filtresi uygula
    # 5. sonucu çizdir
#    pass
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # 1. CSV dosyasını oku
    df = pd.read_csv("data.csv")

    # 2. Örnekleme frekansını hesapla
    dt = df["time"].iloc[1] - df["time"].iloc[0]
    fs = 1 / dt

    print("Örnekleme frekansı:", fs, "Hz")

    # 3. Temel istatistikleri yazdır
    print("Ortalama:", df["value"].mean())
    print("Medyan:", df["value"].median())
    print("Standart Sapma:", df["value"].std())
    print("Minimum:", df["value"].min())
    print("Maksimum:", df["value"].max())

    # 4. Hareketli ortalama filtresi uygula
    window_size = 3
    df["moving_avg"] = df["value"].rolling(window=window_size).mean()

    # 5. Sonucu çizdir
    plt.plot(df["time"], df["value"], label="Ham Veri")
    plt.plot(df["time"], df["moving_avg"], label="Hareketli Ortalama")
    plt.xlabel("Zaman")
    plt.ylabel("Değer")
    plt.legend()
    plt.show()


if _name_ == "_main_":
    main()
