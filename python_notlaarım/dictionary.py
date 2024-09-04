# key - value
# 41 => kocaeli uzun yol aşağıdaki gibi

sehirler = ['kocaeli', 'istanbul']
plakalar = [41, 34]

print(plakalar[sehirler.index('kocaeli')])

# key bilgisi ile value bilgisine ulaşılabilir:
# plakalar = { 'key' : 'value'}

plakalar = { 'kocaeli' : '41', 'istanbul' : 34}

print(plakalar['kocaeli'])
print(plakalar['istanbul'])

# daha önceden olmayan key ekleme
plakalar['ankara'] = 6
print(plakalar)

#*****************************************************

#key value yöntemiyle iç içe bilgiler

users = {
    'sadikturan' : {
        'age' : 36,
        'email' : 'sadik@gmail.com',
        'address' : 'kocaeli',
        'phone' : '05453454434'

    },
    'cinarturan' : {
        'age' : 2,
        'email' : 'cinar@gmail.com',
        'address' : 'kocaeli',
        'phone' : '05453454434'
    }

}

print(users['cinarturan'])

print(users['cinarturan']['age'])  #cınarturan ın age bilgini alır

#*****************dictionary.demo**************************

ogrenciler = {
    '120' : {  #öğrenci numarası
        'ad' : 'Ali',
        'soyad' : ' Yılmaz',
        'telefon' : '532 000 0003'
    }, #2. öğrencinin bilgilerine geçerken virgülü unutma
    '125' : {
        'ad' : 'can',
        'soyad' :'korkmaz',
        'telefon' : '532 000 0002'
    }
}

#bilgileri verilen öğrencileri kullanıcıdan aldığın bilgilerer göre dictionary içinde sakla


ogrenciler = {}

number = input("öğrenci no: ")  #kullanıcıdan veri almak için yapıldı
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler[number]= {
    'ad' :name,
    'soyad' : surname,
    'telefon' : phone
}

print(ogrenciler)