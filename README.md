# Game Character Development

This Python project models a simple RPG-style character system with different classes and abilities.

## Features

- Base `Character` class with core stats (health, mana, strength, intelligence, agility, defense)
- Three character subclasses with unique stats and leveling bonuses:
  - **Warrior** — high health and strength, stronger attacks
  - **Mage** — high mana and intelligence, magical attacks with mana regeneration
  - **Rogue** — high agility, balanced stats, agile attacks
- Level-up mechanics that improve stats based on character class
- `Ability` class representing special skills that consume mana and deal damage
- Basic attack and ability usage with damage calculation and health management

## Usage Example

```python
warrior = Warrior("Aragorn")
mage = Mage("Gandalf")

fireball = Ability("Fireball", mana_cost=20, damage=30)
mage.learn_ability(fireball)

warrior.attack(mage)
mage.use_ability(0, warrior)


Author
Created by Nándor Forgó
📧 nfori.coding@gmail.com
