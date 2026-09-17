# Fridge Rescue

## Overview

**Fridge Rescue** is an interactive Python CLI application that recommends meals based on ingredients the user already has.

The goal of the project is to help users make better use of the food available in their kitchen by identifying:

- Recipes they can prepare immediately.
- Recipes that require only one additional ingredient.

The application uses a rule-based recommendation system written in Python rather than relying on an external recipe API.

---

## Features

- Check and update available ingredients.
- Save ingredients between program sessions using File I/O.
- Recommend recipes that can be made using the user's available ingredients.
- Filter recipe recommendations by meal category.
- Show recipes that are only one ingredient away from being possible.
- Select a recommended recipe to view its full details.
- Display recipe category, estimated preparation time, required ingredients, and instructions.
- Validate numeric and yes/no user input.
- Handle invalid input without ending the program.
- Styled interactive CLI using the `Rich` library.

---

## User Stories

### As a user, I should be able to:

- Tell Fridge Rescue which ingredients I currently have.
- Update my available ingredients.
- Save my fridge ingredients between sessions.
- Find recipes that I can make with my current ingredients.
- Choose a recipe category:
  - Breakfast
  - Lunch
  - Dinner
  - Snack
  - Any
- Find recipes where I am missing only one ingredient.
- Select a recipe from the recommendations.
- View the required ingredients for a recipe.
- View the estimated preparation time.
- View cooking instructions.
- Enter invalid input without causing the application to stop.
- Exit the application when finished.

---

## Main Menu

When Fridge Rescue starts, the following menu is displayed:

```text
1. Check / Update My Ingredients
2. Rescue My Fridge
3. Almost Possible Recipes
4. Exit
```

---

## Usage

### 1. Check / Update My Ingredients

Select:

```text
1
```

Fridge Rescue will ask whether you have each supported ingredient.

Example:

```text
Do you have eggs? yes
Do you have chicken? no
Do you have tuna? no
Do you have bread? yes
Do you have cheese? yes
```

Only `yes` or `no` answers are accepted.

The selected ingredients are saved locally so they can be loaded again when the application is restarted.

---

### 2. Rescue My Fridge

Select:

```text
2
```

The application will ask you to choose a meal category:

```text
1. Breakfast
2. Lunch
3. Dinner
4. Snack
5. Any
```

Fridge Rescue compares your available ingredients with the ingredients required by each recipe.

Only recipes that:

1. Match the selected category, and
2. Can be made using all of your available required ingredients

will be displayed.

Example:

```text
===== READY TO MAKE =====

1. Cheese Omelette
2. Egg & Cheese Toast
3. Grilled Cheese
0. Back
```

Choose a recipe number to view its full details.

Example:

```text
================================
       EGG & CHEESE TOAST
================================

Category: Breakfast
Estimated Time: 10 minutes

Ingredients:
- Eggs
- Cheese
- Bread

Instructions:
1. Cook the egg in a pan.
2. Toast the bread.
3. Place the egg on the bread.
4. Add cheese and serve.
```

Enter:

```text
0
```

to return without selecting a recipe.

---

### 3. Almost Possible Recipes

Select:

```text
3
```

Choose a meal category.

Fridge Rescue will search for recipes where you are missing **exactly one required ingredient**.

Example:

```text
===== ALMOST POSSIBLE =====

1. Tuna Melt
   Missing: Tuna

2. Tomato Pasta
   Missing: Tomato

0. Back
```

You can select one of the recipes to view its full details.

This feature helps the user identify meals they could make by purchasing only one additional ingredient.

---

### 4. Exit

Select:

```text
4
```

to close Fridge Rescue.

---

## Input Validation

Fridge Rescue validates user input throughout the program.

For menu selections, entering an invalid value such as:

```text
hello
```

or:

```text
9
```

will display an error message and ask the user to try again.

For ingredient questions, answers other than:

```text
yes
no
```

will also be rejected.

---

## How the Recommendation System Works

Fridge Rescue stores predefined recipes with:

- Recipe name
- Required ingredients
- Meal category
- Estimated cooking time
- Cooking instructions

For **Ready to Make** recommendations, the program checks whether every required recipe ingredient exists in the user's available ingredients.

For **Almost Possible** recommendations, the program counts the missing ingredients and only displays recipes where exactly one ingredient is missing.

The recommendation logic is implemented directly in Python.

---

## Technologies Used

- Python
- Git
- GitHub
- Rich
- Python File I/O
- Python Modules
- Python Virtual Environments

---

## Python Concepts Used

This project demonstrates:

- Variables
- Strings
- Lists
- Conditional statements
- `for` loops
- `while` loops
- Functions
- Function parameters
- Return values
- Modules
- Imports
- File reading and writing
- Exception handling
- Raising exceptions
- Input validation
- External Python packages
- Virtual environments

---

## Project Structure

```text
UNIT_PROJECT/
│
├── main.py
├── ingredients.py
├── recipes.py
├── recommendations.py
├── validation.py
├── storage.py
├── README.md
├── requirements.txt
└── .gitignore
```

`fridge.txt` is generated locally by the application to store the user's available ingredients.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Joud-Almusa/UNIT_PROJECT.git
```

### 2. Move into the project directory

```bash
cd UNIT_PROJECT
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows Command Prompt

```bash
venv\Scripts\activate
```

#### Git Bash

```bash
source venv/Scripts/activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run:

```bash
python main.py
```

If needed on Windows with Git Bash:

```bash
python.exe main.py
```

---

## External Library

Fridge Rescue uses the `Rich` Python library to improve the appearance of the command-line interface.

It is used for elements such as the welcome panel and styled terminal messages.

The recipe recommendation logic itself is implemented directly in Python.

---

## Data Storage

The user's available ingredients are stored in:

```text
fridge.txt
```

The file is created automatically after the user updates their ingredients.

When Fridge Rescue starts again, the stored ingredients are loaded so the user does not need to enter them again immediately.

---

## Author

**Joud Almusa** 