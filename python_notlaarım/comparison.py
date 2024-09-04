# karşılaştırmak=comparison

# girilen 2 sayıdan hangisi büyüktür

a = int(input('a: '))
b = int(input('b: '))

result = (a > b)
print(f'a: {a} b: {b} den büyüktür: {result}')

# metin, kıyaslama yanlış olsa da aynı olur ama true false doğru ifadeleri verir
#********************************************

# kullanıcıda 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız 
# eğer ortalama 50 ve üstüyse geçti değilse kaldı yazdırın

vize1 =float(input('1. vize: '))
vize2 =float(input('2. vize: '))
final =float(input('final: '))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
# 0.6 ile çarpmak %60 ını almaktır

print(f'not ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}')  # {ortalama>=50} true ya das false döndürür


#********************************************
# girilen ssayını tek mi çift mi olduğunu yazdır

sayi = int(input('sayı: '))

tekcift = (sayi % 2 == 0)  # çift olma durumudur ve true döndürür çiftse

print(f'girilen sayı çift olma durumu: {tekcift}')


#********************************************
# parola ve email bilgisini isteyip doğruluğunu kontrol edin

email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail)
isPassword = (password == girilenPassword)

print(f'Email bilgisi doğru mu: {isEmail} ve Parola doğru mu: {isPassword}')

# yukarıdakini daha kısa yapmak için logical mantıksal operatörleri kullan
# tek bir operatörde birleştirilebilir

email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

result = (email == girilenEmail) and (password == girilenPassword)

print(f'uygulamaya giriş başarılı mı: {result}')


