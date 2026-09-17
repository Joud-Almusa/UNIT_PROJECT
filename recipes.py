recipe_names = [
    "Cheese Omelette",
    "Egg & Cheese Toast",
    "Grilled Cheese",
    "Tuna Sandwich",
    "Tuna Melt",
    "Tomato Pasta",
    "Creamy Cheese Pasta",
    "Chicken Rice Bowl",
    "Chicken & Potato Bowl",
    "Egg Fried Rice"
]


recipe_ingredients = [
    ["eggs", "cheese"],
    ["eggs", "cheese", "bread"],
    ["bread", "cheese"],
    ["tuna", "bread"],
    ["tuna", "bread", "cheese"],
    ["pasta", "tomato", "onion", "garlic"],
    ["pasta", "milk", "cheese", "garlic"],
    ["chicken", "rice", "onion"],
    ["chicken", "potatoes", "onion"],
    ["eggs", "rice", "onion"]
]


recipe_categories = [
    "breakfast",
    "breakfast",
    "snack",
    "lunch",
    "lunch",
    "dinner",
    "dinner",
    "dinner",
    "dinner",
    "lunch"
]


recipe_times = [
    10,
    10,
    10,
    10,
    15,
    25,
    20,
    30,
    35,
    15
]


recipe_instructions = [
    """1. Beat the eggs.
2. Pour them into a heated pan.
3. Add the cheese.
4. Fold the omelette and serve.""",

    """1. Cook the egg in a pan.
2. Toast the bread.
3. Place the egg on the bread.
4. Add cheese and serve.""",

    """1. Place cheese between two slices of bread.
2. Toast the sandwich in a pan.
3. Cook until the bread is golden and the cheese melts.""",

    """1. Prepare the tuna.
2. Place the tuna between slices of bread.
3. Add seasoning if desired.
4. Serve.""",

    """1. Prepare the tuna.
2. Place tuna and cheese between slices of bread.
3. Toast until the cheese melts.
4. Serve warm.""",

    """1. Cook the pasta.
2. Chop the tomato, onion, and garlic.
3. Cook the vegetables in a pan.
4. Add the pasta and mix well.
5. Serve warm.""",

    """1. Cook the pasta.
2. Heat the milk gently in a pan.
3. Add cheese and garlic.
4. Stir until creamy.
5. Add the pasta and mix well.""",

    """1. Cook the rice.
2. Cook the chicken thoroughly.
3. Cook the onion until soft.
4. Combine the chicken, rice, and onion.
5. Serve in a bowl.""",

    """1. Cook the potatoes until tender.
2. Cook the chicken thoroughly.
3. Cook the onion until soft.
4. Combine everything in a bowl.
5. Serve warm.""",

    """1. Cook the rice.
2. Cook the onion in a pan.
3. Add the eggs and scramble them.
4. Add the rice.
5. Mix everything together and serve."""
]


def show_recipe_details(recipe_index):
    print("\n================================")
    print(f"       {recipe_names[recipe_index].upper()}")
    print("================================")

    print(
        f"\nCategory: "
        f"{recipe_categories[recipe_index].title()}"
    )

    print(
        f"Estimated Time: "
        f"{recipe_times[recipe_index]} minutes"
    )

    print("\nIngredients:")

    for ingredient in recipe_ingredients[recipe_index]:
        print(f"- {ingredient.title()}")

    print("\nInstructions:")
    print(recipe_instructions[recipe_index]) 