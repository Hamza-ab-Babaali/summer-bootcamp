import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# string multiplication
print("x" * 50)

entered_num=input("Please enter a phone number : \n")

phone_num=phonenumbers.parse(entered_num, "MR")

print(phone_num)

# you might want to get some information about the location that corresponds to a phone number .
print(geocoder.description_for_number(phone_num, "en"))

# for mobile numbers in some countries,
# you can also find out information about wich carrier originally owned a phone number.
print(carrier.name_for_number(phone_num, "en"))

print(timezone.time_zones_for_number(phone_num))








