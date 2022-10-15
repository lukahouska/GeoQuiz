import bottle
import random
import os
import hashlib
from bottle import error
from model import Uporabnik, Kviz, Igra1, Igra2

uporabniki = {}

skrivnost = 'TOP SECRET'

for ime_datoteke in os.listdir('uporabniki'):
    uporabnik = Uporabnik.nalozi_stanje(os.path.join('uporabniki', ime_datoteke))
    uporabniki[uporabnik.uporabnisko_ime] = uporabnik

def trenutni_uporabnik():
    uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret=skrivnost)
    if uporabnisko_ime is None:
        bottle.redirect('/prijava/')
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
    return bottle.redirect('/navodila/')

@bottle.get('/prijava/')
def prijava_get():
    return bottle.template('prijava.html')

@bottle.post('/prijava/')
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

@bottle.post('/odjava/')
def odjava():
    bottle.response.delete_cookie('uporabnisko_ime', path='/')
    bottle.redirect('/')

@bottle.get('/navodila/')
def prva_stran():
    return bottle.template('prva_stran.html')

@bottle.post('/level1/')
def level1_post():
    bottle.redirect('/level1/')

@bottle.get('/level1/')
def level1():
    igra1 = Igra1(0, [], [], [])
    igra1.pridobi_drzave()
    return bottle.template('level1.html', igra1=igra1)

@bottle.post('/odgovor/<igra1>/<drzava>/')
def preveri_odgovor(igra1, drzava):
    izbrani_odgovor = bottle.request.forms.getunicode('odgovor')
    if izbrani_odgovor == drzava:
        igra1.pravilni += 1
    bottle.redirect('/igra1/')


@error(500)
def error500(e):
    return bottle.template('napaka.html')

bottle.run(debug=True, reloader=True)