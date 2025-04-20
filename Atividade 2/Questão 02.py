# 2. Controle de Estoque Inteligente
import json
import os

class Inventory:
    def __init__(self, filename='estoque.json'):
        self.filename = filename
        self.products = self.load_products()

    def load_products(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_products(self):
        with open(self.filename, 'w') as f:
            json.dump(self.products, f, indent=4)

    def add_product(self, name, quantity, price):
        self.products.append({'name': name, 'quantity': quantity, 'price': price})
        self.save_products()

    def show_inventory(self):
        total = 0
        for p in self.products:
            subtotal = p['quantity'] * p['price']
            total += subtotal
            print(f"{p['name']} - {p['quantity']} unidades - R${p['price']} (Total: R${subtotal})")
        print(f"Valor total do estoque: R${total}")