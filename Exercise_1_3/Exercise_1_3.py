recipes_list = []
ingredients_list = []

def take_recipe():
    
    name = input("Enter your recipe name: ")
    cooking_time = int(input("Enter your cooking time in minutes: "))
    
    ingredients = []
    ingredientInput = input("Enter an ingredient: ")
    ingredients.append(ingredientInput)
    while(True):
        ingredientInput = input("Enter another ingredient or press q to quit: ")
        if ingredientInput == "q":
            break
        ingredients.append(ingredientInput)
    recipe ={"name" : name, "cooking_time":cooking_time, "ingredients": ingredients}
    return recipe

n = int(input("Enter how many recipes you want to make: "))    
for i in range(0, n , 1):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)
    
for recipe in recipes_list:
    print("Recipe: ", recipe['name'])
    print("Cooking Time: ", str(recipe['cooking_time']))
    print("Ingredients: ")
    for ingredient in recipe['ingredients']:
        print(ingredient)
    if(recipe['cooking_time'] < 10 ):
        if(len(recipe['ingredients']) < 4):
            print("Difficulty level: Easy")
        elif (len(recipe['ingredients']) >= 4):
            print("Difficulty Level: Medium")
    elif(recipe['cooking_time'] >= 10 ):
        if(len(recipe['ingredients']) < 4):
            print("Difficulty level: Intermediate")
        elif (len(recipe['ingredients']) >= 4):
            print("Difficulty Level: Hard")

ingredients_list.sort()
print("Ingredients Available Across All Recipes")
print("----------------------------------------")
for ingredient in ingredients_list:
    print(ingredient)