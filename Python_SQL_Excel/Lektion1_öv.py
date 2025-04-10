#I Python finns det tre grundläggande typer av flow control statements:
#Transfer statements - pass, continue, raise, return osv
#Conditional statements - condtioional statements kan vara if elif och else 
#Iterativa statements - while och for loopar

# Operators = speciella symboler för att utföra olika uträkningar, 
# Assignment operator: =, 
# Arithmetic operator: + - /,
# Comparison operatorx: == != > < >=,
# Logical operator: And, Or, Not,
# Membership operator: In

#----------------------------------------------------------------

#I Python finns det fyra grundläggande datatyper:--------- >>>>>>
#>>>>>>>>>>

#Integers (heltal) - hela numeriska värden som inte har decimaler. Till exempel 1, 5, 100.
#Floats (flyttal) - numeriska värden som har decimaler. Till exempel 3.14, 0.5, 100.0.
#Strings (strängar) - en sekvens av tecken som representerar text. Till exempel "hej", "Python är kul".
#Booleans (booleska värden) - antingen sant (True) eller falskt (False).

#Det finns också flera andra datatyper i Python som är avancerade och bygger på dessa grundläggande datatyper, till exempel listor, tupler, 
# dictionaries och sets. Listor används för att lagra en samling av element, tupler används för att lagra en samling av element som inte kan ändras, 
# dictionaries används för att lagra nyckel-värde-par och sets används för att lagra unika värden utan någon specifik ordning.

#----------------------------------------------------------------

# Python finns det fyra grundläggande datastrukturer:---------->>>>
#>>>>>>>>>>

#Listor (lists) - en samling av element i en ordnad sekvens. Listor kan innehålla element av olika datatyper, inklusive andra listor.
#Tupler (tuples) - en samling av element i en ordnad sekvens, precis som listor. Skillnaden är att tupler är oföränderliga, vilket innebär att elementen inte kan ändras efter att tupeln skapats.
#Dictionaries (dictionaries) - en samling av nyckel-värde-par där varje nyckel är kopplad till ett specifikt värde. Dictionaries är en mycket användbar datastruktur för att lagra och hämta data med hjälp av nycklar.
#Sets (sets) - en samling av unika värden utan någon specifik ordning. Set används ofta för att ta bort dubletter från andra datastrukturer eller för att utföra matematiska operationer på mängder, såsom union eller snitt.
#-------#
#Det finns också flera andra avancerade datastrukturer i Python, såsom deque, 
# heap och defaultdict, som bygger på dessa grundläggande datastrukturer och som ger ytterligare funktionalitet och prestanda för specifika användningsområden.


#-------------------------------------------
#LISTOR
# Lista (list)
min_lista = [1, 2, 3, 4, 5]

# Tuple (tuple)
min_tuple = (1, 2, 3, 4, 5)

# Dictionary (dict)
min_dict = {'a': 1, 'b': 2, 'c': 3}

# Set (set)
mitt_set = {1, 2, 3, 4, 5}

#Hur skapar vi en lista ? 

min_lista1 = [1,2,3,4,5]
b = min_lista1[0]
print(b) # en slice indexering

min_lista1 = [1,2,3,4,5,6]
b = min_lista1[0:5]
print(b) # en slice indexering med första 5

min_lista1 = [1,2,3,4,5]
min_lista1[0] = 10 # gör om den första till värdet 10
print(min_lista1)

min_lista1 = [1,2,3,4,5]
min_lista1.append(6) #lägger till värdet 6
print(min_lista1)

min_lista1 = [1,2,3,4,5]
b = min_lista1[::2]
print(b) # Skriver ut varannat värde i listan

#LIST COMPREHENSION
# Skapa en lista med några element
lista1 = [1, 2, 3, 4, 5]

# Skapa en ny lista som är en kopia av lista1
lista2 = [x for x in lista1]

# för att dubblera värdena med två i listan
lista3 = [x * 2 for x in lista1]

# Skriv ut de två listorna
print("Lista 1: ", lista1)
print("Lista 2: ", lista2)
print("Lista 3: ", lista3)

#-------------------------------------------------------------------------

my_set = {1, 2, 3, 4, 5}
my_set.add(6) # lägger till - Man kan också navända sig av update
print (my_set)

my_set = {1, 2, 3, 4, 5}
my_set.remove(1) #tar bort
print (my_set)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2]) # Plockar ut värdet på plats två

#Plocka ut värden och keys i dicten
min_dict1 = {'a': 1, 'b': 2, 'c': 3}
print(min_dict1.keys())
print(min_dict1.values())
print(min_dict1.items())

#Går även att göras med en for loop
for key, value in min_dict1.items():
	print(key, value)

print(min_dict1['a']) # Hämta värde baserat på en key

#min_dict1['a'] = 25 # Ändra ett keys värde med indexering
#min_dict1.pop['a'] # Ta bort ett key value pair

# Slå ihop en lista ----- list_1 + list_2
# Slå ihop ett set ---- set_1.union(set_2)
# Slå ihop tå tuples ---- a+b

for x in min_lista: #iterera över listans element 
	print(x)

print(len(min_lista))  #längden i en lista 

print(type(min_lista)) #typen i en lista

