class Animal:

    def hacerSonido():
        print("Sonido genérico")
    

class Perro (Animal):

    def moverCola():
        print("El perro mueve la cola")
    
print(Animal.hacerSonido())