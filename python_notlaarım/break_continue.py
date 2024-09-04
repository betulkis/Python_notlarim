# k ya denk geldiğinde döngü durdurulur

name = 'Sadık turan'

for letter in name:
    if letter == 'k':
        break
    print(letter)


#break döngüden tamamen çıkış yapıyor. continue sadecec o anki döngü turunu iptal ediyor kaldığı yerden devam ediyor

name = 'Sadık turan'

for letter in name:
    if letter == 'k':  
        continue            # k yı yazmaz kalanı devam ettirir
    print(letter)


 