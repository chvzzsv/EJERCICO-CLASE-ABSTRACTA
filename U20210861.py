from abc import ABC, abstractmethod

class MiCasa(ABC):
        
    @abstractmethod
    def datos(self):
        pass
    
        
class Persona(MiCasa):
    def __init__(self, nombre, edad, genero):
        self.nombre= nombre
        self.edad= edad
        self.genero= genero

    def datos(self):
        return 'El nombre de una de las personas es {} tiene la edad de {} años, género {}'.format(self.nombre, self.edad, self.genero)
    
class Animal(MiCasa):
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad

    def datos(self):
        return 'El nombre de la mascota es {}, tiene {} meses'.format(self.nombre, self.edad)

class Tienda(MiCasa):
    def __init__(self, productoPrecio):
        self.productoPrecio= productoPrecio

    def datos(self):
        return 'La leche cuesta ${} en el mini super de mi casa'.format(self.productoPrecio)
    
Javier = Persona('Enrique', 20, 'Masculino')
Perro = Animal('Kaiser', 3)
MiniSuper = Tienda(5)
print(Javier.datos())
print(Perro.datos())
print(MiniSuper.datos())