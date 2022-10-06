# model za projektno
import random
from string import ascii_lowercase
import json

class Uporabnik:
    def __init__(self, uporabnisko_ime, zasifrirano_geslo,skupne_tocke):
        self.uporabnisko_ime = uporabnisko_ime
        self.zasifrirano_geslo = zasifrirano_geslo
        self.skupne_tocke = skupne_tocke

    def v_slovar(self):
        return {
            'uporabnisko_ime': self.uporabnisko_ime,
            'zasifrirano_geslo': self.zasifrirano_geslo,
            'skupne točke': self.skupne_tocke
        }
    
    def shrani_stanje(self, ime_datoteke):
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(self.v_slovar(), datoteka, ensure_ascii=False, indent=4)


    @classmethod
    def nalozi_stanje(cls, ime_datoteke):
        with open(ime_datoteke) as datoteka:
            slovar_stanja = json.load(datoteka)
            uporabnisko_ime = slovar_stanja['uporabnisko_ime']
            zasifrirano_geslo = slovar_stanja['zasifrirano_geslo']
            skupne_tocke = slovar_stanja['skupne_tocke']
            return cls(uporabnisko_ime, zasifrirano_geslo, skupne_tocke)

    def preveri_geslo(self, zasifrirano_geslo):
        if self.zasifrirano_geslo != zasifrirano_geslo:
            raise ValueError('Napačno geslo!')
        else:
            return True





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
        koncni_nabor = []
        pravilne_drzave = []
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
            pravilne_drzave.append(drzava)
        for sez in nabor:
            sez1 = list(zip(ascii_lowercase, sez))
            koncni_nabor.append(sez1)
        koncni_nabor.append(pravilne_drzave)
        return koncni_nabor




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



    





  

