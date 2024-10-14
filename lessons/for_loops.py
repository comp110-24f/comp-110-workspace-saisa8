"""For loops syntax + practice!

pets: list[str] = ["Louie", "Bo", "Bear"]
# Tell every pet they're a good boy
for animal in pets:
    print(f"Good boy, {animal}!")  # "Good boy, " + animal + "!
"""

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(f{idx} + ": " + {names[idx]})
