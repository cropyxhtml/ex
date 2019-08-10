from contacts.contact import Contact
class ContactsModel:
    def __init__(self):
        pass
    @staticmethod
    def set_contact(n1,n2,n3,n4):
        contact=Contact(n1,n2,n3,n4)
        return contact

    @staticmethod
    def get_contacts(params):
        contacts = []
        for i in params:
            contacts.append(i.to_string())
        return ''.join(contacts)
    @staticmethod
    def del_contact(params, name):
        for i, t in enumerate(params):
            if t.n1 == name:
                del params[i]

