class Pokemon:
    def __init__(self, name, level, type, max_health, is_knocked_out=False):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.health = max_health
        self.is_knocked_out = is_knocked_out

    def lose_health(self, amount):
        self.health -= amount
        print(f"\n{self.name} got attacked and has {self.health} left!")
        if self.health <= 0:
            self.knock_out()

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} has {self.health} now that he healed.")

    def knock_out(self):
        self.is_knocked_out = True
        print(f"{self.name} got knocked out because his life went to 0.")

    def attack(self, poke):
        if self.type == "Grass":
            if poke.type == "Fire":
                print(
                    f"{self.name} deals {self.level/2} damages to {poke.name}!")
                damage = self.level/2
            elif poke.type == "Grass":
                print(
                    f"{self.name} deals {self.level} damages to {poke.name}!")
                damage = self.level
            elif poke.type == "Water":
                print(
                    f"{self.name} deals {self.level*2} damages to {poke.name}!")
                damage = self.level*2
        if self.type == "Fire":
            if poke.type == "Fire":
                print(
                    f"{self.name} deals {self.level} damages to {poke.name}!")
                damage = self.level
            elif poke.type == "Grass":
                print(
                    f"{self.name} deals {self.level*2} damages to {poke.name}!")
                damage = self.level*2
            elif poke.type == "Water":
                print(
                    f"{self.name} deals {self.level/2} damages to {poke.name}!")
                damage = self.level/2
        if self.type == "Water":
            if poke.type == "Fire":
                print(
                    f"{self.name} deals {self.level*2} damages to {poke.name}!")
                damage = self.level*2
            elif poke.type == "Grass":
                print(
                    f"{self.name} deals {self.level/2} damages to {poke.name}!")
                damage = self.level/2
            elif poke.type == "Water":
                print(
                    f"{self.name} deals {self.level} damages to {poke.name}!")
                damage = self.level
        poke.lose_health(damage)


class Trainer:
    def __init__(self, name, potions, pokemons, active_pokemon):
        self.name = name
        self.potions = potions
        self.active_pokemon = active_pokemon
        self.pokemons = pokemons

    def use_potion(self):
        if self.potions:
            self.pokemons[self.active_pokemon].heal(20)
            self.potions -= 1
            print(
                f"{self.name} used a potion on {self.pokemons[self.active_pokemon].name} that has now {self.pokemons[self.active_pokemon].health}")
        else:
            print(f"{self.name} tried to use a potion, but no potions left...")

    def attack(self, other_trainer):
        print(f"{self.name}:")
        self.pokemons[self.active_pokemon].attack(
            other_trainer.pokemons[other_trainer.active_pokemon])
        if other_trainer.pokemons[other_trainer.active_pokemon].is_knocked_out:
            other_trainer.switch_pokemon((other_trainer.active_pokemon+1) % 6)

    def switch_pokemon(self, pokemon):
        if self.pokemons[pokemon].is_knocked_out:
            print(f"Sorry {self.name}, this pokemon is dead, yes DEAD ...")
            if sum(poke.health for poke in self.pokemons) == 0:
                print(f"####################################################")
                print(f"††††{self.name} all your pokemons are dead, you LOST††††")
                print(f"####################################################")
        else:
            print(
                f"{self.name} took {self.pokemons[self.active_pokemon].name} back and sent {self.pokemons[pokemon].name} to fight instead !")
            self.active_pokemon = pokemon


dracofeu = Pokemon("Dracofeu", 50, "Fire", 300)
tortank = Pokemon("Tortank", 50, "Water", 350)
salameche = Pokemon("Salameche", 20, "Fire", 100)
carapucce = Pokemon("Carapucce", 20, "Water", 100)
bulbizard = Pokemon("Bulbizard", 20, "Grass", 100)
florizard = Pokemon("Florizard", 50, "Grass", 400)

mathieu = Trainer("Mathieu", 6, [
                  dracofeu, tortank, salameche, carapucce, bulbizard, florizard], 1)
jehanne = Trainer("Jehanne", 3, [
                  dracofeu, tortank, salameche, carapucce, bulbizard, florizard], 3)

mathieu.attack(jehanne)
jehanne.use_potion()
jehanne.use_potion()
jehanne.use_potion()
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
mathieu.attack(jehanne)
