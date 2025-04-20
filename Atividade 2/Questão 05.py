# 5. Gerenciador de Contatos
import json
import os

class ContactManager:
    def __init__(self, filename='contatos.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def add_contact(self, name, phone, email):
        self.contacts.append({'name': name, 'phone': phone, 'email': email})
        self.save_contacts()

    def search_contact(self, name):
        found = [c for c in self.contacts if name.lower() in c['name'].lower()]
        for c in found:
            print(f"Nome: {c['name']} - Telefone: {c['phone']} - Email: {c['email']}")
