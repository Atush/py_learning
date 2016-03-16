from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

def random_phone(maxlen):
    symbols = string.digits
    return "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

def random_email(maxlen_username, maxlen_domain):
    symbols = string.ascii_letters
    username = "".join(random.choice(symbols) for i in range(random.randrange(maxlen_username)))
    domain = "".join(random.choice(symbols) for i in range(random.randrange(maxlen_domain))) + "." + "".join(random.choice(string.ascii_letters) for i in range(random.randrange(4)))
    return username + "@" + domain

testdata = [Contact(firstname="", lastname="", address="", homephone="", mobile="", workphone="", email="", email2="", email3="", phone2="")] + [Contact(firstname = random_string("FN", 10), lastname=random_string("LN", 10), address=random_string("address", 20), homephone=random_phone(10), mobile=random_phone(10), workphone=random_phone(10), email=random_email(15,5), email2=random_email(15,5), email3=random_email(15,5), phone2=random_phone(10)) for i in range(5)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))