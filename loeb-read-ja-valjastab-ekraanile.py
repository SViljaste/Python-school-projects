# !/usr/bin/python
# _*_ coding: utf-8 _*_
# Programm, mis loeb failist read ja väljastab need ekraanile
import sys


# Kui tahan, et õigete parameetritega skript töötak, pean kirjtuama '!='
if len(sys.argv) != 2:
    print "Viga! Argumentide arv on vale, kasuta ...."
    sys.exit(1)

min = 0
max = 0
fh=open(sys.argv[1])
while True:
    line = fh.readline()
    if not line:
        break
    print int(line)
    if int(line) < min:
        min = int(line)
    elif int(line) > max:
        max = int(line)
print "Min:", min, "Max:", max
# Võtab failinimeks selle, mis käsurealt on antud!
# open avab faili ehk hetkel skripti enda!
# fh=open(sys.argv[1])
# while True:
    # line = fh.readline()

    # split_line = line.split(',')
    # if not line:
        # break
    # print int(line):
    # print split_line[1], split_line[2]
    # for char in split_line[1]:
        # print char    
fh.close()
