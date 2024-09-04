numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)
print(val)

val = max(letters)
print(val)


val = numbers[3:6]  # 3. indeksten 6.ya kadar 6.yok
print(val)

val = numbers[:3]   #baştan başla 3.indekse kadar    [4:] = 4.indeksten başla sona kadar
print(val)

numbers.append(49)  # 49u  listeye ekler
print(numbers)



numbers.insert(3, 78)  # insert() metodu 3.indekse 78 ekle
print(numbers)

# pop() eleman siler.  numbers.pop() ve numbers.pop(-1) sondaki elemanı siler (0)ilk elemanı siler

# numbers.remove(49) silmek istediğin karakteri verirsin

# numbers.sort() liste sayısal olarak sıralanır

# years dizisinde kaç tane 1998 değeri var:  result = years.count(1998)





