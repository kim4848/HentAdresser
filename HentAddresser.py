import sys
import urllib2
import json


Vejnavn = raw_input('Vejnavn ')
Husnummer = raw_input('Husnummer ')
Postnummer = raw_input('Postnummer ')


if len(Husnummer)>0:
    Husnummer='&husnr='+Husnummer
else:
    Husnummer=''

if len(Postnummer)>0:
    Postnummer='&postnr='+Postnummer
else:
    Postnummer=''
 

content = urllib2.urlopen('http://dawa.aws.dk/adresser?vejnavn='+Vejnavn+Husnummer+Postnummer).read()
data = json.JSONDecoder(content)

print content


