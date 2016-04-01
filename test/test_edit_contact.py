# -*- coding: utf-8 -*-

from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_new = Contact(firstname ="Maria")
    contact_new.id = contact.id
    contact_new.lastname = contact.lastname
    app.contact.edit_contact_by_id (contact.id, contact_new)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(contact_new)
    if check_ui:
        assert sorted(old_contacts, key = Contact.id_con_max) == sorted(new_contacts, key = Contact.id_con_max)


#def test_edit_first_contact_mn(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname = "test"))
#    app.contact.edit(Contact(middlename="M"))

#def test_edit_first_contact_sn(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname = "test"))
#    app.contact.edit(Contact(lastname="Artemieva"))
