# -*- coding: utf-8 -*-
#"""
#Grafik çizim fonksiyonları
#"""

#def plot_time(t, x_raw, x_filt, save_path):
#    """
#    Ham ve filtrelenmiş sinyali zaman domeninde çizer

#    Parametreler:
#        t        : zaman vektörü
#        x_raw   : ham sinyal
#        x_filt  : filtrelenmiş sinyal
#        save_path : kayıt edilecek dosya yolu
#    """
    # TODO:
    # matplotlib kullanarak:
    # - iki sinyali aynı grafikte çiz
    # - eksen isimleri ve başlık ekle
    # - grafiği dosyaya kaydet
#    pass
    # -- coding: utf-8 --
#"""
#Grafik çizim fonksiyonları
#"""

import matplotlib.pyplot as plt


def plot_time(t, x_raw, x_filt, save_path):
    """
    Ham ve filtrelenmiş sinyali zaman domeninde çizer

    Parametreler:
        t         : zaman vektörü
        x_raw     : ham sinyal
        x_filt    : filtrelenmiş sinyal
        save_path : kayıt edilecek dosya yolu
    """

    # Ham sinyali çiz
    plt.plot(t, x_raw, label="Ham Sinyal")

    # Filtrelenmiş sinyali çiz
    plt.plot(t, x_filt, label="Filtrelenmiş Sinyal")

    # Eksen isimleri
    plt.xlabel("Zaman (s)")
    plt.ylabel("Genlik")

    # Başlık
    plt.title("Ham ve Filtrelenmiş Sinyal (Zaman Domeni)")

    # Açıklama kutusu
    plt.legend()

    # Grafiği dosyaya kaydet
    plt.savefig(save_path)

    # Belleği temizle
    plt.close()
