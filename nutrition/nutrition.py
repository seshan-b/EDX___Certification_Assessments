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
# 3. Loop through each fruit in the `fruits` list:
def check_fruit_calories(fruit_calories):
    while True:
        # 4. Prompt the user for Item Which fruit
        user_fruit = input("Which fruit would you like to check? (or type 'exit' to quit): ").strip().lower()
        if user_fruit == 'exit':
            break
        #    a. Check if the fruit is in the `fruit_calories` dictionary.
        if user_fruit in fruit_calories:
            #    b. If the fruit is in the dictionary, print the fruit and its calorie count.
            print(f"{user_fruit.capitalize()} has {fruit_calories[user_fruit]} calories.")
        else:
            #    c. If the fruit is not in the dictionary, print that the fruit is not found.
            print(f"Sorry, we don't have calorie information for {user_fruit}.")

# Main function to initialize the dictionary and check the fruit calories
def main():
    fruit_calories = initialize_fruit_calories()
    check_fruit_calories(fruit_calories)

if __name__ == "__main__":
    main()
