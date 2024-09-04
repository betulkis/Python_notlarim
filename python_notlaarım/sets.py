fruits = {'orange', 'apple', 'banana'}
# print(fruits[0]) indekslenemez
for x in fruits:
    print(x)

#fruits adlı değişken, bir kümeyi (set) temsil eder. Python'daki kümeler, sırasız ve tekrarsız öğelerden oluşur, bu nedenle kümelerde elemanların belli bir sırası yoktur. Bu yüzden, kümelerde indeksleme işlemi yapılamaz.
#Örneğin, bir liste (list) sıralı bir veri yapısıdır ve içinde bulunan öğelere indeks numaraları ile erişebilirsiniz. Ancak kümeler, sıralı olmadıkları için elemanların belirli bir indeks numarası yoktur, bu yüzden fruits[0] gibi bir erişim denemesi hata verir.
#Ancak, kümeler üzerinde döngü (for döngüsü) ile iterasyon yapabilirsiniz, çünkü küme içindeki her bir öğeye sırayla erişilebilir. Yine de bu sıranın belirli bir düzeni olmayacaktır, yani aynı küme için her çalıştırmada farklı bir sıra ile karşılaşabilirsiniz.

# eleman ekleme

fruits.add('cherry')
print(fruits)
