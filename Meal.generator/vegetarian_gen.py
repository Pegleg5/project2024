#!/usr/bin/env python3

import random

# Dictionary of vegetarian meals and their ingredients
vegetarian_meals = {
    "Vegetable stir-fry with tofu": ["Tofu", "Assorted vegetables (bell peppers, broccoli, carrots, etc.)", "Soy sauce", "Garlic", "Ginger"],
    "Quinoa salad with roasted vegetables": ["Quinoa", "Cherry tomatoes", "Cucumbers", "Red onion", "Lemon juice", "Olive oil"],
    "Chickpea curry": ["Chickpeas", "Tomatoes", "Onion", "Garlic", "Garam masala", "Turmeric", "Coconut milk"],
    "Caprese Salad with Mozzarella and tomatoes": ["Fresh Mozzarella", "Tomatoes", "Fresh basil", "Balsamic glaze", "Olive oil"],
    "Zucchini Noodles with Pesto": ["Zucchini", "Basil pesto", "Cherry tomatoes", "Parmesan cheese"],
    "Black Bean and Sweet Potato Enchiladas": ["Black beans","Sweet potatoes", "Corn tortillas", "Enchilada sauce", "Cheese", "Sour cream"],
    "Mushroom Risotto": ["Arborio rice", "Mushrooms", "onion", "Garlic", "Vegetable broth", "Parmesan cheese"],
    "Greek Salad with Feta and Olives": ["Romaine lettuce", "Cuccumber", "Cherry Tomatoes", "Red onion", "Kalamata olives", "Feta cheese", "Olive oil"],
    "Spinach and Feta Stuffed Peppers": ["Bell peppers", "Spinach", "Feta cheese", "Quinoa", "Garlic", "Onion"],
    "Lentil Soup": ["Lentils", "Carrots", "Celery", "Onion", "Garlic", "Vegetable broth", "Tomato paste", "Bay leaves", "Cumin", "coriander", "Paprika"]
}

# Randomly select a meal
random_meal, ingredients = random.choice(list(vegetarian_meals.items()))

# Display the selected meal and its ingredients
user_input = input("Hello! im assuming you are here because you or a loved one just cannot decide what to eat tonight. Is that correct? Y/N ")
print(user_input)
if user_input.lower() == "y":
    print(f"Today's vegetarian meal suggestion: \n{random_meal}")
    print("Ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
else:
    print(f"Then why are you here? Begone and enjoy your meal!")
