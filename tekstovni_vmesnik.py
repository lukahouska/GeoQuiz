from model import Igra1


slovar_drzav = {"Slovenija":"LJUBLJANA", "Avstrija":"DUNAJ", "Nemčija":"BERLIN", "Francija":"PARIZ",
 "Italija":"RIM", "Španija":"Madrid", "Poljska":"VARŠAVA", "Romunija":"BUKAREŠTA", "Nizozemska":"AMSTERDAM", 
 "Belgija":"BRUSELJ", "Grčija":"ATENE", "Češka":"PRAGA", "Portugalska":"LIZBONA", "Madžarska":"BUDIMPEŠTA",
  "Švedska":"STOCKHOLM", "Bolgarija":"SOFIJA", "Danska":"Kobenhavn", "Finska":"HELSINKI", "Slovaška":"BRATISLAVA",
   "Irska":"DUBLIN", "Hrvaška":"ZAGREB", "Litva":"VILNA", "Latvija":"RIGA", "Estonija":"TALIN", "Ciper":"NIKOZIJA",
    "Luksemburg":"LUKSEMBURG", "Malta":"VALLETA"}


def pozeni_vmesnik():
    print("Pozdravljeni!\nTa geografska igra je sestavljena iz dveh nivojev.\nZa napredovanje na naslednji nivo potrebujete vsaj 9/10 pravilnih odgovorov.\nZa vsak pravilni odgovor dobite eno točko.")
    print("=========================================")

#nova stran
    print("LEVEL 1")
    print("\nMed štirimi možnimi odgovori državi določite pripadajoče glavno mesto.")


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
    if stevilo_pravilnih >= 9:
        print(f"Pravilno ste odgovorili na {stevilo_pravilnih!r}/10 vprašanj.")
    else:
        print(f"Pravilno ste odgovorili na {stevilo_pravilnih!r}/10 vprašanj. Na žalost to ni dovolj za naslednji nivo")
        

#nova stran
    print("LEVEL 2")
    print("\nZa vsako državo pripišite pripadajoče glavno mesto.")

    igra = Igra1()
    seznam_drzav = Igra1.pridobi_drzave(slovar_drzav)
    stevilo_pravilnih = 0
    skupne_tocke = 0
    for i in range(2):
        print("drzava")
        print(seznam_drzav[i])
        odgovor = input("glavno mesto:")
        pravilnost = Igra1.preveri_odgovor(Igra1, odgovor, slovar_drzav, seznam_drzav[i])
        if pravilnost:
            stevilo_pravilnih += 1
            skupne_tocke += 1
            print("Pravilen odgovor")
        else:
            print("Napačen odgovor")
    if stevilo_pravilnih >= 9:
        print(f"\nPravilno ste odgovorili na {stevilo_pravilnih!r}/10 vprašanj.")
    else:
        print(f"\nPravilno ste odgovorili na {stevilo_pravilnih!r}/10 vprašanj. Na žalost to ni dovolj za naslednji nivo")

#level 3?
#nova stran
    if skupne_tocke < 10:   
        print(f"Očitno geografija ni vaše področje. Skupno število točk:{skupne_tocke!r}.\nNa prvi strani si lahko pogledate na katero mesto vas to uvršča.")
    elif 10 <= skupne_tocke <= 15:
        print(f"Soliden rezultat vendar zmorete bolje. Skupno število točk:{skupne_tocke!r}.\nNa prvi strani si lahko pogledate na katero mesto vas to uvršča.")
    elif skupne_tocke > 15:
        print(f"Odlično! Skupaj ste zbrali {skupne_tocke!r} točk.\nNa prvi strani si lahko pogledate na katero mesto vas to uvršča.")
        



    



pozeni_vmesnik()