# model za projektno
import random

class Igra:
    def __init__(self, pravilni):
        #self.stopnja = stopnja
        self.pravilni = pravilni

    def nova_igra():
        pass


    def pridobi_drzave(slovar):
        seznam_drzav = list(slovar.keys())
        stevilo_drzav = len(seznam_drzav)
        sez_indeksov = [random.randint(0, stevilo_drzav -1) for i in range(2)]
        return [seznam_drzav[i] for i in sez_indeksov]

    def preveri_odgovor(self, odgovor, slovar_drzav, drzava):
        odgovor = odgovor.upper()
        if odgovor == slovar_drzav[drzava]:
            #self.pravilni = self.pravilni + 1
            return True
        return False




  

