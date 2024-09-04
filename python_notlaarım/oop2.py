# class kapsamı içerisinde attributes ve meethods var
# Attributes (Özellikler):sınıfın temsil ettiği nesnenin sahip olduğu verilerdir.nesneye ait bilgiler veya özelliklerdir. Diyelim ki bir Araba sınıfımız var. Bu sınıfın "attributes" olarak renk, model, ve hız gibi özellikleri olabilir

# Methods, sınıfın yapabileceği işlerdir. Yani, bu nesnenin gerçekleştirebileceği eylemler veya işlemlerdir.Araba sınıfını düşünelim. Bu sınıfın "methods" olarak hızlan, yavaşla, ve durdur gibi işlemleri olabilir.

# Attributes: Bir nesnenin neye sahip olduğunu belirtir. (Özellikler)
# Methods: Bir nesnenin ne yapabildiğini belirtir. (İşlemler)
# sınıflar nesnelerin hem neler olduğunu hem de neler yapabileceğini belirleyen bir yapı sunar.


#          ------------ ÖNEMLİ---------------


# ** Constructor (yapıcı metot):  bir sınıftan yeni bir nesne oluşturulurken otomatik olarak çağrılan özel bir metottur. Python'da bu metodun adı __init__'dir. ! * ! * ! * ! * ! * !
class Araba:
    def __init__(self, renk, model):
        self.renk = renk  # Bu bir object attribute.
        self.model = model  # Bu da bir object attribute.

araba1 = Araba("kırmızı", "2020")


# ****** self parametresi classtan türetilen herhangi bir objeyi temsil ediyor. obje üzerine bir değer aktarmak istediğimiz zaman self kullanırız



# ** CLASS ATTRİBUTES, bir sınıfın tüm nesneleri (örnekleri) için ortak olan verilerdir. 
class Araba:
    tekerlek_sayisi = 4  # Bu bir class attribute'tur.


# **  Object attributes, bir sınıftan oluşturulan her bir nesneye özgü olan verilerdir. Bu özellikler, her bir nesnenin kendisine ait olur ve diğer nesnelerden bağımsızdır.
class Araba:
    def __init__(self, renk):
        self.renk = renk  # Bu bir object attribute'tur.

araba1 = Araba("kırmızı")
araba2 = Araba("mavi")

#--------********---------******-----------*******-------

class Person:
    # class attributes
    address = 'no information'
    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı.')

        # methods


# object (instance)
p1 = Person(name='ali', year= 1990) 
p2 = Person(name ='yağmur', year = 1995)

p1.name = 'ahmet'
p1.address = 'kocaeli' 

print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')