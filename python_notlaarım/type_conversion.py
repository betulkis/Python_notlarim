"""x = input('1.sayı: ')
y = input('2.sayı: ')

print(type(x))
print(type(y))

toplam = int(x) + int(y)

print(toplam)"""

# yarıçapı verilen bir dairenin alan ve çevresini hesapla 

"""pi = 3.14

r = float(input("yarı çap: "))

alan= pi * (r ** 2)
cevre = 2 * pi * r

print("alan:", alan)
print("çevre:", cevre)

# float bilgiyi string bir birleştirme işleminde kullanamayız
# print("alan: " + alan + "çevre: " + cevre)    bu hata verir

print("alan: " + str(alan) + " çevre: " + str(cevre))"""  #çevreden önce bir boşluk bıraktık birleşince arası ayrık olsun


name = 'sadık'
surname = 'turan'
age = 36

greeting = 'my name is ' + name + ' ' + surname + ' and \n I am ' + str(age) + ' years old'  # \n alt satıra geçer
length = len(greeting)

print(greeting)  # greeting değişkeni oluşturduk

print(greeting[0])   #ilk karakter yazdırılır indeks 0 string ifadenin her bir elemanı bir indeks ile ifade edilmiştir
print(len(greeting))  #cümlenin kaç karakterli olduğunu bulmak için len kullanılır
print(greeting[-1]) #son karakter verir veya bunun yerine en başta greetingin altına length = len(greeting)  tanımla uzunluğu bulsun sonra print(greeting[length-1]) yap ve sondaki karakteri sana söylesin
print(greeting[length-1])
print(greeting[3:9])  # 3.indeksten 9 a kadar olan yerleri yazdırır
print(greeting[2:40:2]) #2 den 40 a 2 şer 2 şer harf alır

