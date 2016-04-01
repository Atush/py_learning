import re
from fixture.contact import Contact


def test_all_data_on_home_page(app, db):
    contact_list_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_con_max)
    contact_list_from_db = sorted(db.get_contact_list(), key=Contact.id_con_max)
    i=0
    for contact_ui in contact_list_from_ui:
        print(str(contact_ui.all_emails_from_home_page) + ' and finally ' + str(merge_emails_like_on_home_page(contact_list_from_db[i])))
        assert contact_ui.firstname == contact_list_from_db[i].firstname.strip()
        assert contact_ui.lastname == contact_list_from_db[i].lastname.strip()
        assert contact_ui.all_phones_from_home_page == merge_phones_like_on_home_page(contact_list_from_db[i])
        assert contact_ui.all_emails_from_home_page == merge_emails_like_on_home_page(contact_list_from_db[i])
        i=i+1

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]","",s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                (contact.homephone, contact.mobile, contact.workphone, contact.phone2)))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, (contact.email, contact.email2, contact.email3))))
