def get_number_choice(prompt, minimum, maximum):
    while True:
        try:
            choice = int(input(prompt))

            if choice < minimum or choice > maximum:
                raise ValueError

            return choice

        except ValueError:
            print(
                f"Invalid choice. Please enter a number "
                f"from {minimum} to {maximum}."
            )


def get_yes_no(prompt):
    while True:
        answer = input(prompt).lower()

        if answer == "yes" or answer == "no":
            return answer

        else:
            print("Invalid input. Please enter yes or no.")   