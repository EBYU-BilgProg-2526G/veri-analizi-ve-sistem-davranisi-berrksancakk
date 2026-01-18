# -*- coding: utf-8 -*-
#"""
#Basit sinyal işleme fonksiyonları
#"""

#def moving_average(x, window_size):
#    """
#    Hareketli ortalama filtresi

#    Parametreler:
#        x           : sinyal vektörü
#        window_size : pencere uzunluğu (int)

#    Dönen:
#        y : filtrelenmiş sinyal
#    """
    # TODO:
    # 1. her örnek için pencereyi belirle
    # 2. pencere içindeki ortalamayı hesapla
    # 3. sonucu yeni bir listeye yaz
#    pass
    # -- coding: utf-8 --
#"""
#Basit sinyal işleme fonksiyonları
#"""

x = [10, 12, 11, 15, 14]
y = moving_average(x, 3)
print(y)

def moving_average(x, window_size):
    """
    Hareketli ortalama filtresi

    Parametreler:
        x           : sinyal vektörü
        window_size : pencere uzunluğu (int)

    Dönen:
        y : filtrelenmiş sinyal
    """

    y = []  # filtrelenmiş sinyal

    # Her örnek için pencereyi gez
    for i in range(len(x) - window_size + 1):
        # 1. pencereyi belirle
        window = x[i:i + window_size]

        # 2. pencere içindeki ortalamayı hesapla
        avg = sum(window) / window_size

        # 3. sonucu listeye ekle
        y.append(avg)

    return y
