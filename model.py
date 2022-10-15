# model za projektno
import random
from string import ascii_lowercase
import json

class Uporabnik:
    def __init__(self, uporabnisko_ime, zasifrirano_geslo,skupne_tocke):
        self.uporabnisko_ime = uporabnisko_ime
        self.zasifrirano_geslo = zasifrirano_geslo
        self.skupne_tocke = skupne_tocke
        self.igra1 = Igra1(0, [], [], [])
        self.igra2 = Igra2(0)

    def v_slovar(self):
        return {
            'uporabnisko_ime': self.uporabnisko_ime,
            'zasifrirano_geslo': self.zasifrirano_geslo,
            'skupne_tocke': int(self.skupne_tocke)
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
            #trenutna_igra = Igra1(0, [], [], [])
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
    def __init__(self, pravilni, mesta, pravilne_drzave, nabori_drzav):
        self.pravilni = pravilni
        self.mesta = mesta
        self.pravilne_drzave = pravilne_drzave
        self.nabori_drzav = nabori_drzav
   
    def pridobi_drzave(self):
        with open('slovar_drzav.json', 'r', encoding='utf-8') as datoteka:
            slovar = json.load(datoteka)
            seznam_drzav = list(slovar.keys())
            stevilo_drzav = len(seznam_drzav)
        
            #nabor = []
            #pravilne_drzave = []
            while len(seznam_drzav) > 10:
                a = random.randint(0, stevilo_drzav -1)
                seznam_drzav.pop(a)
                stevilo_drzav -= 1
            for drzava in seznam_drzav:
                self.pravilne_drzave.append(drzava)
                mesto = slovar[drzava]
                self.mesta.append(mesto)
                seznam_drzav1 = list(slovar.keys())
                stevilo_drzav1 = len(seznam_drzav1)

                nabor_moznosti = [drzava]

                a = seznam_drzav1.index(drzava)
                seznam_drzav1.pop(a)
                while len(seznam_drzav1) > 3:
                    b = random.randint(0, len(seznam_drzav1) -2)
                    seznam_drzav1.pop(b)
                    stevilo_drzav1 -= 1
                nabor_moznosti.extend(seznam_drzav1)
                random.shuffle(nabor_moznosti)
                #nabor.append(nabor_moznosti)
                self.nabori_drzav.append(nabor_moznosti)
                #pravilne_drzave.append(drzava)
                
                

            #sez_mesta = [slovar[d] for d in pravilne_drzave]
            #self.mesta.extend(sez_mesta)
            #self.pravilne_drzave.extend(pravilne_drzave)
            #self.nabori_drzav.extend(nabor)



class Igra2:
    def __init__(self, pravilni):
        self.pravilni = pravilni
        self.seznam_drzav = []
        self.seznam_mest = []

    def pridobi_drzave(self):
        with open('slovar_drzav.json', 'r', encoding='utf-8') as datoteka:
            slovar = json.load(datoteka)
            seznam_drzav = list(slovar.keys())
            stevilo_drzav = len(seznam_drzav)
            while len(seznam_drzav) > 10:
                a = random.randint(0, stevilo_drzav -1)
                seznam_drzav.pop(a)
                stevilo_drzav -= 1
            self.seznam_drzav.extend(seznam_drzav)
            seznam_mest = [slovar[d] for d in seznam_drzav]
            self.seznam_mest = seznam_mest


    
    def preveri_odgovor(odgovor, slovar_drzav, drzava):
        odgovor = odgovor.upper()
        if odgovor == slovar_drzav[drzava]:
            return True
        return False



    





  

