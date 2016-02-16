# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_first_group_name(app):
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    app.group.edit(Group(name="new name"))


def test_edit_first_group_header(app):
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    app.group.edit(Group(header="new header"))


def test_edit_first_group_footer(app):
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    app.group.edit(Group(footer="new footer"))
