import bottle
from datetime import *
import random
import os
import hashlib
from model import Uporabnik, Kviz, Igra1, Igra2

uporabniki = {}

skrivnost = 'TOP SECRET'

for ime_datoteke in os.listdir('uporabniki'):
    uporabnik = Uporabnik.nalozi_stanje(os.path.join('uporabniki', ime_datoteke))
    uporabniki[uporabnik.uporabnisko_ime] = uporabnik

def trenutni_uporabnik():
    uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret=skrivnost)
    if uporabnisko_ime is None:
        bottle.redirect('/')
    return uporabniki[uporabnisko_ime]

# se ne shranjenemu uporabniku doda novo zbirko, shranjenemu pa vrne svojo zbirko
def zbirka_uporabnika():
    return trenutni_uporabnik().zbirka

def shrani_trenutnega_uporabnika():
    uporabnik = trenutni_uporabnik()
    uporabnik.shrani_stanje(os.path.join('uporabniki', f'{uporabnik.uporabnisko_ime}.json'))


@bottle.get('/')
def osnovna_stran():
    shrani_trenutnega_uporabnika()
    return bottle.template('osnovna_stran.html')

@bottle.post('/')
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    geslo = bottle.request.forms.getunicode('geslo')
    h = hashlib.blake2b()
    h.update(geslo.encode(encoding='utf-8'))
    zasifrirano_geslo = h.hexdigest()
    if 'nov_racun' in bottle.request.forms and uporabnisko_ime not in uporabniki:
        uporabnik = Uporabnik(uporabnisko_ime, zasifrirano_geslo,0)
        uporabniki[uporabnisko_ime] = uporabnik
    else:
        uporabnik = uporabniki[uporabnisko_ime]
        uporabnik.preveri_geslo(zasifrirano_geslo)
    bottle.response.set_cookie('uporabnisko_ime', uporabnik.uporabnisko_ime, path='/', secret=skrivnost)
    bottle.redirect('/')

@bottle.get('/')
def osnovna_stran():
    return bottle.template('osnovna_stran.html')

@bottle.get('/navodila/')
def prva_stran():
    return bottle.template('prva_stran.html')





bottle.run(debug=True, reloader=True)