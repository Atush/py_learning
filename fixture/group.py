
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    # possible parameters: name, header, footer
    def edit(self, parameter, new_value):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        # init editing
        wd.find_element_by_name("edit").click()
        # edit group form
        if parameter == "name":
            element_name = "group_name"
        elif parameter == "header":
            element_name = "group_header"
        elif parameter == "footer":
            element_name = "group_footer"
        wd.find_element_by_name(element_name).click()
        wd.find_element_by_name(element_name).clear()
        wd.find_element_by_name(element_name).send_keys(new_value)
        # submit group edition
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # check first group
        wd.find_element_by_name("selected[]").click()
        # init deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

