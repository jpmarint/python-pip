class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def avanza(self):
        print("Ando caminando")


class Ciclista(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def avanza(self):
        print('Ando pedealeando en bicicleta')

def main():
    persona = Persona("Juan Pa")
    persona.avanza()

    ciclista = Ciclista("Jean Paul")
    ciclista.avanza()


if __name__ == '__main__':
    main()