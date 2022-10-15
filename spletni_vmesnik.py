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
        uporabnik = Uporabnik(uporabnisko_ime, zasifrirano_geslo, 0)
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
    shrani_trenutnega_uporabnika()
    uporabnik=trenutni_uporabnik()
    return bottle.template('prva_stran.html', uporabnik = uporabnik)

@bottle.post('/level1/')
def level1_post():
    shrani_trenutnega_uporabnika()
    bottle.redirect('/level1/')

@bottle.get('/level1/')
def level1():
    uporabnik=trenutni_uporabnik()
    igra1 = Igra1(0, [], [], [])
    igra1.pridobi_drzave()
    uporabnik.igra1 = igra1
    return bottle.template('level1.html', igra1=igra1)

@bottle.post('/odgovor/')
def preveri_odgovor():
    uporabnik = trenutni_uporabnik()
    igra1 = uporabnik.igra1
    for i in range(10):
        str_i = str(i)
        izbrani_odgovor = bottle.request.forms.getunicode(str_i)
        if izbrani_odgovor == igra1.pravilne_drzave[i]:
            uporabnik.igra1.pravilni += 1
            uporabnik.skupne_tocke += 1
    shrani_trenutnega_uporabnika()
    if igra1.pravilni > 8:
        bottle.redirect('/level2/')
    bottle.redirect('/intermezzo/')

@bottle.get('/level2/')
def level2():
    uporabnik = trenutni_uporabnik()
    igra2 = Igra2(0)
    igra2.pridobi_drzave()
    uporabnik.igra2 = igra2
    return bottle.template('level2.html', igra2=igra2)

@bottle.post('/odgovor2/')
def preveri_odgovor2():
    uporabnik = trenutni_uporabnik()
    #igra2 = uporabnik.igra2
    for i in range(10):
        str_i = str(i)
        vpisani_odgovor = bottle.request.forms.getunicode(str_i)
        if vpisani_odgovor.upper() == uporabnik.igra2.seznam_mest[i]:
            uporabnik.igra2.pravilni += 1
            uporabnik.skupne_tocke += 1
    shrani_trenutnega_uporabnika()
    bottle.redirect('/intermezzo2/')

@bottle.get('/intermezzo/')
def intermezzo():
    uporabnik = trenutni_uporabnik()
    return bottle.template('intermezzo.html', uporabnik=uporabnik)

@bottle.post('/intermezzo/')
def intermezzo_post():
    shrani_trenutnega_uporabnika()
    bottle.redirect('/navodila/')

@bottle.get('/intermezzo2/')
def intermezzo_2():
    uporabnik = trenutni_uporabnik()
    return bottle.template('intermezzo2.html', uporabnik=uporabnik)

@bottle.post('/intermezzo2/')
def intermezzo_post():
    shrani_trenutnega_uporabnika()
    bottle.redirect('/navodila/')


@error(500)
def error500(e):
    return bottle.template('napaka.html')

bottle.run(debug=True, reloader=True)