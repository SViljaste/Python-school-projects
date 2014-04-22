# Muutuja omistamine Käib võrdusmärgi abil
a = 5                               # Täisarv (int)
b = 0.5                             # Ujukomaarv (float)
c = 'Mina olen sõne'
d = ['Mina', 'olen', 'massiiv']
e = {'Mina': 'Me', 'Sina':'You'}
a = 5 + 3a = a + 1                 # Sama mis:a += 1

#Operaatorid
Omistamine:       =
Võrdne:           ==
Mitte võrdne:     !=
Suurem kui:       >=
Väiksem kui:      <=
Loogiline 'ja':   and
Loogiline 'või':  or
Loogiline täiend: not
Liitmine:         +
Lahutamine:       -
Korrutamine:      *
Jagamine:         /
Jagamisjääk:      %
Omistamisega:    += -= *= /= %=

#Sõne funktsioonid
s.replace(otsitav, asendatav)Tagastab sõne kus on asendus teostatud
s.find(otsitav)Leitu positsioon: 0-...Kui ei leitud: -1
s.split(eraldaja)Tagastab massiivi
s.lower()
s.upper()
s.startswith(otsitav)tagastab True või False
s.endswith(otsitav)tagastab True või False
s.strip()tagastab sõne kus tühikud algusest ja lõpust on eemaldatud

#Treppimine ehk indenting
Blokki alustavad: for, while, if, else, elif, def
Pseudo-kood:
blokkidest väljas kood
välimist blokki alustav lause:
→→välimise bloki kood
→→sisemist blokki alustav lause:
→→→→sisemise bloki kood
→→→→sisemise bloki kood
→→välimise bloki kood
blokkidest väljas kood

#For tsükkel
foreach tsükli moodi PHP/C# keeles
Toetab break ja continue lauseid
Pseudokoodi näide

tee_midagi_enne_tsüklit
for element in massiiv:
    tee_midagi_elemendiga(element)
tee_midagi_peale_tsüklit()

#Failide töötlemine
Lugemine:
fh=open(failinimi)
fh.read()
fh.readlines()
fh.close()

Kirjutamine:
fh=open(failinimi, 'w')
fh.write(puhver)
fh.close()

#Massiiv (list)
Massiiv (list) on järjestatud objektide kogumi hoidmiseks
Elementideks võivad olla kõik muutujad
Elemente saab üle kirjutada
Elemente saab lisada
Korteež (tuple) pole muudetav (mutable)

#Massiivi koodinäide
m = ['a', 'b', 'c']
m.append('d')
m += ['d', 'e']
m.pop()
del(m[indeks])
m.remove(väärtus)

#Alamhulgad
s = [1, 2, 3, 4, 5]

print s[1:]
[2, 3, 4, 5]

print s[1:3]
[2, 3]

print s[-2:]
[4, 5]

print s[-2]
4

t = 'tere maailm'
print t[5:]'maailm'
print t[5:8]'maa'
print t[-3:]'ilm'
print t[-4]'a'

"""
Süntaks ei nõua aga...
Treppimiseks 4 tühikut
Rida ei tohiks ületada 79 sümbolit
Tühjad read funktsioonide ja suuremate koodiplokkide eraldamiseks
Kasuta tühikuid operaatorite ümber ja peale koma
"""

#Nimetamise tavad
"""
Moodulite nimed: lowercase
Funktsioonid: lowercase_with_underscore
Klasside nimed: CamelCase
Konstandid: ALL_UPPERCASE
Klasside privaatsed funktsioonid: _start_with_underscore
Pythoni sisemised funktsioonid: __double_underscore_around__
"""

#Sõnastik (dictionary)
"""
Sõnastik on assiotsiatiivne massiiv
Hoiab seoseid võtme ja väärtuse vahel nt telefoninumber ja isiku nimi
Võtmeks sobivad hashitavad objektid (sõned, numbrid, objektid)
Väärtusteks sobivad kõik muutujad
"""

