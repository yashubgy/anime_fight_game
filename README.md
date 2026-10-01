# Anime Character Battle Engine (Python OOP)

A small project I built to practice Object-Oriented Programming (OOP) in Python and move beyond simple text-based loops like Wordle or Blackjack. 

The goal here is to model anime characters (like Goku and Naruto) with individual stats, transformations, and combat actions loaded dynamically from an external JSON file instead of hardcoding everything in scripts.

---

## Current Features

- **Dynamic Data Ingestion:**
  - Character profiles, stats (HP, Energy/Ki/Chakra, Attack), and awakening forms are read directly from `heros.json`.
  - Uses `.get('form', '0')` to safely handle characters that don't have an awakening form without throwing runtime `KeyError` exceptions.

- **OOP State & Encapsulation:**
  - Base stats (`hp`, `max_hp`, `energy`, `attack`) are managed directly inside the `Character` class instance.
  - Transformation logic checks energy thresholds, applies attack and HP multipliers, and prevents invalid states (like transforming without enough energy or without an awakening form).

- **Turn Combat Actions:**
  - `attack(target)`: Scales damage based on whether the character is currently transformed, then applies it to the enemy instance.
  - `take_damage(amount)`: Clamps health to 0 and prints status alerts (e.g., standard hit, critical hit below 100 HP, or knockout).

- **Roster Inspection with Pandas:**
  - A quick helper function (`show_characters`) reads the JSON into a Pandas DataFrame to inspect the roster table.

---

## File Structure

```text
├── heros.json    # JSON config holding characters, stats, and form multipliers
├── main.py       # Character class definition, methods, and test run
└── README.md
