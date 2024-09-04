name = 'Çınar'
surname = 'Turan'

print('My name is {}' .format(name))    #string ifadeden sonra {} yapıyoruz ve ' ' tırnakları kapatıp  . diyoruz o zaman string ifade üzerinden kullanabileceğimiz string metotları karşımıza gelir bunklardan biri format 

#format metoduna bazı argumanlar gönderebiliyoruz. burdan göndereceğimiz argüman süslü parantez yerine geçecek  

print('My name is {} {}' .format(name, surname))   

result = 200/700
print('the result is {r:1.4}' .format(r=result))
#işlemin sonucu 0.2857142857767 r:1.4 dediğimizde .dan sonraki 4 virgülden sonra kaç basamak yazılacağını söyler .dan önceki sayı ise tam kısım için kaç karakterlik boşluk bırakılacağını belirtiyor 10 yazsak boşluklar olur

#süslü parantez içine değişken ismini yazıp kullanmak için başa f koyulur

print(f'My name is {name}')  