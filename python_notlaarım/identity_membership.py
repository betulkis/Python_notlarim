# is ve in operatörleri

# Identity operator: is

x = y = [1, 2,3]
z = [1, 2, 3]

print(x==y)
print(x==z)  # listelere atılan değerler aynı olduğu için karşılaştırması true

# ANCAK adres karşılaştırması yapmak istiyorsak is kullanırız

print(x is y)  # true

print(x is z) # x ve z farklı referansa sahip o yüzden false döndürür adresleri aynı değil çünkü
# is operatörünü kullandığımızda objeler aynı mı değilmi buna bakılır değerler önemli değil. aynı adresi tutup tutmadığı önemli




# not is şeklinde de kullanılabilir 


#*************************
# membership operator: in
# liste içerisinde aradığımız bir elemanın olup olmadığını sorarız

x = ['apple', 'banana']
print('banana' in x)   # x içinde banana var mı

name = 'çınar'
print('a' in name) # a var true olur
print('a' not in name) # a yok mu (a var o zaman bu false olur)

# not in şeklinde de kullanılabilir yok mu anlamında
