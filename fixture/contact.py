from model.contact import Contact
from selenium.webdriver.common.by import By

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
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        #Select(wd.find_element_by_name('bday')).select_by_visible_text(contact.bday)
        #Select(wd.find_element_by_name('bmonth')).select_by_visible_text(contact.bmonth)
        self.change_field_value("byear", contact.byear)
        #Select(wd.find_element_by_name('aday')).select_by_visible_text(contact.aday)
        #Select(wd.find_element_by_name('amonth')).select_by_visible_text(contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # init editing
        wd.find_elements_by_name("entry")[index].find_elements(By.TAG_NAME, "td")[7].click()
        self.fill_contact_form(new_contact_data)
        # saving changes
        wd.find_element_by_name("update").click()
        self.open_home_page()
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
            for element in wd.find_elements_by_name("entry"):
                lastname = element.find_elements(By.TAG_NAME, "td")[1].text
                firstname = element.find_elements(By.TAG_NAME, "td")[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(id = id, firstname = firstname, lastname = lastname))
        return list(self.contact_cache)
