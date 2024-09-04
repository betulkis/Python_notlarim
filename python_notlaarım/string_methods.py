# upper metodu  bütün karakterleri büyük harfe çevirir
# metodlarda bir parametre göndermeyecek olsak bile () kullanılır

message = 'hello there'

message = message.upper()
print(message)

# lower() bütün karakterleri küçük harfe çevirir 
# title() her kelimenin baş harfi büyük harfe çevrilir
# capitalize() sacece ilk kelime büyük harfle başlar diğerleri küçük olur

# message = message.strip()
#strip() metodu : baştaki boşluk karakteri gider.kullanıcıdan gelen bilgileri kontrolden geçirmemiz gerekiyor örn şifre girişi yaptığında başında boşluk olması eşleşmede sorun çıkartır

# split() her kelimeyi ayrı ayrı verir dizi şeklinde

message = message.split()
print(message)

message = ' ' .join(message)  # kelimelerin arasına ' ' içinde ne varsa onu koyar boşluksa boşluk, çizgiyse çizgi
print(message)


# replace ilk tırnak içindekini bulur ve onun yerine 2.tırnaktaki ifadeyi yazar

deneme= 'sadık turan'
deneme = deneme.replace('sadık','değişti')
print(deneme)

# .replace('ö','o')
# .replace(' ','-')


# python string methods w3schools  bakabilirsin


# .count('a')  kaç tane a karakteri olduğunu sayar

# .find('com')  com ifadesi var mı varsa hangi c indekste.  .find('com', 0, 10)  0 ile 10.ineks arasında com var mı bulamazsa -1 döndürür 

# .endswith('com')  com ile bitiyor mu (true döndürür)


