# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app, json_contacts, db, check_ui):
    contact=json_contacts
    app.open_home_page()
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_con_max) == sorted(new_contacts, key = Contact.id_con_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_con_max) == sorted(app.group.get_contact_list(), key=Contact.id_con_max)