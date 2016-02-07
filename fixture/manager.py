from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class ManageHelper:

    def __init__(self, app):
        self.app = app
        self.app.session = SessionHelper(self.app)
        self.app.group = GroupHelper(self.app)
        self.app.contact = ContactHelper(self.app)