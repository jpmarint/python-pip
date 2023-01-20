class Lavadora:
    def __init__(self) -> None:
        pass

    def wash(self, temperatura="caliente"):
        self._fill_tank(temperatura)
        self._add_soap()
        self._lavar()
        self._centrifugar()

    def _fill_tank(self, temperature):
        print(f'Filling tank with water at {temperature}°C')

    def _add_soap(self):
        print("Adding detergeant")

    def _lavar(self):
        print("Washing")

    def _centrifugar(self):
        print("Rinse")



