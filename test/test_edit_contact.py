# -*- coding: utf-8 -*-

from model.contact import Contact


def test_edit_first_contact_fn(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname ="Maria")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    app.contact.edit(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key = Contact.id_con_max) == sorted(new_contacts, key = Contact.id_con_max)

#def test_edit_first_contact_mn(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname = "test"))
#    app.contact.edit(Contact(middlename="M"))

#def test_edit_first_contact_sn(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname = "test"))
#    app.contact.edit(Contact(lastname="Artemieva"))
