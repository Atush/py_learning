# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_first_group_name(app):
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="new name")
    group.id = old_groups[0].id
    app.group.edit(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key = Group.id_gr_max) == sorted(new_groups, key = Group.id_gr_max)

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
