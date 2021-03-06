# -*- coding: utf-8 -*-

from model.contact import Contact
import random


def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list())== 0:
        app.contact.create(Contact(firstname = "test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
