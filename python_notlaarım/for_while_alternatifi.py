for x in range(10):   #10 dahil değil 0 dan 10 a kadar olan sayıları yazdırır
    print(x) 

# yukarıdaki işlemi dizi şeklinde farklı yolla da yapabiliriz:

numbers = [x for x in range(10)]  # 0 da n 10 a kadar sayıları tek tek alıyoruz x in range(10) ... aldığımız her değeri x in içine atıyoruz. x in içine gelen değerler diiznin içierisindeki elemanları temsil ediyor
print(numbers)

#*****************************
# hello bir dizi şeklinde çevrilip harf harf yazdırma

myString = 'Hello'
myList = []

for letter in myString:
   myList.append(letter)
print(myList)

# yukarıdakinin daha kolay yazımı:

myList = [letter for letter in myString]
print(myList)

#ikisinin çıktısı da ['H', 'e', 'l', 'l', 'o']


years = [1983, 1975, 2004, 2002]
ages = [2024-farketmez for farketmez in years]         # ! * ! * ! * ! * ! * ! * !
print(ages)

# for farketmez in years = döngü burada öncesinde istediğin işlemi yaptırabilirsin örn:

results = [x if x%2==0 else 'TEK' for x in range(1,10)]
print(results)