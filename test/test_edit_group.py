# -*- coding: utf-8 -*-

def test_edit_first_group_name(app):

    app.session.login(username="admin", password="secret")
    app.group.edit("name", "new name")
    app.session.logout()


def test_edit_first_group_header(app):

    app.session.login(username="admin", password="secret")
    app.group.edit("header", "new header")
    app.session.logout()


def test_edit_first_group_footer(app):

    app.session.login(username="admin", password="secret")
    app.group.edit("footer", "new footer")
    app.session.logout()