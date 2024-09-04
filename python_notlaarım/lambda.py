def square(num):  # karesini alma fonksiyonu içerisine numara alacak
    return num ** 2

result = square(2)

print(result)

# bir listenin içindeki sayıların karesini almak istiyorsak:
# map methodu kullanılabilir: dizi içerisindeki her bir elemana ulaşıp her bir elemanı bir fonksiyon üzerinden geçirebiliriz
# *** map methodunu içerisine fonksiyonun ismini ! ve kullanacak olduğumuz diziyi yazıyoruz  map(square, numbers)

def square(num): return num ** 2

numbers = [1,3,5,7,9]

result = list(map(square, numbers))   # map den dönen sonucu listeye çevir

print(result)


# her bir elemanın tek tek dolaşılması için list ya da for döngüsü kullanılmalı for:

for item in map(square, numbers):
    print(item)


# lambda 
# square in yaptığı işlemi isimsiz bir fonksiyonla yapabilirisn 

numbers = [1,3,5,9]

result = list(map(lambda num: num ** 2, numbers))

print(result)

# ** bir fonksiyon tanımlıyorsun ve isim de verebiliyorsun

square = lambda num: num ** 2
numbers = [2,4]
result = list(map(square, numbers)) # **
print(result)


square = lambda num: num ** 2
result = square(7)
print(result)