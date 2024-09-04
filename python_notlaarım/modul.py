from math import * # bunu yaptığında direkt işlemi kullanabilrsin math yazmana gerek kalmaz

value = sqrt(9)
print(value)


'''import math
import math as islem # *** takma isim verdik verdiğimiz isimle d eulaşabiliriz


value = dir(math) #kullanabileceğim değerleri verir

value = math.sqrt(49) # = 7 karekökünü alır

value = islem.factorial(5)  # takma ismi kullandık ***

print(value)  #bunu yazmayı unutma
'''

# modül ile aynı ismi alma  math adında py dosyası oluşturma hata alırsın _math vs olabilir. abzen haat alınca vscode u  aç kapa yap

import random

result = random.random()  # 0.0 - 1.0 arası random değer üretir
print(result) 

result = int(random.uniform(10,100))  # 10 ile 100 arası int rastgele sayı
print(result)


# isimler databaseden gelirse ve listenin kaç elemanlı olcağı belli olmayacaksa len(names)-1 ifadesi kullanılır .listenin eleman sayısının bir eksiği

names = ['ali','yağmur','deniz','cenk']
result = names[random.randint(0,len(names)-1)]
print(result)