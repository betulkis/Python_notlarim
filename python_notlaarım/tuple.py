list = [1, 2, 3]

tuple = (1, 'iki', 3)  # parantez isteğe bağlı

print(type(list))
print(type(tuple))

print(list[1]) # 1.indeksteki eleman
print(tuple[1])

print(len(tuple))  # eleman sayısı
print(len(list))

# tuple da herhangi bir elemana atama işlemi yapamıyoruz 

list = ['ali', 'veli']
tuple = ('damla', 'ayşe')

list[0] = 'ahmet'  #ali ahmete dönüşür ama tuple da bu olmaz
#tuple[0] = 'deniz'  # damla deniz olMaz

print(list)
print(tuple)

# count kaç kez tekrarlandığı söylenir print(tuple.count('ayşe'))

