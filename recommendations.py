import recipes
from validation import get_number_choice


def choose_category():
    print("\n===== CHOOSE A CATEGORY =====")
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")
    print("4. Snack")
    print("5. Any")

    choice = get_number_choice(
        "\nChoose a category (1-5): ",
        1,
        5
    )

    if choice == 1:
        return "breakfast"

    elif choice == 2:
        return "lunch"

    elif choice == 3:
        return "dinner"

    elif choice == 4:
        return "snack"

    else:
        return "any"


def category_matches(recipe_category, selected_category):

    if selected_category == "any":
        return True

    if recipe_category == selected_category:
        return True

    return False


def recipe_is_ready(required_ingredients, available_ingredients):

    for ingredient in required_ingredients:

        if ingredient not in available_ingredients:
            return False

    return True


def show_ready_recipes(available_ingredients, selected_category):

    matching_recipes = []

    for index in range(len(recipes.recipe_names)):

        category = recipes.recipe_categories[index]

        if category_matches(category, selected_category):

            required_ingredients = recipes.recipe_ingredients[index]

            if recipe_is_ready(
                required_ingredients,
                available_ingredients
            ):
                matching_recipes.append(index)

    print("\n===== READY TO MAKE =====")

    if len(matching_recipes) == 0:
        print("No matching recipes found.")
        return

    for number in range(len(matching_recipes)):

        recipe_index = matching_recipes[number]

        print(
            f"{number + 1}. "
            f"{recipes.recipe_names[recipe_index]}"
        )

    print("0. Back")

    choice = get_number_choice(
        "\nChoose a recipe to view: ",
        0,
        len(matching_recipes)
    )

    if choice == 0:
        return

    selected_recipe_index = matching_recipes[choice - 1]

    recipes.show_recipe_details(
        selected_recipe_index
    )


def find_missing_ingredient(
    required_ingredients,
    available_ingredients
):
    missing_count = 0
    missing_ingredient = ""

    for ingredient in required_ingredients:

        if ingredient not in available_ingredients:
            missing_count += 1
            missing_ingredient = ingredient

    if missing_count == 1:
        return missing_ingredient

    return ""


def show_almost_possible(
    available_ingredients,
    selected_category
):

    matching_recipes = []
    missing_ingredients = []

    for index in range(len(recipes.recipe_names)):

        category = recipes.recipe_categories[index]

        if category_matches(category, selected_category):

            required_ingredients = recipes.recipe_ingredients[index]

            missing_ingredient = find_missing_ingredient(
                required_ingredients,
                available_ingredients
            )

            if missing_ingredient != "":
                matching_recipes.append(index)
                missing_ingredients.append(
                    missing_ingredient
                )

    print("\n===== ALMOST POSSIBLE =====")

    if len(matching_recipes) == 0:
        print("No almost-possible recipes found.")
        return

    for number in range(len(matching_recipes)):

        recipe_index = matching_recipes[number]

        print(
            f"\n{number + 1}. "
            f"{recipes.recipe_names[recipe_index]}"
        )

        print(
            f"   Missing: "
            f"{missing_ingredients[number].title()}"
        )

    print("\n0. Back")

    choice = get_number_choice(
        "\nChoose a recipe to view: ",
        0,
        len(matching_recipes)
    )

    if choice == 0:
        return

    selected_recipe_index = matching_recipes[choice - 1]

    recipes.show_recipe_details(
        selected_recipe_index
    ) 