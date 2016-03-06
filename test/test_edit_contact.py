# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    print("Index is "+str(index))
    contact = Contact(firstname ="Maria")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key = Contact.id_con_max) == sorted(new_contacts, key = Contact.id_con_max)

#def test_edit_first_contact_mn(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname = "test"))
#    app.contact.edit(Contact(middlename="M"))

#def test_edit_first_contact_sn(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname = "test"))
#    app.contact.edit(Contact(lastname="Artemieva"))
