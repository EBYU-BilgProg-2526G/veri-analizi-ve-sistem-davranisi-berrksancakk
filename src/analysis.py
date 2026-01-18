# -*- coding: utf-8 -*-
#"""
#Temel sinyal analiz fonksiyonları
#"""

#def sampling_rate(t):
#    """
#    Zaman vektöründen örnekleme frekansını hesaplar

#    Parametre:
#        t : zaman vektörü

#    Dönen:
#        fs : örnekleme frekansı (Hz)
#    """
    # TODO:
    # 1. ardışık iki zaman örneği arasındaki farkı hesapla
    # 2. fs = 1 / dt
#    pass
t = np.array([0, 0.01, 0.02, 0.03])
x = np.array([1, 2, 3, 4])

fs = sampling_rate(t)
print(fs)

istatistikler = basic_stats(x)
print(istatistikler)
import numpy as np

def sampling_rate(t):
    # Ardışık iki zaman örneği arasındaki fark
    dt = t[1] - t[0]

    # Örnekleme frekansı
    fs = 1 / dt

    return f

#def basic_stats(x):
   # """
   #Sinyal için temel istatistikleri hesaplar

    #Parametre:
     #   x : sinyal vektörü

    #Dönen:
    #    stats (dict):
    #        mean
    #        std
    #        rms
    #        min
    #        max
   # """
    # TODO:
    # numpy kullanarak gerekli istatistikleri hesapla
  #  pass
    import numpy as np

def basic_stats(x):
    stats = {}

    stats["mean"] = np.mean(x)
    stats["std"] = np.std(x)
    stats["rms"] = np.sqrt(np.mean(x**2))
    stats["min"] = np.min(x)
    stats["max"] = np.max(x)

    return stats

