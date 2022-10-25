import random
from tabulate import tabulate

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

autotalli= []

for kierros in range(10):
    autosaatana = auto((f'ABC- {kierros+1}'), random.randint(100, 200), 0, 0)
    autotalli.append((autosaatana))

while autosaatana.kmatka < 10000:
    for i in autotalli:
        autosaatana.kiihdyta(random.randint(-10,15))
        autosaatana.kulje(1)
    else:
        break

vittusaatana = []
for vittusaatana in autotalli:
    vittusaatana.append((autosaatana.rekisteri, autosaatana.hnopeus, autosaatana.thnopeus, autosaatana.kmatka))

print(tabulate(vittusaatana, headers=['Rekisteri', 'Huippunopeus', 'Tämänhetkinen nopeus', 'Kuljettumatka']))

#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan
# väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

