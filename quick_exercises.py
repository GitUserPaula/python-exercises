from datetime import date
from datetime import datetime
import random


# this is how I can escape characters in a string
print ("this isn\'t flying, this is falling with style!")

fifth_letter = "monty" [4]
print (fifth_letter)

favorite_food = "Spaguetti"
print (len(favorite_food))

print (favorite_food .lower())

print (favorite_food. upper())

pi = 3.14
print (str(pi))

ministry = "the ministry of silly walks"
print (len(ministry))
print (ministry.upper())

the_machine_goes = "ping!"
print (the_machine_goes)

print ("I " + "am " + "a lion")

a = "lion"
b = "tiger"

print ("the %s and the %s are felines" % (b, a))

today = date.today()
today_time= datetime.now()
print (today)
print (today.month)
print (today.year)
print (today.day)

print ("%02d/%02d/%04d" % (today.day, today.month, today.year))
print ("%02d:%02d:%02d" % (today_time.hour, today_time.minute, today_time.second))

#random.randint(10, 1)

print('cats', 'dogs', 'mice', sep=',')


# Definición de una variable global
contador = 0

def incrementar_contador():
    # El Call Stack intenta asignar un valor a 'contador'
    # Python asume que 'contador' es una variable LOCAL a la función.
    contador = contador + 1 
    print(contador)

# La ejecución falla en esta línea:
incrementar_contador()

# El error será: UnboundLocalError: local variable 'contador' referenced before assignment