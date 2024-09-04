#iç içe fonksiyon ! ! ! ! ! ! !  !
# encapsulation
def outer(num1):   # fonksşyonun adı outer olsun dıştaki fonksiyonu temsil etsin
     print('outer')
     def inner_increment(num1):  # içteki fonksiyon
         print('inner')
         return num1 + 1    # inner_incrementin yaptığı num1 i in üzerine 1 eklemek
     num2 = inner_increment(num1)   #******* bu satır sayesinde inner
     print(num1, num2)
     
outer(10)   # outer fonksiyonunu çağırıp içine 10 değeri atarsam bu durumda çağrılacak olan fonksiyon sadece outer fonksiyonu
            # outer fonksiyonunu içine tanımlaması yapılan fonksiyon şu anda çağrılmaadı
# inner_increment(10) çalışmaz sadece outer kapsamında çalıştırılabilecek bir değer
#************************
# İÇTEKİ Fonksiyon. dışta dönen işler içteki fonksiyonu ilgilendirmiyor. karmaşık kodlarda işleri kolaylaştıran bir yöntem
def inner_increment(num1):  # içteki fonksiyon
         print('inner')
         return num1 + 1   
