import phonenumbers

from phonenumbers import geocoder 
from phonenumbers import carrier
pn=phonenumbers.parse("+916302464140")
loc=geocoder.description_for_number(pn,'en')
c=carrier.name_for_number(pn,'en')
print(loc,c)

