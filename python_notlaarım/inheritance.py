# inheritance kalıtım: classların birbirinden 'miras alması'

# person isminde class ve name bilgisi lastName bilgisi age vs olacak ya da run() drink() metodları olabilir
# student isminde ya da teacher isminde bir class tanımlarsak sonradan. personda olan görevlerin hepsinin student ve teacherda da olmasını isterim
# özellikleirn hepsini student ve teacher da tekrarlamaktansa student ın persondan miras almasını sağlarım teacherın persondan miras almasını sağlarım 
# Person : name, lastname, age, eat(), run(), drink()
# Student() => Student(Person) ,  Teacher(Person)


class Person():  # persondan bir obje ürettiğimizde init metodunu otomatik olarak çağıracak ve ekrana person created yazdırılıcak
    def __init__(self):  # init metodu self parametresi
        print('Person Created') 

class Student(Person):  # persondan türetilecek student classı
   pass                 # student personda türetiliyo. personun sahip olduğu tüm özellklere studentte sahip

# persondan türettiğimiz bir p1 objesi tanımlarsak çalıştırıdğımızda print yazdırlırı . student tanımlarsak çalıştırınca da student objesini çağırınca studentta bir person olduğundan çalışır

p1 = Person()
s1 = Student()

#***********************
# studente ın da init metodu olursa ve printi olsa studentın initi personun initini ezer
#.. devamı inheritance2.py de