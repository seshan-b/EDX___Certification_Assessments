### Breaking down the problem
# Use a conditional with 20 Boolean expressions
# One for each fruit,
# Use a dict to associate a fruit with its calories!
# If k is a str and d is a dict, you can check whether k is a key in d with code like:
# Eg: if k in d:


# 1. Initialize a dictionary called `fruit_calories` with fruit names as keys and their calorie counts as values.
def initialize_fruit_calories():
    fruit_calories = {
        'apple': 130,
        'avocado': 50,
        'kiwifruit': 90,
        'pear': 100,
        'sweet cherries': 100
    }
    return fruit_calories

# 2. Create a list called `fruits` containing the names of the fruits to check.
def check_fruit_calories(fruit_calories, fruits):
    # 3. Loop through each fruit in the `fruits` list:
    for fruit in fruits:
        #    a. Check if the fruit is in the `fruit_calories` dictionary.
        if fruit in fruit_calories:
            #    b. If the fruit is in the dictionary, print the fruit and its calorie count.
            print(f"fruit: {fruit}, calories: {fruit_calories[fruit]}")
        else:
            #    c. If the fruit is not in the dictionary, print that the fruit is not found.
            print(f"fruit: {fruit} is not found")

# 4. Prompt the user for Item Which fruit
def main():
    fruit_calories = initialize_fruit_calories()

    # Create a list of fruits
    fruits = ['apple', 'avocado', 'kiwifruit', 'pear', 'sweet cherries']

    check_fruit_calories(fruit_calories, fruits)

    while True:
        user_fruit = input("Which fruit would you like to check? (or type 'exit' to quit): ").lower()
        if user_fruit == 'exit':
            break
        normalized_fruit = user_fruit.strip().lower()
        if normalized_fruit in fruit_calories:
            print(f"{user_fruit.capitalize()} has {fruit_calories[normalized_fruit]} calories.")
        else:
            print(f"Sorry, we don't have calorie information for {user_fruit}.")

if __name__ == "__main__":
    main()
