import os
import re
import csv

def pretvori_v_sekunde(niz):
    skupni_cas = 0
    seznam = niz.strip().split(' ')
    for i in range(1, len(seznam), 2):
        clen = seznam[i]
        if 'day' in clen:
            skupni_cas += int(seznam[i-1])*24*60*60
        if 'hour' in clen:
            skupni_cas += int(seznam[i-1])*60*60
        if 'minute' in clen:
            skupni_cas += int(seznam[i-1])*60
        if 'second' in clen:
            skupni_cas += int(seznam[i-1])
    return skupni_cas

def vsebina_datoteke(ime_datoteke):
    '''Vrne niz z vsebino datoteke z danim imenom.'''
    with open(ime_datoteke) as datoteka:
        vsebina = datoteka.read()
    return vsebina


Najboljsi_resevalci = dict()

def obdelaj_fastest_solvers(ime_dat):
    regex_casi = re.compile(r'color:#555;">(\d*)\D.*?td><td>(.*?)<.*?td><td>(.*?)<')
    vsi = re.findall(regex_casi, vsebina_datoteke(ime_dat))

    najhitrejsi = pretvori_v_sekunde(vsi[0][2])

    povprecni_cas = 0

    for vrstica in vsi:
        mesto, resevalec, cas = vrstica
        mesto, resevalec, cas = int(mesto), resevalec, pretvori_v_sekunde(cas)
        povprecni_cas += cas
        if resevalec not in Najboljsi_resevalci:
            Najboljsi_resevalci[resevalec] = 101 - mesto
        else:
            Najboljsi_resevalci[resevalec] += 101 - mesto

    povprecni_cas = povprecni_cas//len(vsi)
    return (najhitrejsi, povprecni_cas, len(vsi))


def obdelaj_naloge(ime_dat):
    regex = re.compile(r'problem=(\d*)".*? on .*?, (.*?)">(.*?)<.*solvers">(\d*)<')
    vsi = re.findall(regex, vsebina_datoteke(ime_dat))
    return vsi


def Main():
    Po_nalogah = dict()
    for i in range(277,567):
        ime_datoteke = (r'Fastest_Solvers\Naloga_{}'.format(i))
        rezultat = obdelaj_fastest_solvers(ime_datoteke)
        Po_nalogah[i] = rezultat

    slovar_nalog = dict()
    for i in range(6,13):
        ime_datoteke = (r'Arhivi\Stran_{}'.format(i))
        podatki = obdelaj_naloge(ime_datoteke)
        for naloga in podatki:
            ID, datum, ime, resilo = naloga
            najhitrejsi, povprecni_cas, highscore = Po_nalogah[int(ID)]
            slovar_nalog[int(ID)] = (ID, datum, ime, resilo, najhitrejsi, povprecni_cas, highscore)


    polja = ["ID", "Objavljeno", "Ime", "Rešilo #", "Najhitrejši cas", "Povprecni cas", "Highscore #"]
    with open('Tabela.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(polja)
        for i in range(277,557):
            writer.writerow(slovar_nalog[i])

    ### Tabela resevalcev

    Najboljsi_resevalci.pop('')
    
    polja_2 = ["Tekmovalec", "Točke"]
    with open('Tekmovalci.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(polja_2)
        for ime, tocke in Najboljsi_resevalci.items():
            writer.writerow([ime, tocke])
    

     
    



                    
