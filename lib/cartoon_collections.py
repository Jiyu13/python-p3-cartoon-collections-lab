def roll_call_dwarves(dwarves):
    for i in range(len(dwarves)):
        print(f"{i+1}. {dwarves[i]}")


def summon_captain_planet(planeteer_calls):
    return [f"{call.capitalize()}!" for call in planeteer_calls]

def long_planeteer_calls(short_words):
    for i in range(len(short_words)):
        if len(short_words[i]) > 4:
            return True
    return False

def find_the_cheese(snacks):
    for snack in snacks:
        if snack in ["cheddar", "gouda",  "camembert"]:
            return snack
