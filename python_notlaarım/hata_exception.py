# Error
# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e) => SyntaxError



# error handling => hata yönetimi

try:
     x = int(input('x: '))
     y = int(input('y: '))
     print(x/y)
except (ZeroDivisionError,ValueError) as e:    # yakalanan hatayı e adlı bir değişkende saklar. Böylece, e değişkeni üzerinden hatanın türüne ve mesajına erişebilirsiniz.
     print('yanlış bilgi girdiniz')
     print(e)

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('yanlış bilgi girdiniz')

while True:
    try:
        x = int(input('x: '))      #try: Bu blok içinde hata oluşabilecek kodlar yazılır. Eğer bir hata oluşursa, except bloğuna geçilir.
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:   #try bloğunda oluşan herhangi bir hatayı yakalar.  Exception, Python'da yakalanabilecek tüm hataları kapsayan en genel hata sınıfıdır. as ex kısmı ise yakalanan hatayı ex değişkenine atar 
        print('yanlış bilgi girdiniz', ex)  #print('yanlış bilgi girdiniz', ex) ifadesi, hatanın türü ve mesajını ekrana yazdırır.
    else:
        break    # Eğer try bloğunda hata oluşmazsa, bu blok çalışır. break ifadesiyle döngü sonlandırılır.
    finally:
        print('try except sonlandı.')



# raise

#raise ifadesi, Python'da özel bir hata oluşturmak için kullanılır. Bu durumda, Exception sınıfı kullanılarak bir hata oluşturulur


def check_password(psw):
     if len(psw) < 8:
         raise Exception("parola en az 7 karakter olmalıdır.")   #Eğer şifre bu uzunluktan daha kısa ise, kasıtlı olarak bir hata (Exception) oluşturur ve bir hata mesajı verir.
     

password = "1234567"
try:
     check_password(password)
except Exception as ex:
     print(ex)


#**********************

turkce_karakterler = 'şçğüöıİ'

parola = input('parola')

for i in parola:
    if i in turkce_karakterler:
        raise TypeError('Parola türkçe karakter içeremez.')
    else:
        pass
print('geçerli parola')  

# fonksiyonla yapmak daha iyi:

# def checkPassword(parola):
#     turkce_karakterler = 'şçğüöıİ'

#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError('Parola türkçe karakter içeremez.')
#         else:
#             pass
#     print('geçerli parola')    

# parola = input('parola: ')

# try:
#     checkPassword(parola)    
# except TypeError as err:
#     print(err)