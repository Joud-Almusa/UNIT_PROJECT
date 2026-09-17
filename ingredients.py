from validation import get_yes_no


ingredients_list = [
    "eggs",
    "chicken",
    "tuna",
    "bread",
    "rice",
    "pasta",
    "potatoes",
    "cheese",
    "milk",
    "yogurt",
    "tomato",
    "onion",
    "bell pepper",
    "garlic",
    "corn"
]


def check_ingredients():
    available_ingredients = []

    print("\nLet's check what's in your kitchen.")
    print("Answer with yes or no.\n")

    for ingredient in ingredients_list:
        answer = get_yes_no(
            f"Do you have {ingredient}? "
        )

        if answer == "yes":
            available_ingredients.append(ingredient)

    return available_ingredients


def view_ingredients(available_ingredients):
    print("\n===== MY FRIDGE =====")

    if len(available_ingredients) == 0:
        print("Your fridge is currently empty.")

    else:
        for ingredient in available_ingredients:
            print(f"- {ingredient.title()}")   