#Omistamine
d = dict()
d = {'key':'value','key2':'value2'}

#Elemendi lisamine/ülekirjutamine
d['key'] = 'value'

#Võtme eksistentsi kontroll, tagastab True/False
d.has_key('key')

#Elemendi lugemine
x = d['key']

#Võti-väärtus paaride massiiv:
d.items()

#Võti-väärtus paaride iteraator:
d.iteritems()

#Kuvamine
for key, value in d.iteritems():
    print '%s => %s' % (key, value)
    
#Funktsioonid
#Funktsiooni defineerimine:
def korruta(x, y):
    return x*y
    
#Funktsiooni välja kutsumine ja tagastatud väärtuse omistamine:
korruta(3, 4)

#Ka funktsioon on objekt!
#Anonüümne funktsioon:
lambda x,y: x*y

"""
Moodulid

Muutujate nimeruum
Mooduli laadimiseks: import math
Alammooduli laadimiseks täisnimega:import xml.dom.minidom
Moodulist klassi või muutuja laadimiseks: from math import pi
Teise nimega laadimiseks:from math import e as euler
Keskkonnamuutuja: PYTHONPATH
"""

"""
Erindid (exception)

Erindi püüdmise plokkide üldkuju:
try:  
    # Testitav plokk
except ErindiKlass[, objekt]:  
    # Tee midagi
except MuuErindiKlass[, objekt]:  
    # Tee midagi muud
else:  
    # Kui ühtki erindit ei püütud
finally:  
    # Igal juhul käitatav plokk
"""

#Erindi näide:
"""
try:    
    z = 5/0
except ZeroDivisionError:    
    print 'Nulliga jagada ei saa!'
else:    
    print 'Tulemus:', z
finally:    
    print 'Thäts it!'
"""

#OS moodul
"""
import osLaeb operatsioonisüsteemi liidese mooduli

os.path.join('/home', 'lauri')
Tagastab '/home/lauri'

os.path.realpath('../../..')
Tagastab absoluutse tee

os.path.exists
Tagastab tõeväärtuse

os.remove
Kustuta fail
"""

#OPsüsteemi liides
"""
os.chdir(tee)
Muuda aktiivset kataloogi

os.chmod(tee, 0755)
Muuda faili õigusi

os.chown(tee, uid, gid)
Muuda faili omanikku/gruppi

os.mkdir(tee)
Loo kataloog

os.kill(pid)
Tapa protsess
"""

#Stat objekt
"""
obj = os.stat(tee)

print '%o' % obj.st_mode

Omaniku ID: obj.st_uid

Grupi ID: obj.st_gid

Faili suurus: obj.st_size

print datetime.\  
    fromtimestamp(obj.st_mtime)
"""

#Regulaaravaldised
"""
import re

Kas sõne algus vastab mustrile
re.match(muster, sõne)

Kas muster leidub sõnes
re.search(muster, sõne)

Leia kõik mustrile vastavad alamsõned
re.findall(muster, sõne)
"""

#Otsing
"""
Vaikimisi otsib alamsõnet
re.search('m[ae]', 'kalamees') → vastab
re.search('m[ae]', 'kalamaja') → vastab
re.search('m[ae]', 'kala') → ei vasta

Saab panna käituma kui vastavuse funktsiooni:
re.search('^kala$', 'kalab') → ei vasta
re.search('^kala$', 'sakala') → ei vasta
re.search('^kala$', 'kala') → vastab
"""

#Grupeerimine
"""
Veebilehest ISO failide linkide eraldamine:
<a .*?href=\"(.*?\.iso)\">

Koodinäide:
import urllib, re
fh = urllib.urlopen(  
    'http://releases.ubuntu.com/11.04/')
buf = fh.read()
for link in re.findall( 
    '<a .*?href=\"(.*?\.iso)\">', buf):
        print link
"""
















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    















