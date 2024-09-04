import numpy as np 

result = np.array([1,3,5,7,9])  # burda yazan elemanları dizi şeklinde yazdırır
# result = np.arange(1,10)  # 1 den 10 kadar eleman dizisi 10 dahil değil
# result = np.arange(10,100,3) # 10 ile 100 arası dizi artış miktarı 3
# result = np.zeros(10) # 10 tane 0
# result = np.ones(10) # 10 tane 1
# result = np.linspace(0,100,5) # verdiğin başlangıç ve bitiş değerini eşit aralıklarla böler 0 25 50 75 100
# result = np.linspace(0,5,5)  # 0 ile 5 i 5 eşit parçaya böl. 0 1.25 2.5 3.75 5
# result = np.random.randint(0,10) # 0 ve 10 arası 10 dahil değil rastgele sayı verir
# result = np.random.randint(20)  # sadece üst değer de verilebilir 0 dan 20 ye kadar aynı mantık 0 dahil 20 değil
# result = np.random.randint(1,10,3) # 1 10 arası rastgele 3 sayı
# result = np.random.rand(5) # rand 0 ile 1 arası 5 sayı üretir
# result = np.random.randn(5) # randn - değerlerde dahil olur
# result = np.arange(50) # 0 dan 50 ye kadar dizi oluşturur 50 dahil değil

# np_array = np.arange(50) # 5 e 10 luk bir matris oluşturur
# result = np_array.reshape(5,10)   # 5 satır 10 sütun 0dan 50 ye kadar 50 yok

# np_array = np.arange(50) 
# np_multi = np_array.reshape(5,10)  # np_multi  çok boyutlu bir dizi
# print(np_multi.sum(axis=1)) #np_multi satırların toplamı
# print(np_multi.sum(axis=0))  # sütunların toplamı 

# rnd_numbers = np.random.randint(1,100,10)  # 1 ile 100 arası 10 sayı rastgele
# print(rnd_numbers)
# result = rnd_numbers.max()  üretilen sayılardan max olan sayı
# result = rnd_numbers.min()
# result = rnd_numbers.mean() # sayıların ort
# result = rnd_numbers.argmax() # üretilen en büyük sayının indeksi
# result = rnd_numbers.argmin()


print(result)

# array dizi