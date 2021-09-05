## Pet Shop Application
## Act like a mini-inventory-system

import json
import os.path


##Class Inventory
class Inventory:
    pets = {}

    def __init__(self):
        self.load()

    def add(self, key, qty):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v + qty
        else:
            q = qty
        self.pets[key] = q
        print(f'Added {qty} {key} : total {self.pets[key]}') 

    def remove(self, key, qty):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v - qty
        if q < 0:
            q = 0
        self.pets[key] = q
        print(f'Removed {qty} {key} : total {self.pets[key]}') 

    def display(self):
        for key, qty in self.pets.items():
            print(f'{key} : {qty}')

    def save(self):
        print('Saving Inventory')
        with open('inventory.txt', 'w') as f:
            json.dump(self.pets, f)
        print('Saved')

    def load(self):
        print('Loading Inventory')
        if not os.path.exists('inventory.txt'):
            print('Skipping, Noting to load')
            return
        with open('inventory.txt', 'r') as f:
            self.pets = json.load(f)
        print('Loaded')

def main():
    inv = Inventory()
    while True:
        action = input('Action: Add, Remove, list, Save, Exit: ')

        if action == 'Exit':
            break

        if action == 'List':
            inv.display()

        if action == 'Add' or action == 'Remove':
            key = input('Add an Animal: ')
            qty = int(input('Add Quantity: '))
            if action == 'Add':
                inv.add(key, qty)
            if action == 'Remove':
                inv.remove(key, qty)
    inv.save()

if __name__ == "__main__":
    main()