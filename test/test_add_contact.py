# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanych", lastname="Petrov", nickname="petya",
                               title="testing3", company="gasprom", address="NY", homephone="sweet home",
                               mobile="1234567", workphone="7654321", fax="1234", email="email@email.ru", email2="email2@email.ru",
                               email3="email3@email.ru", homepage="index.ru", bday="17", bmonth="March",
                               byear="1990", aday="27", amonth="September", ayear="2000",
                               address2="Soviet Union", phone2="sweet-sweet home", notes="be prepared"))
    app.session.logout()
