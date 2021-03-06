from model.contact import Contact
from selenium.webdriver.common.by import By
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # go to create contact page
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        #self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        #self.change_field_value("nickname", contact.nickname)
        #self.change_field_value("title", contact.title)
        #self.change_field_value("company", contact.company)
        #self.change_field_value("address", contact.address)
        #self.change_field_value("home", contact.homephone)
        #self.change_field_value("mobile", contact.mobile)
        #self.change_field_value("work", contact.workphone)
        #self.change_field_value("fax", contact.fax)
        #self.change_field_value("email", contact.email)
        #self.change_field_value("email2", contact.email2)
        #self.change_field_value("email3", contact.email3)
        #self.change_field_value("homepage", contact.homepage)
        #Select(wd.find_element_by_name('bday')).select_by_visible_text(contact.bday)
        #Select(wd.find_element_by_name('bmonth')).select_by_visible_text(contact.bmonth)
        #self.change_field_value("byear", contact.byear)
        #Select(wd.find_element_by_name('aday')).select_by_visible_text(contact.aday)
        #Select(wd.find_element_by_name('amonth')).select_by_visible_text(contact.amonth)
        #self.change_field_value("ayear", contact.ayear)
        #self.change_field_value("address2", contact.address2)
        #self.change_field_value("phone2", contact.phone2)
        #self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("entry")[index].find_elements(By.TAG_NAME, "td")[7].click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("entry")[index].find_elements(By.TAG_NAME, "td")[6].click()

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None


    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        #self.select_contact_by_id(id)
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # check index contact
        wd.find_elements_by_name("selected[]")[index].click()
        # init deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # check index contact
        self.select_contact_by_id(id)
        # init deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(id = id, firstname = firstname, lastname = lastname, all_phones_from_home_page = all_phones, all_emails_from_home_page = all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, homephone=homephone, mobile=mobile, workphone=workphone, phone2=phone2, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobile=mobile, workphone=workphone, phone2=phone2)