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



uusi_auto = auto('ABC-123', 142, 0, 0)

uusi_auto.kiihdyta(30)
uusi_auto.kiihdyta(70)
uusi_auto.kiihdyta(50)

print(f' Auton tämän hetkinen nopeus kiihdyttelyn jälkeen on: {uusi_auto.thnopeus}')
uusi_auto.kiihdyta(-200)
print(f' Äkkijarrutuksen jälkeen tämän hetkinen nopeus on: {uusi_auto.thnopeus}')
