# -*- coding: utf-8 -*-

from model.contact import Contact


def test_edit_first_contact_fn(app):

    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname ="Maria"))
    app.session.logout()


def test_edit_first_contact_mn(app):

    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(middlename="M"))
    app.session.logout()


def test_edit_first_contact_sn(app):

    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(lastname="Artemieva"))
    app.session.logout()