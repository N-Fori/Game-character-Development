class Character:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

        # Base stats - will be adjusted by subclasses
        self.max_health = 100
        self.health = 100
        self.max_mana = 50
        self.mana = 50
        self.strength = 10
        self.intelligence = 10
        self.agility = 10
        self.defense = 5

        self.abilities = []

    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        self.max_mana += 5
        self.mana = self.max_mana
        self.strength += 1
        self.intelligence += 1
        self.agility += 1
        self.defense += 1
        return f"{self.name} leveled up to level {self.level}!"

    def attack(self, target):
        damage = self.strength * 0.8
        damage_dealt = target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")
        return damage_dealt

    def take_damage(self, amount):
        effective_damage = max(1, amount - self.defense * 0.5)
        self.health = max(0, self.health - effective_damage)
        return effective_damage

    def is_alive(self):
        return self.health > 0

    def learn_ability(self, ability):
        self.abilities.append(ability)

    def use_ability(self, ability_index, target):
        if ability_index < 0 or ability_index >= len(self.abilities):
            return 0

        ability = self.abilities[ability_index]
        return ability.use(self, target)


class Warrior(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        # Warriors have more health and strength, less mana and intelligence
        self.max_health = 150
        self.health = 150
        self.max_mana = 30
        self.mana = 30
        self.strength = 15
        self.intelligence = 5
        self.defense = 8

    def level_up(self):
        result = super().level_up()
        # Extra strength bonus for warriors
        self.strength += 2
        self.max_health += 10  # Extra health for warriors
        self.health = self.max_health
        return result

    def attack(self, target):
        # Warriors have a stronger basic attack
        damage = self.strength * 1.2
        damage_dealt = target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")
        return damage_dealt


class Mage(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        # Mages have more mana and intelligence, less health and strength
        self.max_health = 80
        self.health = 80
        self.max_mana = 150
        self.mana = 150
        self.strength = 5
        self.intelligence = 20
        self.defense = 3

    def level_up(self):
        result = super().level_up()
        self.intelligence += 2  # Extra intelligence bonus for mages
        self.max_mana += 15  # Extra mana for mages
        self.mana = self.max_mana
        return result

    def attack(self, target):
        # Mages use intelligence for basic attacks
        damage = self.intelligence * 0.4
        damage_dealt = target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")

        # Mages regain some mana on basic attacks
        mana_regen = 5
        self.mana = min(self.max_mana, self.mana + mana_regen)

        return damage_dealt


class Rogue(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        # Rogues have more agility, balanced other stats
        self.max_health = 100
        self.health = 100
        self.max_mana = 60
        self.mana = 60
        self.strength = 12
        self.intelligence = 8
        self.agility = 18
        self.defense = 4

    def level_up(self):
        result = super().level_up()
        # Extra agility bonus for rogues
        self.agility += 2
        return result

    def attack(self, target):
        # Rogues use agility for stronger attacks
        damage = self.strength * 0.5 + self.agility * 0.7
        damage_dealt = target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")
        return damage_dealt


class Ability:
    def __init__(self, name, mana_cost, damage):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage

    def use(self, character, target):
        if character.mana < self.mana_cost:
            print(f"{character.name} doesn't have enough mana to use {self.name}")
            return 0

        character.mana -= self.mana_cost

        # Calculate damage
        if hasattr(character, 'intelligence'):
            # Scale with intelligence for magical abilities
            damage = self.damage + (character.intelligence * 0.5)
        else:
            damage = self.damage

        damage_dealt = target.take_damage(damage)
        print(f"{character.name} used {self.name} on {target.name} for {damage_dealt:.1f} damage!")

        return damage_dealt