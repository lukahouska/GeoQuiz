# model za projektno
import random

class Igra1:
    def __init__(self):
        self.pravilni = 0

    def nova_igra():
        pass


    def pridobi_drzave(slovar):
        seznam_drzav = list(slovar.keys())
        stevilo_drzav = len(seznam_drzav)
        while len(seznam_drzav) > 10:
            a = random.randint(0, stevilo_drzav -1)
            seznam_drzav.pop(a)
        return seznam_drzav

    
    def preveri_odgovor(self, odgovor, slovar_drzav, drzava):
        odgovor = odgovor.upper()
        if odgovor == slovar_drzav[drzava]:
            return True
        return False

    





  

