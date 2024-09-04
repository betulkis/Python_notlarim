# studente ın da init metodu olursa ve printi olsa studentın initi personun initini ezer
# ama bunu istemiyoruz tamma ezsin ama ezdikten sonra da yine personun init metodunu çalıştırması gerekiyor sonuçta studenttan bi şeyler ürettiğinde yine personın özelliklerini de başlatıyor olması lazım . ikisi de olması lazım yani !
# studentta hem kendine has şeylerin hem de personun özellikleriolması için studentta init içerisinde de  Person.__init__(self)  [personun init metodu da çalıştırılmış olacak] demen gerekiyor ****
# ----ÖNEMLİ-------


class Person():  
    def __init__(self):  
        print('Person Created') 

class Student(Person):  # persondan türetilecek student classı
    def __init__(self):
        Person.__init__(self) #[personun init metodu da çalıştırılmış olacak] 
        print('Student Created')  

p1 = Person()
s1 = Student()

#  Person.__init__(self) bu olmazsa student çalışınca persondan aldığı özellikler yazdırılmaz