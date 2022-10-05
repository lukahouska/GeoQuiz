from model import Igra1, Igra2, Kviz


slovar_drzav = {"Slovenija":"LJUBLJANA", "Avstrija":"DUNAJ", "Nemčija":"BERLIN", "Francija":"PARIZ",
 "Italija":"RIM", "Španija":"MADRID", "Poljska":"VARŠAVA", "Romunija":"BUKAREŠTA", "Nizozemska":"AMSTERDAM", 
 "Belgija":"BRUSELJ", "Grčija":"ATENE", "Češka":"PRAGA", "Portugalska":"LIZBONA", "Madžarska":"BUDIMPEŠTA",
  "Švedska":"STOCKHOLM", "Bolgarija":"SOFIJA", "Danska":"Kobenhavn", "Finska":"HELSINKI", "Slovaška":"BRATISLAVA",
   "Irska":"DUBLIN", "Hrvaška":"ZAGREB", "Litva":"VILNA", "Latvija":"RIGA", "Estonija":"TALIN", "Ciper":"NIKOZIJA",
    "Luksemburg":"LUKSEMBURG", "Malta":"VALLETA"}


def pozeni_vmesnik():
    kviz = Kviz(0)

    print("Pozdravljeni!\nTa geografska igra je sestavljena iz dveh nivojev.\nZa napredovanje na naslednji nivo potrebujete vsaj 9/10 pravilnih odgovorov.\nZa vsak pravilni odgovor dobite eno točko.")
    print("=========================================")

#nova stran
    print("LEVEL 1")
    print("\nMed štirimi možnimi odgovori državi določite pripadajoče glavno mesto.")


    igra1 = Igra1(0)
    seznam_drzav = Igra1.pridobi_drzave(slovar_drzav)
    #stevilo_pravilnih = 0
    #skupne_tocke = 0
    for i in range(10):
        print("drzava:" + seznam_drzav[i])
        odgovor = input("glavno mesto:")
        pravilnost = Igra1.preveri_odgovor(igra1, odgovor, slovar_drzav, seznam_drzav[i])
        if pravilnost:
            #stevilo_pravilnih += 1
            igra1.pravilni += 1
            kviz.skupne_tocke += 1
            print("Pravilen odgovor")
        else:
            print("Napačen odgovor")
    if igra1.pravilni >= 9:
        print(f"Pravilno ste odgovorili na {igra1.pravilni!r}/10 vprašanj.")
    else:
        print(f"Pravilno ste odgovorili na {igra1.pravilni!r}/10 vprašanj. Na žalost to ni dovolj za naslednji nivo.")
        

#nova stran
    if igra1.pravilni >= 9:
        print("LEVEL 2")
        print("\nZa vsako državo pripišite pripadajoče glavno mesto.")

        igra2 = Igra2(0)
        seznam_drzav = Igra2.pridobi_drzave(slovar_drzav)
        #stevilo_pravilnih = 0
        for i in range(10):
            print("drzava:" + seznam_drzav[i])
            odgovor = input("glavno mesto:")
            pravilnost = Igra2.preveri_odgovor(igra2, odgovor, slovar_drzav, seznam_drzav[i])
            if pravilnost:
                igra2.pravilni += 1
                kviz.skupne_tocke += 1
                print("Pravilen odgovor")
            else:
                print("Napačen odgovor")
            
        print(f"\nPravilno ste odgovorili na {igra2.pravilni!r}/10 vprašanj.")
    elif igra2.pravilni < 9:
        pass

#level 3?
#nova stran
    if kviz.skupne_tocke < 10:   
        print(f"Očitno geografija ni vaše področje. Skupno število točk: {kviz.skupne_tocke!r}.\nNa prvi strani si lahko pogledate na katero mesto vas to uvršča.")
    elif 10 <= kviz.skupne_tocke <= 15:
        print(f"Soliden rezultat vendar zmorete bolje. Skupaj ste zbrali {kviz.skupne_tocke!r} točk.\nNa prvi strani si lahko pogledate na katero mesto vas to uvršča.")
    elif kviz.skupne_tocke > 15:
        print(f"Odlično! Skupaj ste zbrali {kviz.skupne_tocke!r} točk.\nNa prvi strani si lahko pogledate na katero mesto vas to uvršča.")
        



    



pozeni_vmesnik()