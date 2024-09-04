numbers = [1,2,3,4,5]

for num in numbers:
    print(num)

#  1 den 5 e kadar sayılar yazdırılır. Listenin içerisinden tek tek elemanları al num değişkeninin içerisine at ve her for dögüsü döndüğünde gelen num ı ekrana yazdır
#*****************************

numbers = [1,2,3,4,5]

for num in numbers:
    print('Hello')
    # 1 den 5 e kadar hello yazar burda  önemli olan şey: listenin eleman sayısı kadar for döngüsü dönüyor olması

#*****************************

names = ['çınar', 'sadık', 'sena']

for farketmez in names:
    print(f'benim adım {farketmez}')


#******************************

name = 'sadık turan'    # string ifade olursa # string ifadenin her bir karakteri tek tek yazdırılır alt alta

for n in name:
    print(n)

#******************************

tuple = [(1.2),(1,3),(3,5),(5,7)]

for a,b in tuple:
    print(a)   # parantez içindeki ilk ve ikinci değeri temsil eder a,b ve print(a) sadece ilk değeri yazdırır

#print(a,b) tek tek elemanları ayrılmış şekilde yazdırır   1 2 gibi

#**********************************
# sayılar listesindeki hangi sayılar 3 ün katıdır

sayilar= [1,3,5,7,9,12,19,21]

for sayi in sayilar:
    if(sayi%3==0):   # 3 e bölümünde kalan 0 ise sayı 3 ün katıdır
        print(sayi)

#**********************************
# sayılar listesinde sayıların toplamı kaçtır

sayilar= [1,3,5,7,9,12,19,21]

toplam = 0
for sayi in sayilar:
    toplam = toplam + sayi  # toplam += sayi
print('toplam:',toplam)

# tek sayılar parantezin içindeki ifadeyle anlaşılır: if (sayi % 2 == 1)



