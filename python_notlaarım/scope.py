# global scope
x = 'global x'

def function():
    # local scope
    x = 'local x'  
    #print(x) içeride print yapılırsa local x de yazdırılır eğer  def içinde x tanımlanmazsa bu print globali yazdırır

function()
print(x)  # local olan değil global olan yazdırılır dıştaki printte


