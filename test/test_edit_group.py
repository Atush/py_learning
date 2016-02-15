# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_first_group_name(app):

    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="new name"))
    app.session.logout()


def test_edit_first_group_header(app):

    app.session.login(username="admin", password="secret")
    app.group.edit(Group(header="new header"))
    app.session.logout()


def test_edit_first_group_footer(app):

    app.session.login(username="admin", password="secret")
    app.group.edit(Group(footer="new footer"))
    app.session.logout()