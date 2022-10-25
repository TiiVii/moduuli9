class auto():
    def __init__(self, rekisteri, hnopeus, thnopeus, kmatka):
        self.rekisteri = rekisteri
        self.hnopeus = hnopeus
        self.thnopeus = thnopeus
        self.kmatka = kmatka

    def kiihdyta(self, muutos):
        self.thnopeus += muutos
        if self.thnopeus>self.hnopeus:
            self.thnopeus=self.hnopeus
        if self.thnopeus<0:
            self.thnopeus=0

    def kulje(self, tuntimaara):
        self.kmatka += (tuntimaara * self.thnopeus)



uusi_auto = auto('ABC-123', 142, 0, 0)

uusi_auto.kiihdyta(30)
uusi_auto.kiihdyta(70)
uusi_auto.kiihdyta(50)

uusi_auto.kulje(2)

uusi_auto.kiihdyta(-200)
print(f'Yhteensä autolla on kuljettu: {uusi_auto.kmatka} km.')



