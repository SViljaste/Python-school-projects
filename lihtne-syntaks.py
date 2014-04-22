# !/usr/bin/python
# _*_ coding: utf-8 _*_
# Tere täpiline kommentaar
import datetime
import sys

print 'Tere maailm!'

t2na = datetime.datetime.now()

# print t2na
#print type(t2na), dir(t2na)

# len = length
print len(sys.argv)

for arg in sys.argv:
    print "Argument", arg
    print "Sees"

# Võib kasut False
if True:
    print "Tõene"
else:
    print "Vale"
    i = "sdasd" + 2

print "Väljas"
