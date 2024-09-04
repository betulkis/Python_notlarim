# bir fonksiyona bir özellik eklemek istediğimizde kullanırız


def dekoratör(fonksiyon): # ** parantez içi g
    def sarmalayıcı():
        print("Fonksiyon çalışmadan önce")
        fonksiyon()   # ** g
        print("Fonksiyon çalıştıktan sonra")
    return sarmalayıcı

@dekoratör  # baştaki fonksiyon adı dekoratör. my_decorator de olabilirdi ismi
def merhaba():    #  bunu direkt yukarıya aktarıyoruz yukarıdaki g fonksiyon() da çağırıyoruz
    print("Merhaba, Dünya!")

merhaba()


#çıktı
# Fonksiyon çalışmadan önce
# Merhaba, Dünya!
# Fonksiyon çalıştıktan sonra


# wrapper=sarmalayıcı
 
