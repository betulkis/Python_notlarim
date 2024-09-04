if 3>2:
    print('selam')



if True:
    print('selam')


isLoggedin = True

if isLoggedin:     # yukarıdan isLoggedin false yapılırsa selam mesajı yazdırılmaz
    print('selam')    

#************************************

username = 'sadikturan'
password = '1234'

isLoggedin = (username == 'sadikturan') and (password == '1234') # true olursa ekrana selam yazar

if isLoggedin:   # true döndürürse bu blok çalışır
    print('selam') 

else:   # false döndürürse bu blok çalışır
    print('username ya da parola yanlış')

#****************************************
# parola yanlışsa ya da user name yanlışsa  bunu bildiren bir kod yaz

username = 'sadikturan'
password = '1234'

isLoggedin = (username == 'sadikturan') and (password == '1234') # true olursa ekrana selam yazar

if (username == 'sadikturan'):   # username doğruysa parola kontrolü yapılır
    if (password == '1234'):      # parola doğruysa hoş geldiniz yazdırılır
        print('hoş geldiniz')
    else:                          # parola doğru değilse
        print('parola yanlış') 

else:   
    print('username yanlış')   # username yanlışsa buraya gelir 

#****************************************
# if elif elif elif else

x = int(input('x: ')) #stringi int e çevir çünkü kullanıcıdan string değer alıyor
y = int(input('y: '))

if x > y:
    print('x y den büyük')
elif x == y:
    print('x y eşit')
else:
    print('y x den büyük')


