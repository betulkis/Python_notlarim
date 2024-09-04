for item in range(50,100,20):  #50den 1**e kadar 20şer artıyor
    print(item)

# bu elemanları liste şeklinde yazdır

print(list(range(50,100,20)))

#*********************************
# zip metodu: listeleri eşleştirmek için zip metodu kullanılır

list1 = [1,2,3,4,5]   # isimler listesi
list2 = ['a','b','c','d','e']   # telefon listesi vb olabilir

print(list(zip(list1, list2)))  # eşleştirme sonucunu list e çevir ve ekranda göster print

for item in zip(list1, list2):
    print(item) # alt alta for döngüsü ile yazdırır

for a,b in zip(list1, list2):
    print(a)   #listeni sadece 1 2 3 (isimler listesi vb olabilir) bilgileri verdirilir