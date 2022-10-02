from model import Igra


slovar_drzav = {"Slovenija":"LJUBLJANA", "Avstrija":"DUNAJ", "Nemčija":"BERLIN"}


def pozeni_vmesnik():
    print("Dobrodošli v GeoQuiz")
    print("===========================")
    igra = Igra(0)
    seznam_drzav = Igra.pridobi_drzave(slovar_drzav)
    for i in range(2):
        print("drzava")
        print(seznam_drzav[i])
        odgovor = input("glavno mesto:")
        pravilnost = Igra.preveri_odgovor(Igra, odgovor, slovar_drzav, seznam_drzav[i])
        if pravilnost:
            print("Pravilen odgovor")
        else:
            print("napacen odgovor")

    print("Stevilo pravilnih je {igra.pravilni!r}")
    
        



    



pozeni_vmesnik()