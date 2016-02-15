from selenium.webdriver.support.ui import Select

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

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.firstname)
        self.type("middlename", contact.middlename)
        self.type("lastname", contact.lastname)
        self.type("nickname", contact.nickname)
        self.type("title", contact.title)
        self.type("company", contact.company)
        self.type("address", contact.address)
        self.type("home", contact.homephone)
        self.type("mobile", contact.mobile)
        self.type("work", contact.workphone)
        self.type("fax", contact.fax)
        self.type("email", contact.email)
        self.type("email2", contact.email2)
        self.type("email3", contact.email3)
        self.type("homepage", contact.homepage)
        #Select(wd.find_element_by_name('bday')).select_by_visible_text(contact.bday)
        #Select(wd.find_element_by_name('bmonth')).select_by_visible_text(contact.bmonth)
        self.type("byear", contact.byear)
        #Select(wd.find_element_by_name('aday')).select_by_visible_text(contact.aday)
        #Select(wd.find_element_by_name('amonth')).select_by_visible_text(contact.amonth)
        self.type("ayear", contact.ayear)
        self.type("address2", contact.address2)
        self.type("phone2", contact.phone2)
        self.type("notes", contact.notes)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    # possible parameters: firstname, middlename, lastname
    def edit(self, new_contact_data):
        wd = self.app.wd
        # init editing
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # saving changes
        wd.find_element_by_name("update").click()


    def delete_first_contact(self):
        wd = self.app.wd
        # open home page
        wd.find_element_by_link_text("home").click()
        # check first group
        wd.find_element_by_name("selected[]").click()
        # init deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
