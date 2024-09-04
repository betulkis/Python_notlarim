x = 1

while x <= 20: #koşul
    print(x)
    x = x + 1
print('bitti')

#*************
# if y % 2==0:  sadece çift sayıları yazdırmak için 0, tek için 1 

y = 1
while y <= 30:
    if y % 2==0:  #if ten sonra : unutma 
        print(y)
    y += 1
    
#***************

# name nin içine bir değer girmedikçe sürekli bize isminizi giriniz diyecek 

name = ''
while not name:
    name = input('isminizi giriniz: ')



    