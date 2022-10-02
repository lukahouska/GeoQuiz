from model import Igra1


slovar_drzav = {"Slovenija":"LJUBLJANA", "Avstrija":"DUNAJ", "Nemčija":"BERLIN"}


def pozeni_vmesnik():
    print("Dobrodošli v GeoQuiz")
    print("===========================")
    igra = Igra1()
    seznam_drzav = Igra1.pridobi_drzave(slovar_drzav)
    stevilo_pravilnih = 0
    for i in range(2):
        print("drzava")
        print(seznam_drzav[i])
        odgovor = input("glavno mesto:")
        pravilnost = Igra1.preveri_odgovor(Igra1, odgovor, slovar_drzav, seznam_drzav[i])
        if pravilnost:
            stevilo_pravilnih += 1
            print("Pravilen odgovor")
        else:
            print("Napačen odgovor")

    print(f"Stevilo pravilnih je {stevilo_pravilnih!r}")
    
        



    



pozeni_vmesnik()