# def : Python da fonksiyon tanımlamak için 'def' komutunu kullanırız.
# def dedikten sonra fonksiyona bir isim veriyoruz

def sayHello():    # istediğin ismi ver
    print('Hello')

sayHello()         # fonksiyonu çağır


# fonksiyona dışarıdan bir parametre de gönderebiliriz

def sayHello(name):    
    print('Hello ' + name)

sayHello('çınar') 

#*************************************

def sayHello(name = 'user'):    
    print('Hello ' + name)

sayHello() 

#*************************************
# fonksiyona dışarıdan bir bilgi gönderelim string bir ifade oluştursun ve bu bilgiyi geri göndersin

# return ile sonrasında yazılan ifadenin fonksiyona geri gönderilmesini sağla
# msg isimli değişken tanımla, print ile msg ı ekrana yazdır

def sayHello(name = 'user'):
    return 'Hello ' + name     # ! ! ! ! ! return ifadesi, 'Hello Ela' değerini fonksiyonun dışına döndürür.return, bir fonksiyonun sonucunu belirler ve fonksiyonun çalışmasının bittiği noktayı işaret eder. Fonksiyonun geri döndürdüğü değer, fonksiyon çağrıldığında yerine konur ve bu değerle işlem yapılabilir.

msg = sayHello('Ela')

print(msg)

# Ela bilgisi fonksiyona gönderildi Ela bilgisi user ın yerine geçti
# Hello Ela şeklinde string oluşturuldu bu bilgiyi print ile ekrana yazdırmak yerine bunu geri göderiyoruz
#*******************************

def total(num1, num2):  # fonksiyon dışarıdan 2 sayı alsın
    return num1 + num2  # gönderdiğimiz 2 sayıyı toplayan bir fonksiyon olsun

result = total(10,20)
print(result)

# örneğin 10 ve 20 sayılarını gönderelim ancak return ettiğimiz için örenğin result değişkeninin içerisine aktar. print(result) ile ekrana yazdırırız
#**********************************

def yasHesapla(dogumYili):
    return 2024 - dogumYili

ageCinar = yasHesapla(2004)
ageSelim = yasHesapla(2002)

print(ageCinar, ageSelim)
