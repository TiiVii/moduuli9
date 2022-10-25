class auto():
    def __init__(self, rekisteri, hnopeus, thnopeus, kmatka):
        self.rekisteri = rekisteri
        self.hnopeus = hnopeus
        self.thnopeus = thnopeus
        self.kmatka = kmatka

uusi_auto = auto('ABC-123', 142, 0, 0)

print(f'Auton rekisterinumero on: {uusi_auto.rekisteri}\nAuton huippunopeus on: {uusi_auto.hnopeus}\nAuton huippunopeus on: {uusi_auto.thnopeus}\nAuton kuljettu matka on: {uusi_auto.kmatka}')