nya_listan = min_lista
print(f'Hej detta är ett en lista: {nya_listan}')

#----------------------------------------------------------------
#HANTERA DATUM MED DATETIME

#stftime
#strptime

import datetime

datetime.datetime.now()

print(datetime.datetime.now())

#datetime_obj.month --- Hämta ut månad
dt_obj = datetime.datetime(2023, 5, 20)
month = dt_obj.month

print(month)

#----------------------------------------------------------------
#KLASSER CLASS OCH METODER INUTI

#Klasser är en sorts ritning eller mall över ett, eller flera objekt och tydligögr vad objektet ska ha för egenskaper etc.
#Metoder inuti en klass kallas för attrbiut
#Klasser är otroligt bra och gör det enkelt att återvända genom arv (inheritence), dvs parent och child.
# ARV för att dra nytta av att redan ha skrivit attribut och metoder som vi ändå skall använda i vår child class

class MyClass():
    def __init__(self, a, b): #Self är bryggan för andra metoder inuti klassen
        self.a = a
        self.b = b

    def print_values(self):
        print(f'These are the two values: {self.a}, {self.b}')

my_instance = MyClass(a=5, b=3) # Ger objektet värden
my_instance.print_values() # instanstierar och kallar på klassen

#class MyClass(Parentclass): # ARV #

#Kan vi lägga till attribut på child-classen som parent-classen inte har? - JA!
#Kan vi lägga till metoder på child-classen som parent-classen inte har? - JA!
#Kan vi skriva över metoder från parent-classen i child-classen? - JA!

class ParentClass:
    def __init__(self, x):
        self.x = x

class ChildClass(ParentClass):
    def __init__(self, x, y):
        super().__init__(x) #SUPER() --- när vi vill skapa en instans av parentklassen
        self.y = y

child = ChildClass(10, 20)
print(child.x) # Output x dvs 1
print(child.y) # Output y dvs 2 

#COMPOSITION---- SOM ARV och är en alternativ metod till att skpa nya klasser med egenskaper från tidigare skapade klasser.

#Skillnaden mellan composition och arv är att i composition skapar man en ny klass genom att kombinera andra klasser, 
# medan i arv skapar man en ny klass genom att ärva egenskaper och beteenden från en befintlig klass. 
# I composition har man en starkare koppling mellan objekten, eftersom de är direkt beroende av varandra, 
# medan i arv är beroendet mer implicit.

class Engine:
    def start(self):
        print("Bilmotorn har startats")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

car = Car()
car.start() # printar "Bilmotorn har startats"

#----------------------------------------------------------------
#TESTER

#TDD - Test driven development, ompröva kod och se till att den är så pass eror fri som möjligt.
#Testa eventuella fel och förbättra koden innan man skickar den vidare, eller lägger upp den.
# Unittest och integration test - Flöde och specfika eventuella funktionsfel
# Raise för att höja och skapa fel, hur kommer det se ut? Detta kan man skapa själv i sin kod genom raise 
import unittest

#EX 1
def add_numbers(x, y):
    return x + y

class TestAddNumbers(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add_numbers(2, 3), 5)
    
    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)
    
    def test_decimal_numbers(self):
        self.assertEqual(add_numbers(1.5, 2.5), 4.0) 

    # KOllA SÅ ATT ALLA TAL BLIR JÄMNA 
if __name__ == '__main__':
    unittest.main()

#EX 2
#I det här exemplet testar vi funktionen divide() för division med noll. 
#Vi använder assertRaises() för att säkerställa att funktionen faktiskt genererar ett ZeroDivisionError
#-undantag när vi försöker dela med noll. Om divide() inte genererar undantaget, kommer testet att misslyckas.
import unittest

def divide_numbers(x, y):
    if y == 0:
        raise ZeroDivisionError("division by zero")
    return x / y

class TestDivideNumbers(unittest.TestCase):

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_numbers(2, 0)
    
    def test_division_with_non_zero_denominator(self):
        self.assertAlmostEqual(divide_numbers(4, 2), 2.0)
    
if __name__ == '__main__':
    unittest.main()

#SETUP TEST
#I detta exempel använder vi setUp() för att skapa en instans av MyClass med namnet "Alice". 
#Vi kan sedan använda denna instans i våra tester test_get_name() och test_name_type() utan att behöva skapa en ny instans i varje test.  

from unittest import TestCase

class MyClass:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class MyTest(TestCase):
    def setUp(self):
        self.my_object = MyClass(name='Alice')

    def test_get_name(self):
        self.assertEqual(self.my_object.get_name(), 'Alice')

    def test_name_type(self):
        self.assertIsInstance(self.my_object.get_name(), str)

#VAD ÄR SETUP() - TESTMILJÖN
from unittest import TestCase

class MyTest(TestCase):

    def setUp(self):
        self.my_list = [1, 2, 3]

    def test_list_length(self):
        self.assertEqual(len(self.my_list), 3)

        
#I det här exemplet skapas en lista my_list i metoden setUp(), och sedan testas längden av listan i metoden test_list_length(). 
# Eftersom setUp() körs före varje testmetod kan vi vara säkra på att listan finns tillgänglig och är redo att testas i varje test.

