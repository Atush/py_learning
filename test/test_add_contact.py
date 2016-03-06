# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Ivanych", lastname="Petrov", nickname="petya",
                               title="testing3", company="gasprom", address="NY", homephone="sweet home",
                               mobile="1234567", workphone="7654321", fax="1234", email="email@email.ru", email2="email2@email.ru",
                               email3="email3@email.ru", homepage="index.ru", bday="17", bmonth="March",
                               byear="1990", aday="27", amonth="September", ayear="2000",
                               address2="Soviet Union", phone2="sweet-sweet home", notes="be prepared")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_con_max) == sorted(new_contacts, key = Contact.id_con_max)
