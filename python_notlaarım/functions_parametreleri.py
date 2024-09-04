def changeName(n): # parametre = n
    n = 'ada'

name = 'yiğit'  # değişken tanımla değişken adı name değişkene verdiğimiz isim yiğit

changeName(name)  # changeName e name bilgisi gönderirisem name n ye kopyalanır çıktı yiğit olur ada dönmez

print(name)

#*************

def change(n):
    n[0] = 'istanbul'

sehirler = ['ankara', 'izmir']
            
change(sehirler)
print(sehirler)

# listede adresteki bilgi güncellenir ama change(sehirler[:]) yaparsan ankara izmir yazmaya deva eder 0.indeks güncellenmez
#*************

# gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yaz

def yazdir(kelime, adet):
    print(kelime * adet)

yazdir('Merhaba\n', 10)

