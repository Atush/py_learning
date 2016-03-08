# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

def random_phone(maxlen):
    symbols = string.digits
    return "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

def random_email(maxlen_username, maxlen_domain):
    symbols = string.ascii_letters
    username = "".join(random.choice(symbols) for i in range(random.randrange(maxlen_username)))
    domain = "".join(random.choice(symbols) for i in range(random.randrange(maxlen_domain))) + "." + "".join(random.choice(string.ascii_letters) for i in range(random.randrange(4)))
    return username + "@" + domain

testdata = [Contact(firstname="", lastname="", address="", homephone="", mobile="", workphone="", email="", email2="", email3="", phone2="")] + [Contact(firstname = random_string("FN", 10), lastname=random_string("LN", 10), address=random_string("address", 20), homephone=random_phone(10), mobile=random_phone(10), workphone=random_phone(10), email=random_email(15,5), email2=random_email(15,5), email3=random_email(15,5), phone2=random_phone(10)) for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_con_max) == sorted(new_contacts, key = Contact.id_con_max)
