#!/usr/bin/python
# _*_ coding: utf-8 _*_
# 1. väljastab käsurea argumentide arvu ja nende väärtused
# (iga argument eraldi real)
#
# vajalik selleks, et importida python 3 versiooni süntaksit.
from __future__ import print_function

# vajalik süsteemne moodul sys, selleks, et argumente käsurealt lugeda.
import sys

# Täiendus 4. ----
# vajalik moodul kaasaja konfifaili kirjutmaiseks.
try:
    import yaml
except ImportError:
    print("See programm vajab yaml moodulit!")
    print("paigaldamiseks: sudo apt-get install python-yaml")
# Miks exit(1,2,3 jne on vajalik selleks, et kasutada veatöötluses sisenditena mujal)   
    sys.exit(1)
#----

# Täiendus 1. ----
if len(sys.argv) != 3:
    print("Argumentide arv on vale!")
# sys.argv[0] on sama, mis bashis $0 ehk programmi enda nimi
    print("Käivita programm vastavalt:", sys.argv[0], "sisendfail väljundfail")
    sys.exit(1)
#----

print("Argumentide arv on:", len(sys.argv))

# Täiendus 2. ----
# Avan sisendfaili
ifh = open(sys.argv[1], 'r')
# Avan väljundfaili.
ofh = open(sys.argv[2], 'w')
# Loendame ridu
for line in ifh.readline():
   # print(line)
    ofh.write(line)
#----

# Täiendus 3. ----
# Expection erroris kinni püüda IOErrori nt 
# (kui faili ei saa lugeda, siis exit 1)
# Slaidid 41
# Kodutöös peavad try: olema kõikide failide kohta.
try:
    ifh = open(sys.argv[1], 'r')
except IOError:
    print("sisendfaili avamine ebaõnnestus!")
    sys.exit(2)

#kas *fail* on olemas?
#kas ** on olemas?
#----

# Eemaldatud Täiendus 2.-ga
#for arg in sys.argv:
#    print("Argument:", arg)

print("programm lõpetas töö")





