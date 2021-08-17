import phonenumbers

#to take user input eg. +91phonenumber
number = input("Enter the phone number with country code")

#code for the location
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

#code for service provider
from phonenumbers import  carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))
