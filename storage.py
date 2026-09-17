FRIDGE_FILE = "fridge.txt"


def save_ingredients(available_ingredients):
    file = open(FRIDGE_FILE, "w", encoding="utf-8")

    for ingredient in available_ingredients:
        file.write(ingredient + "\n")

    file.close()


def load_ingredients():
    try:
        file = open(FRIDGE_FILE, "r", encoding="utf-8")

        lines = file.readlines()
        file.close()

        available_ingredients = []

        for line in lines:
            ingredient = line.strip()

            if ingredient != "":
                available_ingredients.append(ingredient)

        return available_ingredients

    except FileNotFoundError:
        return []

    