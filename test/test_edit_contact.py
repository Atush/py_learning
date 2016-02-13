# -*- coding: utf-8 -*-


def test_edit_first_contact_fn(app):

    app.session.login(username="admin", password="secret")
    app.contact.edit("firstname", "Maria")
    app.session.logout()


def test_edit_first_contact_mn(app):

    app.session.login(username="admin", password="secret")
    app.contact.edit("middlename", "M")
    app.session.logout()


def test_edit_first_contact_sn(app):

    app.session.login(username="admin", password="secret")
    app.contact.edit("lastname", "Artemieva")
    app.session.logout()