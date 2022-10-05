# model za projektno
import random


class Kviz:
    def __init__(self, skupne_tocke):
        self.skupne_tocke = skupne_tocke

class Igra1:
    def __init__(self, pravilni):
        self.pravilni = pravilni

    def pridobi_drzave(slovar):
        seznam_drzav = list(slovar.keys())
        stevilo_drzav = len(seznam_drzav)
        nabor = []
        while len(seznam_drzav) > 10:
            a = random.randint(0, stevilo_drzav -1)
            seznam_drzav.pop(a)
            stevilo_drzav -= 1
        for drzava in seznam_drzav:
            nabor_moznosti = [drzava]
            seznam_drzav1 = list(slovar.keys())
            stevilo_drzav1 = len(seznam_drzav1)
            a = seznam_drzav1.index(drzava)
            seznam_drzav1.pop(a)
            while len(seznam_drzav1) > 3:
                b = random.randint(0, len(seznam_drzav1) -2)
                seznam_drzav1.pop(b)
                stevilo_drzav1 -= 1
            nabor_moznosti.extend(seznam_drzav1)
            random.shuffle(nabor_moznosti)
            nabor.append(nabor_moznosti)
        return nabor
        











class Igra2:
    def __init__(self, pravilni):
        self.pravilni = pravilni

    def pridobi_drzave(slovar):
        seznam_drzav = list(slovar.keys())
        stevilo_drzav = len(seznam_drzav)
        while len(seznam_drzav) > 10:
            a = random.randint(0, stevilo_drzav -1)
            seznam_drzav.pop(a)
            stevilo_drzav -= 1
        return seznam_drzav

    
    def preveri_odgovor(self, odgovor, slovar_drzav, drzava):
        odgovor = odgovor.upper()
        if odgovor == slovar_drzav[drzava]:
            return True
        return False



    





  

