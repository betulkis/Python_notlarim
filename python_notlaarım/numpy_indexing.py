import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]
result = numbers[-1]
result = numbers[0:3] # indeks 0 ile 3 arası 3 yok
result = numbers[:3] # 0 dan
result = numbers[3:] # 3 ten sona ilk dahil
result = numbers[::] # tüm liste
result = numbers[::-1] # listenin tersi. adım sayısı sağdan sola 1er1er

                       #0        #1         #2 
numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])  # 2 boyutlu liste 3 e 3 lük matris
result = numbers2[0] # çıktı [0,5,10] 
result = numbers2[2]
result = numbers2[0,2] # 1.satır 2.indeks
result = numbers2[2,1]  
result = numbers2[:,2]  # tüm satırlar tüm satırların 2.indeksi
result = numbers2[:,0] # 0 15 50 gelir
result = numbers2[:,0:2]
result = numbers2[-1,:]
result = numbers2[:2,:2]


