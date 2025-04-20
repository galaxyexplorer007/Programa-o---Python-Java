# 4. Sistema Bancário com Login
import json
import os

class BankSystem:
    def __init__(self, filename='usuarios_banco.json'):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {}

    def save_users(self):
        with open(self.filename, 'w') as f:
            json.dump(self.users, f, indent=4)

    def register_user(self, username, password):
        if username not in self.users:
            self.users[username] = {'password': password, 'balance': 0.0, 'transactions': []}
            self.save_users()

    def login(self, username, password):
        return self.users.get(username, {}).get('password') == password

    def deposit(self, username, amount):
        self.users[username]['balance'] += amount
        self.users[username]['transactions'].append(f"Depósito: R${amount}")
        self.save_users()

    def withdraw(self, username, amount):
        if self.users[username]['balance'] >= amount:
            self.users[username]['balance'] -= amount
            self.users[username]['transactions'].append(f"Saque: R${amount}")
            self.save_users()
        else:
            print("Saldo insuficiente.")

    def show_transactions(self, username):
        print(f"Transações de {username}:")
        for t in self.users[username]['transactions']:
            print(t)