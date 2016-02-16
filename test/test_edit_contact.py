# -*- coding: utf-8 -*-

from model.contact import Contact


def test_edit_first_contact_fn(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "test"))
    app.contact.edit(Contact(firstname ="Maria"))


def test_edit_first_contact_mn(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "test"))
    app.contact.edit(Contact(middlename="M"))


def test_edit_first_contact_sn(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "test"))
    app.contact.edit(Contact(lastname="Artemieva"))
