#!/usr/bin/env python3

import sys
import random
import datetime

from ssb_data import FEMALE_FIRSTNAMES, MALE_FIRSTNAMES, LASTNAMES
NAMELISTS = [FEMALE_FIRSTNAMES, MALE_FIRSTNAMES, ]

from random_data import EMAILDOMAINS, STREETNAMES, STREETSUFFIX

##

MIN_AGE = 10
MAX_AGE = 45

##


def generate_address():
    address = "{}{} {}".format(random.choice(STREETNAMES),
                               random.choice(STREETSUFFIX),
                               random.randint(1,1000))
    return address


def generate_firstname(double_firstname=None, dash_firstname=None,
                       namelist=None):
    if double_firstname is None:
        double_firstname = bool(random.getrandbits(1))
    if dash_firstname is None:
        dash_firstname = bool(random.getrandbits(1))
    if namelist is None:
        namelist = list(random.choice(NAMELISTS))
    
    firstname = random.choice(namelist)
    if double_firstname:
        namelist.remove(firstname)
        dash_firstname = bool(random.getrandbits(1))
        second_firstname = random.choice(namelist)

        if dash_firstname:
            firstname += "-"
        else:
            firstname += " "

        firstname += second_firstname

    return firstname


def generate_phone_number():
    return "+47{}{}".format(random.choice([4,9]), random.randint(0000000, 9999999))


def generate_email(person):
    email = "{}.{}@{}".format(person['firstname'], person['lastname'],
                              random.choice(EMAILDOMAINS))
    return email.lower().replace(" ", "")


def generate_dob():
    year = datetime.datetime.now().year - random.randint(MIN_AGE, MAX_AGE)
    month = random.randint(1, 12)
    day = random.randint(1, 28) # skip last days to not worry about short months
    dob = datetime.datetime(year, month, day).strftime('%Y-%m-%d')
    return dob


def generate_person():
    person = {}

    person['firstname'] = generate_firstname()
    person['lastname'] = random.choice(LASTNAMES)
    person['email'] = generate_email(person)
    person['phone_number'] = generate_phone_number()
    person['address'] = generate_address()
    person['postal_code'] = random.randint(0000, 9999)
    person['date_of_birth'] = generate_dob()

    return person


def main():
    if len(sys.argv) == 2:
        wanted_persons = int(sys.argv[1])
    else:
        print("need number of wanted persons as first parameter")
        sys.exit()
    

    persons = []
    for i in range(0, wanted_persons):
        persons.append(generate_person())


    from pprint import pprint
    pprint(persons)

if __name__ == '__main__':
    main()
