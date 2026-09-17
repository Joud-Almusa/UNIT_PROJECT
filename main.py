from rich.console import Console
from rich.panel import Panel
from ingredients import check_ingredients, view_ingredients

from recommendations import (
    choose_category,
    show_ready_recipes,
    show_almost_possible
)

from storage import save_ingredients, load_ingredients

from validation import get_number_choice


console = Console()


def show_menu():
    console.print(
        Panel.fit(
            "[bold]FRIDGE RESCUE[/bold]\n"
            "Turn what you already have into your next meal.",
            title="Welcome"
        )
    )

    console.print("[bold]1.[/bold] Check / Update My Ingredients")
    console.print("[bold]2.[/bold] Rescue My Fridge")
    console.print("[bold]3.[/bold] Almost Possible Recipes")
    console.print("[bold]4.[/bold] Exit")


def main():
    available_ingredients = load_ingredients()

    while True:
        show_menu()

        choice = get_number_choice(
            "\nChoose an option (1-4): ",
            1,
            4
        )

        if choice == 1:
            available_ingredients = check_ingredients()

            save_ingredients(available_ingredients)

            console.print(
                "\n[bold green]Your fridge has been updated.[/bold green]"
            )

            view_ingredients(available_ingredients)

        elif choice == 2:
            if len(available_ingredients) == 0:
                console.print(
                    "\n[yellow]Please check your ingredients first.[/yellow]"
                )

            else:
                category = choose_category()

                show_ready_recipes(
                    available_ingredients,
                    category
                )

        elif choice == 3:
            if len(available_ingredients) == 0:
                console.print(
                    "\n[yellow]Please check your ingredients first.[/yellow]"
                )

            else:
                category = choose_category()

                show_almost_possible(
                    available_ingredients,
                    category
                )

        elif choice == 4:
            console.print(
                "\n[bold green]Thank you for using Fridge Rescue![/bold green]"
            )
            break


main() 