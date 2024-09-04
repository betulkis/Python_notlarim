def usalma(number):  # 'fonksiyon' döndürme 
    def inner(power):
        return number ** power   # üs alma
    
    return inner

two = usalma(2)   # usalma fonksiyonuna 2 değerini gönderdiğimizde
three = usalma(3) # değer değil de fonksiyon göndereceğiz
print(two(3))
 
