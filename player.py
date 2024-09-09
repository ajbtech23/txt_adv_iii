import items

class Player:
    def __init__(self):
        self.inventory = [items.Rock(), items.Dagger(), 'Gold(5)', 'Crusty Bread']

    def print_inventory(self):
        print("Inventory:\n")
        for index, item in enumerate(self.inventory, 1):
            print(f"{index}. {item}")
        best_weapon = self.most_powerful_weapon()
        print(f"Your best weapon is your {best_weapon}")

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None

        for weapon in self.inventory:
            try:
                if weapon.damage > max_damage:
                    best_weapon = weapon
                    max_damage = weapon.damage
            except AttributeError:
                pass

        return best_weapon
