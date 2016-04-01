# -*- coding: utf-8 -*-

from model.group import Group
import random


def test_edit_some_group_name(app, db, check_ui):
    if len(db.get_group_list())==0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_new = Group(name="new name")
    app.group.edit_group_by_id(group.id, group_new)
    group_new.id=group.id
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(group_new)
    assert sorted(old_groups, key = Group.id_gr_max) == sorted(new_groups, key = Group.id_gr_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_gr_max) == sorted(app.group.get_group_list(), key=Group.id_gr_max)


#def test_edit_first_group_header(app):
#    if app.group.count()==0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit(Group(header="new header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_edit_first_group_footer(app):
#    if app.group.count()==0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit(Group(footer="new footer"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
